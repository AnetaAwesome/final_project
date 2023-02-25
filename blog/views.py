from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from .models import BlogPost, Contact
from .forms import BlogPostForm, ContactForm
from blog import forms

class BlogPostView(TemplateView):
    template_name = 'blog/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogPostCreate(CreateView):
    ''' Creates new post view '''
    model = BlogPost
    # form_class = BlogPostForm
    fields = '__all__'
    template_name = 'blog/create_post_view.html'

    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk': self.object.pk})


# class ContactFormView(CreateView):
#     ''' Defines contact form'''
#     # model = Contact
#     form_class = ContactForm
#     # fields = '__all__'
#     template_name = 'blog/contact_form.html'
#
#     def get_success_url(self):
#         return reverse('thank_you')

def contact_form(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            contact_data = Contact(first_name=form.cleaned_data['first_name'],
                                    last_name=form.cleaned_data['last_name'],
                                    email_field=form.cleaned_data['email_field'],
                                   note=form.cleaned_data['note'])
            contact_data.save()
            return redirect('thank_you')

    else:
        form = forms.ContactForm()
    return render(request, 'blog/contact_form.html', {'form': form})


def thank_you_view(request):
    return render(request, 'blog/thank_you.html')