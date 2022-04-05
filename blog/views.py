from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post

def blog(request):
  posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
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



