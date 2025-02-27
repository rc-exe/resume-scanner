 Resume Scanner & Ranker

This project is a **Resume Scanner & Ranker** built using **Streamlit**. It allows users to upload resumes in **PDF/DOCX** format and compare them against a **job description** using **NLP-based ranking**.

 Features
✅ Upload multiple resumes (**PDF/DOCX**)
✅ Extract text from resumes
✅ Enter a job description
✅ Rank resumes based on job description relevance
✅ Display scores in percentage format

 Installation
 Prerequisites
- Python 3.x installed
- VS Code (or any IDE of your choice)

 Install Dependencies
Run the following command to install the required libraries:
```bash
pip install streamlit PyPDF2 python-docx spacy scikit-learn
python -m spacy download en_core_web_sm
```

 How to Run the Project
Run the following command in your terminal:
```bash
streamlit run app.py
```
This will launch the Streamlit web app.

 Project Structure
```
resume-scanner/
│── app.py                Streamlit UI
│── resume_parser.py      Extracts text from resumes
│── job_matcher.py        Compares resumes with job descriptions
│── requirements.txt      Dependencies
│── sample_resumes/       Folder for test resumes
```

 Usage
1. Upload one or more resumes in **PDF/DOCX** format.
2. Enter a **job description** in the provided text area.
3. Click on **Scan Resumes** to analyze and rank resumes.
4. View the ranked list with similarity scores in percentage.

 License
© 2025 Ritesh Chakramani. All rights reserved.

