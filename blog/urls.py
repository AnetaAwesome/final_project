from django.urls import path, include
from django.views.generic import DetailView, RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import models

urlpatterns = [
    path('main_page/', views.BlogPostList.as_view(), name='main_page'),
    path('create/blog_post/', views.BlogPostCreate.as_view(), name='blogpost_create'),
    path('blog_post/<int:pk>/', DetailView.as_view(model=models.BlogPost, template_name='blog/blogpost_detail.html'),
         name='blogpost_detail'),
    path('update/blog_post/<int:pk>/', views.BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('delete/blog_post/<int:pk>/', views.BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path("contact/", views.contact_form, name='contact'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
    path('blog_post/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment_create'),
    path('about_me/', views.AboutMe.as_view(), name='about_me'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
