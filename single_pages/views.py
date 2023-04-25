from django.shortcuts import render

from blog.models import Post


def main(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/main.html',
                  {
                      'recent_posts': recent_posts,
                  })
    # 정적 렌더링, templates 폴더를 합칠 수 있기 때문에 디렉터리를 하나 더 만듬
