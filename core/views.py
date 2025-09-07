from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Blog
from django.core.paginator import Paginator

def index(request):
    recent_blogs = Blog.objects.filter(is_published=True)[:6]
    context = {'recent_blogs': recent_blogs}
    return render(request, 'core/index.html', context)

def explore(request):
    blogs = Blog.objects.filter(is_published=True)
    paginator = Paginator(blogs, 12)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {'blogs': blogs}
    return render(request, 'core/explore.html', context)

def about(request):
    context = {}
    return render(request, 'core/about.html', context)

def search_blogs(request):
    query = request.GET.get('q', '')
    if query:
        blogs = Blog.objects.filter(
            Q(title__icontains=query) & Q(is_published=True)
        )[:10]
        results = [{
            'id': blog.id,
            'title': blog.title,
            'author': blog.author.username,
            'created_at': blog.created_at.strftime('%Y-%m-%d')
        } for blog in blogs]
        return JsonResponse({'results': results})
    return JsonResponse({'results': []})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, is_published=True)
    context = {'blog': blog}
    return render(request, 'core/blog_detail.html', context)

def latest_topics(request):
    topics = Blog.objects.filter(is_published=True)[:10]
    results = [{
        'id': topic.id,
        'title': topic.title,
        'created_at': topic.created_at.strftime('%Y-%m-%d %H:%M')
    } for topic in topics]
    return JsonResponse({'topics': results})