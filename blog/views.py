from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    post.counted_view += 1
    post.save()
    prev_post = None
    next_post = None
    try:
        next_post = posts.filter(id__gt=post.id).order_by("id")[0:1].get()
    except Post.DoesNotExist:
        # Post.objects.aggregate(Min("id"))['id__min']
        pass
    try:
        prev_post = posts.filter(id__lt=post.id).order_by("-id")[0:1].get()
    except Post.DoesNotExist:
        # Post.objects.aggregate(Max("id"))['id__max']
        pass
    context = {'post': post, 'prev_post': prev_post, 'next_post': next_post}
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1).filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if s:= request.GET.get('s'):
        posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
