from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'    # 리스트의 순서를 pk의 역순으로


class PostDetail(DetailView):
    model = Post
