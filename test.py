from transformers import pipeline

summarizer = pipeline("summarization", model="IlyaGusev/rut5-base-summarization")

text = "Мобильное приложение стало неудобным после обновления. Часто приходится заново входить, и некоторые функции стали недоступны."

summary = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]["summary_text"]

print("Сводка:", summary)


# import json
# from abstractive import abstractive_summary

# reviews = [
#     "Самый худший банк, не рекомендую. Деньги пропадают, постоянно программа зависает.",
#     "Приложение хорошее, но всегда тупит и иногда у меня пропадают деньги. Я писала, но мне не помогли.",
#     "Всё отлично! Пользуюсь давно, нареканий нет.",
#     "Совсем перестал работать. Войти невозможно.",
#     "Очень неудобный интерфейс и медленная поддержка."
# ]

# print("🔍 Абстрактивные сводки отзывов:\n")

# for i, review in enumerate(reviews, 1):
#     print(f"📝 Отзыв #{i}: {review}")
#     summary = abstractive_summary(review)
#     print(f"🔸 Абстрактивная сводка: {summary}")
#     print("-" * 60)



# экстракт
# from razdel import sentenize
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# def extractive_summary(text, top_n=1):
#     sentences = [s.text.strip() for s in sentenize(text) if s.text.strip()]

#     if len(sentences) <= top_n:
#         return " ".join(sentences)

#     embeddings = model.encode(sentences)
#     mean_embedding = np.mean(embeddings, axis=0)
#     scores = cosine_similarity([mean_embedding], embeddings)[0]

#     top_indices = np.argsort(scores)[-top_n:]
#     top_indices.sort()

#     return " ".join([sentences[i] for i in top_indices])




