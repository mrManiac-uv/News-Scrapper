from django.urls import path
from news.views import NewsItemList

urlpatterns = [
    path('api/news/', NewsItemList.as_view(), name='news_list'),
]
