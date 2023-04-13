import requests
import json


API_KEY = 'a7d0000b4b324a93919c1323cfb63edd'


def getNews(sources):
    # Fetching data from API
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'sources': ','.join(sources),
        'apiKey': API_KEY,
    }
    response = requests.get(url, params=params)

    # Converting into JSON
    data = json.loads(response.text)
    articles = data['articles']
    news_items = []
    # Formatting
    for article in articles:
        news_item = {
            'title': article['title'],
            'details': article['description'],
            'postedAt': article['publishedAt']
        }
        news_items.append(news_item)
    return news_items
