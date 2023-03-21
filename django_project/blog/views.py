from django.shortcuts import render

from .models import Post


# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-pk')  # 현재 DB에서 post class에 담겨 있는 모든 레코드를 꺼내달라
    # order_by() -> 정렬, -pk -> pk에 대해서 역순 정렬
    return render(request, 'blog/index.html', {  # 중괄호로 묶에서 보낼 수 있음
        'posts': posts  # context로 넘겨줌
    })


def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)

    return render(
        request,
        'blog/single_post_page.html', {
            'post': post
        }
    )
