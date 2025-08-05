from razdel import sentenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extractive_summary(text):
    # Разбиваем на предложения
    sentences = [s.text.strip() for s in sentenize(text) if s.text.strip()]
    
    if not sentences:
        return ""
    if len(sentences) == 1:
        return sentences[0]

    # TF-IDF векторизация
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Вычисляем вес каждого предложения
    scores = tfidf_matrix.sum(axis=1).A1

    # Находим индекс предложения с наибольшим весом
    best_index = np.argmax(scores)

    # Возвращаем только одно самое значимое предложение
    return sentences[best_index]

