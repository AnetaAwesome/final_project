from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, FormView
from .models import BlogPost, Contact
from .forms import ContactForm

class BlogPostView(TemplateView):
    template_name = 'blog/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class BlogPostCreate(CreateView):
    ''' '''
    model = BlogPost
    fields = '__all__'
    template_name = 'blog/create_post_view.html'

    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk': self.object.pk})


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'blog/contact_form.html'
    success_url = '/thank_you/'

class SuccessView(TemplateView):
    template_name = 'thank_you.html'
