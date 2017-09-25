from django.shortcuts import render


# Create your views here.
from blog.models import Post


def post_list(request):
    # post_list view 가 published_date 이 존재하는 Post 목록만 보여주도록 수정
    posts = Post.objects.filter(publisted_date__isnull=False)
    context = {
        # posts key의 value 는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
