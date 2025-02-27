import streamlit as st
import os
from resume_parser import extract_text_from_resume
from job_matcher import rank_resumes

# Streamlit UI
st.title("📄 Resume Scanner & Ranker")
st.write("Upload resumes and enter a job description to find the best match.")

# Upload resumes
uploaded_files = st.file_uploader("Upload Resumes (PDF/DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

# Input job description
job_description = st.text_area("Enter Job Description")

if st.button("Scan Resumes"):
    if uploaded_files and job_description:
        st.write("### Results")
        resume_texts = {file.name: extract_text_from_resume(file) for file in uploaded_files}
        rankings = rank_resumes(resume_texts, job_description)
        
        for rank, (name, score) in enumerate(rankings, start=1):
            st.write(f"**{rank}. {name}** - Score: {score *1000:.2f}")
    else:
        st.warning("Please upload resumes and enter a job description.")
# Copyright Footer
st.markdown("---")
st.markdown("© 2025 Ritesh Chakramani. All rights reserved.")