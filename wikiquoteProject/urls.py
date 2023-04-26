"""wikiquoteProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wikiquote_app.views import ArticlesAPIView, CatrgoryDetailAPIView, ArticleAPIView, AllArticlesAPIView, CatrgoriesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/<str:arctcieName>', ArticleAPIView.as_view()),
    path('api/add_article', ArticlesAPIView.as_view()),
    path('api/view_articles', AllArticlesAPIView.as_view()),
    path('category/<str:slug>', CatrgoryDetailAPIView.as_view()),
    path('category', CatrgoriesAPIView.as_view()),
]
