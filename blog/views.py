from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, ListView
from .models import BlogPost, Contact, Comment
from .forms import BlogPostForm, ContactForm, CommentForm
from blog import forms

class BlogPostView(TemplateView):
    template_name = 'blog/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogPostList(ListView):
    model = BlogPost
    template_name = 'blog/main_page.html'
    queryset = BlogPost.objects.order_by('-creation_date')


class BlogPostCreate(CreateView):
    ''' Creates new post view '''
    model = BlogPost
    form_class = BlogPostForm
    # fields = '__all__'
    template_name = 'blog/create_post_view.html'

    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = '__all__'
    template_name = 'blog/blogpost_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel'] = self.get_success_url()
        return context

    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('thank_you')
    template_name = 'blog/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel'] = reverse('blogpost_detail', kwargs={'pk': self.object.pk})
        return context

class CommentCreate(CreateView):
    ''' Creates new comment view '''
    model = Comment
    form_class = CommentForm
    # fields = '__all__'
    template_name = 'blog/add_comment.html'

    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     form.instance.blogpost_id = self.kwargs['pk']
    #     return super().form_valid(form)
    # success_url = reverse_lazy('blogpost_detail')


# class ContactFormView(FormView):
#     ''' Defines contact form'''
#     form_class = ContactForm
#     # model = Contact
#     # fields = '__all__'
#     template_name = 'blog/contact_form.html'
#     success_url = reverse_lazy('blog:thank-you')
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