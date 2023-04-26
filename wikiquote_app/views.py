from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article, Category
from .serializers import ArticleSerializer
import json

from .serializers import ArticleSerializer

# Create your views here.

class ArticlesAPIView(APIView):    
    def post(self, request):
        for article in request.data:
            categories = []
            for category in article['category']:
                categories.append(Category.objects.get_or_create(name = category)[0])
        
            new_article = Article.objects.create(
                title = article['title'],
                language = article['language'],
                wiki = article['wiki'],
                auxiliary_text = article['auxiliary_text'],
                create_timestamp = article['create_timestamp'],
                timestamp = article['timestamp'],
            )
            new_article.category.add(*categories)
            serializer = ArticleSerializer(new_article, many=True)

        return Response({'succes': {'title': new_article.title}})

class AllArticlesAPIView(APIView):
    def get(self, request):
        list = Article.objects.all().values()
        return Response({'data': list})


class ArticleAPIView(APIView):
    def get(self, request , arctcieName):
        article = Article.objects.filter(title__iexact = arctcieName)
        serializer = ArticleSerializer(article, many = True) 

        #json will be pretty if save it in file, but now it is just formatted string
        if request.GET.get("pretty") == 'true':
            return Response(json.dumps(serializer.data, indent=2))
        else:
            return Response(serializer.data)

class CatrgoriesAPIView(APIView):
    def get(self, request):
        for cat in Category.objects.all():
            cat.save()
        categories = Category.objects.all().values()

        return Response({'data': categories})
    
class CatrgoryDetailAPIView(APIView):
    def get(self, request , slug):
        category = Category.objects.get(slug=slug)
        articles = Article.objects.filter(category__name = category)
        serializer = ArticleSerializer(articles, many = True)

        return Response({"category_name": category.name, "articles": serializer.data})
    