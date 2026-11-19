# 📄 Automated Resume Screener  
## OCR-Based Skill-Driven Resume Screening & Ranking System

---

## 🔍 Project Overview

The **Automated Resume Screener** is a complete end-to-end system designed to **analyze, differentiate, and rank resumes automatically** using **OCR (Optical Character Recognition)** and **skill-based logic**.

Unlike traditional resume screening systems that fail on scanned or image-based resumes, this project **successfully processes designed PDF resumes** (such as Canva-style or scanned resumes) and evaluates candidates objectively based on **explicitly defined skills**.

The system provides an **interactive GUI** that allows users to dynamically select skills and instantly view:
- Skill matches
- Skill gaps
- Candidate ranking
- Visual score comparison  

All results update **automatically without rerunning terminal commands**.

---

## 🎯 Problem Statement

Manual resume screening is:
- Time-consuming
- Subjective
- Error-prone
- Inefficient for large volumes

Additionally, many automated systems fail because:
- Resumes are image-based PDFs
- Text extraction returns empty results
- Skill matching becomes impossible

This project solves both problems by:
1. Using **OCR** to read image-based resumes
2. Using **structured skill-based evaluation** instead of vague keyword matching

---

## ✅ Key Features

- 📄 Supports **image-based / scanned PDF resumes**
- 🔍 OCR-based text extraction using **Tesseract**
- 🧠 Skill-driven job requirement definition
- ✅ Skill match analysis
- ❌ Skill gap identification
- ⭐ Weighted scoring and ranking
- 📊 Visual comparison using graphs
- 🖥️ Interactive **Streamlit GUI**
- 🔄 Auto-rerun (no repeated terminal actions)

---

## 🧠 Core Concept

> **Job requirements are defined explicitly using skills, not free text.**

The system:
- Converts resumes into text using OCR
- Matches resume content against required skills
- Applies weighted scoring based on skill categories
- Ranks candidates objectively and transparently

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---------|--------|
| Python | Core programming language |
| Streamlit | GUI development |
| PyMuPDF | PDF handling |
| Tesseract OCR | Text extraction from images |
| Pillow | Image processing |
| NLTK | Text preprocessing |
| Matplotlib | Data visualization |

---

## 📂 Project Structure

Automated_Resume_Screener/
│
├── app.py # Main Streamlit GUI application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── resumes/ # Folder containing PDF resumes
│ ├── 1.pdf
│ ├── 2.pdf
│
└── screenshots/ # GUI & output screenshots (optional)

---

## ⚙️ Installation & Setup

### 🔹 Step 1: Install Tesseract OCR (Mandatory)

Download and install Tesseract OCR from the official repository:

https://github.com/UB-Mannheim/tesseract/wiki

**Default installation path (Windows):**
C:\Program Files\Tesseract-OCR\tesseract.exe

> ⚠️ If installed in a different location, update the path in `app.py`.

---

### 🔹 Step 2: Install Python Dependencies

Open terminal inside the project folder and run:

```bash
pip install -r requirements.txt

streamlit run app.py

http://localhost:8501
