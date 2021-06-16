from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.


def index(request):
	newsapi = NewsApiClient(api_key='a8dde8010d144ca6a2d8bbf892e75cec')
	top_headlines = newsapi.get_top_headlines(
                                          language='en',
                                          country='in')
	a = top_headlines['articles']
	res = []
	for i in range(0,len(a)):
		res.append({"title":a[i]['title'],"date":a[i]['publishedAt'],"content":a[i]['content'],"img":a[i]['urlToImage'],"link":a[i]['url']})
	return render(request,'news/index.html',{
	"res":res
	})
	# top_headlines = newsapi.get_top_headlines(language='en',country='in')
	# 