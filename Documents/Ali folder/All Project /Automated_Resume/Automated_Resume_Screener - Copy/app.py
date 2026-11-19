import os
import re
import fitz
import pytesseract
import nltk
import streamlit as st
import matplotlib.pyplot as plt

from PIL import Image
from nltk.corpus import stopwords

# ===============================
# BASIC CONFIG
# ===============================
RESUME_FOLDER = r"G:\Resume"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


st.set_page_config(
    page_title="Automated Resume Screener",
    layout="wide"
)

# ===============================
# FUNCTIONS
# ===============================
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)

    try:
        stop_words = set(stopwords.words('english'))
    except:
        # fallback basic stopwords (offline-safe)
        stop_words = {
            "the","and","is","in","to","of","for","with","on","as","by",
            "an","be","are","at","from","this","that","or"
        }

    return ' '.join(word for word in text.split() if word not in stop_words)


def extract_text_from_pdf_ocr(pdf_path):
    text = ""
    pdf = fitz.open(pdf_path)
    for page in pdf:
        pix = page.get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        text += pytesseract.image_to_string(img)
    return text

def skill_match_and_gap(resume_text, skills):
    matched = [s for s in skills if s in resume_text]
    missing = [s for s in skills if s not in resume_text]
    return matched, missing

# ===============================
# UI HEADER
# ===============================
st.title("📄 Automated Resume Screener")
st.write("OCR-based, skill-driven resume screening (Auto-Run Mode)")
st.info("🔄 Results update automatically when skills or resumes change")

# ===============================
# SIDEBAR — SKILL SELECTION
# ===============================
st.sidebar.header("🔧 Define Required Skills")

aerospace_skills = st.sidebar.multiselect(
    "Aerospace Core",
    ["aerodynamics", "aircraft performance", "uav", "propulsion", "cfd", "flight stability"],
    default=["uav", "aerodynamics"]
)

tools_skills = st.sidebar.multiselect(
    "Tools & Software",
    ["matlab", "python", "catia", "solidworks", "ansys", "cad", "cnc"],
    default=["matlab", "solidworks"]
)

project_skills = st.sidebar.multiselect(
    "Projects & Practical",
    ["drone", "ornithopter", "wing design", "simulation", "testing"],
    default=["drone"]
)

all_skills = aerospace_skills + tools_skills + project_skills

# ===============================
# AUTO-RUN ANALYSIS (NO BUTTON)
# ===============================
if not all_skills:
    st.warning("Please select at least one skill to start analysis.")
else:
    if not os.path.exists(RESUME_FOLDER):
        st.error("Resume folder not found.")
    else:
        resume_files = [f for f in os.listdir(RESUME_FOLDER) if f.lower().endswith(".pdf")]

        if not resume_files:
            st.warning("No PDF resumes found in the folder.")
        else:
            results = {}

            for file in resume_files:
                path = os.path.join(RESUME_FOLDER, file)

                raw_text = extract_text_from_pdf_ocr(path)
                clean_text = preprocess_text(raw_text)

                matched, missing = skill_match_and_gap(clean_text, all_skills)

                score = (
                    len([s for s in matched if s in aerospace_skills]) * 0.5 +
                    len([s for s in matched if s in tools_skills]) * 0.3 +
                    len([s for s in matched if s in project_skills]) * 0.2
                )

                results[file] = {
                    "Matched": matched,
                    "Missing": missing,
                    "Score": round(score, 2)
                }

            # ===============================
            # DISPLAY RESULTS
            # ===============================
            st.subheader("📊 Resume Analysis")

            for name, data in results.items():
                with st.expander(f"📄 {name}"):
                    st.write("✅ Matched Skills:", data["Matched"])
                    st.write("❌ Missing Skills:", data["Missing"])
                    st.write("⭐ Final Score:", data["Score"])

            # ===============================
            # RANKING
            # ===============================
            ranking = sorted(results.items(), key=lambda x: x[1]["Score"], reverse=True)

            st.subheader("🏆 Final Ranking")
            for i, (name, data) in enumerate(ranking, start=1):
                st.write(f"{i}. {name} → Score: {data['Score']}")

            # ===============================
            # GRAPH
            # ===============================
            names = [r[0] for r in ranking]
            scores = [r[1]["Score"] for r in ranking]

            fig, ax = plt.subplots()
            ax.barh(names, scores)
            ax.set_xlabel("Final Skill Score")
            ax.set_title("Resume Ranking")
            ax.invert_yaxis()

            st.pyplot(fig)
