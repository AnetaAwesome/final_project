from django.urls import path
from django.views.generic import DetailView, RedirectView
from . import views
from . import models

urlpatterns = [
    path('main_page/', views.BlogPostView.as_view()),
    path('create/blog_post/', views.BlogPostCreate.as_view()),
    path('blog_post/<int:pk>/', DetailView.as_view(model=models.BlogPost, template_name='blog/blogpost_detail.html'),
         name='blogpost_detail'),
    # path("contact/", views.ContactFormView.as_view()),
    # path("thank_you/", views.SuccessView.as_view(), name='thank_you'),
    # path("thank_you/", RedirectView.as_view(pattern_name='thank_you')),
    path("contact/", views.contact_form),
    path('thank_you/', views.thank_you_view, name='thank_you'),

]