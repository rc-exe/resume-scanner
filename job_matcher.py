import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def rank_resumes(resume_texts, job_description):
    """Rank resumes based on similarity to the job description."""
    texts = [job_description] + list(resume_texts.values())
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    rankings = sorted(zip(resume_texts.keys(), cosine_similarities[0]), key=lambda x: x[1], reverse=True)
    return rankings
