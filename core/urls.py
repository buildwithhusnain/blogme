from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore, name='explore'),
    path('about/', views.about, name='about'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('api/search/', views.search_blogs, name='search_blogs'),
    path('api/latest-topics/', views.latest_topics, name='latest_topics'),
]
