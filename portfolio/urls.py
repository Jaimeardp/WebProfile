from django.conf.urls import url
from django.urls import path

from portfolio.views import portfolio_list_view

urlpatterns = [
    path('list', portfolio_list_view, name="portfolio_view")
]