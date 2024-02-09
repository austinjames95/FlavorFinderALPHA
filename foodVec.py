from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(description1, description2):
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the descriptions
    tfidf_matrix = vectorizer.fit_transform([description1, description2])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]

    return cosine_sim
