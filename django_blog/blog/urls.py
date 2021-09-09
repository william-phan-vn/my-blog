from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='blog_home'),
    path('<int:blog_id>/', views.blog_details, name='detail'),
]
