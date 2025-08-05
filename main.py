from extractive import extractive_summary
from abstractive import abstractive_summary
import json

# Загружаем отзывы из JSON
with open('mbank_reviews.json', 'r', encoding='utf-8') as f:
    reviews_data = json.load(f)

for i, review_obj in enumerate(reviews_data, 1):
    review_text = review_obj.strip() if isinstance(review_obj, str) else review_obj.get("text", "").strip()

    if len(review_text) < 5:
        continue

    print(f"📝 Отзыв #{i}: {review_text}")

    # Экстрактивная
    extractive = extractive_summary(review_text)
    if extractive.strip() == review_text.strip():
        print(f"🔹 Экстрактивная сводка: {extractive} (Не удалось сократить — вывод совпадает с оригиналом)")
    else:
        print(f"🔹 Экстрактивная сводка: {extractive}")

    # Абстрактивная
    summary = abstractive_summary(review_text)
    print(f"🔸 Абстрактивная сводка: {summary}")

    print("-" * 60)
