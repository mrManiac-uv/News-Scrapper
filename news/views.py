# from rest_framework import generics
# from news.models import NewsItem
# from news.serializer import NewsItemSerializer
# from news.newsAPI import getNews


# class NewsItemList(generics.ListAPIView):
#     # Retrieving all news items from database
#     queryset = NewsItem.objects.all()
#     serializer_class = NewsItemSerializer

#     def getQueryset(self):
#         # Retrieving news items from News API
#         news_items = getNews()
#         print(news_items)

#         # Saving the news items to the database
#         for news_item in news_items:
#             NewsItem.objects.create(**news_item)
#             NewsItem.save()

#         return news_items

from django.http import JsonResponse
from django.views import View
from news.newsAPI import getNews


class NewsItemList(View):
    def get(self, request):
        # Scraping news data for BBC News
        bbc = getNews(['bbc-news'])

        # Scraping news data for Reuters
        reuters = getNews(['reuters'])

        # Formatting
        bbc_data = {
            "status": "ok",
            "data": bbc,
        }
        reuters_data = {
            "status": "ok",
            "data": reuters,
        }

        # Returning a dictionary with the sources separated
        response_data = {
            "Source: BBC NEWS": bbc_data,
            "Source: Reuters": reuters_data,
        }

        return JsonResponse(response_data, status=200)
