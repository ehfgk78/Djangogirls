from django.shortcuts import render

# Create your views here.
from blog.models import Post


def post_list(request):
    # post_list view 가 published_date 이 존재하는 Post 목록만 보여주도록 수정
    # posts = Post.objects.filter(published_date__isnull=False)
    posts = Post.objects.all()
    context = {
        # posts key의 value 는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request):
    # post_detail기능을 구현하는 함수 구현
    # 'post'라는 key로 Post.objects.first()에 해당하는 Post객체를 전달
    # 템플릿은 'blog/post_detail.html'이용
    # Post 인스턴스 1개만 가져옴, 변수명은 posts가 아닌 단일 객체를 나타내는 post를 사용
    post = Post.objects.first()
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

    # 실제 템플릿 생성
    # 'post'라는 변수를 이용해 Post 객체의 내용을 출력

    # UrlResolver(urls.py)
    # /post/detail/ --> url을 'post_detail'뷰와 연결
