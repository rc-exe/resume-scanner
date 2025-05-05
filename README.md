

markdown
# Resume Scanner & Ranker

This project allows users to upload resumes and rank them based on a job description. The application uses NLP techniques to extract text from resumes and match them against the provided job description to find the best match.

## Features

- Upload multiple resumes in PDF or DOCX format.
- Input a job description for matching.
- Rank resumes based on their relevance to the job description.
- Display the rankings and scores in a user-friendly interface using Streamlit.

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- streamlit
- resume-parser
- joblib
- spacy
- scikit-learn
- nltk
- python-docx
- PyPDF2

## Setup Instructions

### Step 1: Clone the Repository

Clone the project repository to your local machine:

bash
git clone https://github.com/yourusername/resume-scanner.git
cd resume-scanner


### Step 2: Create a Virtual Environment

1. Open your terminal or command prompt and navigate to the project directory.
2. Create a virtual environment with the following command:

   bash
   python -m venv venv
   

### Step 3: Activate the Virtual Environment

 For Windows:

  bash
  venv\Scripts\activate
  

 For Mac/Linux:

  bash
  source venv/bin/activate
  

### Step 4: Install Dependencies

Once the virtual environment is activated, install the required Python libraries by running:

bash
pip install -r requirements.txt


### Step 5: Download the spaCy Language Model

To use spaCy for natural language processing, download the English language model:

bash
python -m spacy download en_core_web_sm


### Step 6: Run the Application

After setting up the environment, you can run the application using Streamlit:

bash
streamlit run app.py


This will start the Streamlit application and open it in your default web browser at http://localhost:8501.

## How to Use

1. Upload Resumes: Upload resumes in PDF or DOCX format using the "Upload Resumes" section.
2. Enter Job Description: Input a job description in the provided text box.
3. Scan Resumes: Click the "Scan Resumes" button to process and rank the uploaded resumes based on their relevance to the job description.
4. View Results: The resumes will be ranked with scores, and the best matches will be displayed at the top.

## Project Structure

plaintext
resume-scanner/
├── app.py                  # Main application file
├── job_matcher.py          # Job matching logic and ranking
├── resume_parser.py        # Resume parsing and text extraction
├── requirements.txt        # List of project dependencies
├── README.md               # Project documentation
└── venv/                   # Virtual environment


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

 [Streamlit](https://streamlit.io/)
 [spaCy](https://spacy.io/)
 [scikit-learn](https://scikit-learn.org/)
 [python-docx](https://python-docx.readthedocs.io/en/latest/)
 [PyPDF2](https://pythonhosted.org/PyPDF2/)



This file should include all the necessary instructions and steps for setting up, running, and understanding the project. You can now use it as the README.md file in your repository.

