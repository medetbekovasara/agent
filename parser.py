from google_play_scraper import reviews
import json

def fetch_reviews(app_id="com.maanavan.mb_kyrgyzstan", count=20, lang="ru", country="kg"):
    result, _ = reviews(
        app_id,
        lang=lang,
        country=country,
        count=count
    )
    return result

def write_to_json(data):
    with open('mbank_reviews.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def get_review_data(app_id):
    reviews_data = fetch_reviews(app_id)
    review_list = []

    for review in reviews_data:
        try:
            content = review['content'].strip()
        except:
            content = ''
        try:
            score = review['score']
        except:
            score = ''
        try:
            date = str(review['at'])
        except:
            date = ''

        review_list.append({
            'text': content,
            'rating': score,
            'date': date
        })

    write_to_json(review_list)

def main():
    app_id = 'com.maanavan.mb_kyrgyzstan'
    get_review_data(app_id)

main()
