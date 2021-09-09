from django.shortcuts import render, get_object_or_404

from blog.models import Blog


def all_blogs(request):
    blogs = Blog.objects.all().order_by('-date')[:2]
    context = {'blogs': blogs}
    return render(request, 'blog/blog_home.html', context)


def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/detail.html', context)
