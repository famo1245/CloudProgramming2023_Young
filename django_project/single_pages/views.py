from django.shortcuts import render


def main(request):
    return render(request,
                  'single_pages/main.html')  # 정적 렌더링, templates 폴더를 합칠 수 있기 때문에 디렉터리를 하나 더 만듬
