from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get (self, request, *args, **kwargs):
        tags = ['acticle']
        return render(request, 'articles/article.html', context={'tags': tags})
