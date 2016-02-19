from django.shortcuts import render, get_object_or_404
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    posted = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                               publish__day=day)
