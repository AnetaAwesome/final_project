from django.urls import path
from django.views.generic import DetailView
from . import views
from . import models

urlpatterns = [
    path('main_page/', views.BlogPostView.as_view()),
    path('create/blog_post/', views.BlogPostCreate.as_view()),
    path('blog_post/<int:pk>/', DetailView.as_view(model=models.BlogPost, template_name='blog/blogpost_detail.html'),
         name='blogpost_detail'),
    path("contact/", views.ContactFormView.as_view()),
    path("thank_you/", views.SuccessView.as_view(), name='thank_you'),
]