from django.urls import path
from .views import HomeView, ArticleDetailView, login
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug>',ArticleDetailView.as_view(),name='article_detail'),
    path('login/',login,name='login'),
]
