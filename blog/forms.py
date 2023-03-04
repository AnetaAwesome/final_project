from django import forms
from django.forms import widgets
from .models import BlogPost, Contact, Comment

class BlogPostForm(forms.ModelForm):
    required_css_class = 'required'
    title = forms.CharField(max_length=30, label="Tytuł",
                            widget=forms.TextInput(attrs={"placeholder": "Tytuł posta"}))
    content = forms.CharField(widget=forms.Textarea, label="Treść")
    class Meta:
        model = BlogPost
        fields = ("title", "content")


class ContactForm(forms.ModelForm):
    required_css_class = 'required'

    first_name = forms.CharField(label="Imię", widget=forms.TextInput(attrs={'placeholder': "Imię"}), )
    last_name = forms.CharField(label="Nazwisko", widget=forms.TextInput(attrs={'placeholder': "Nazwisko"}))
    email_field = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder': "E-mail"}))
    note = forms.CharField(widget=forms.Textarea, label="Wiadomość")

    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email_field", "note")

class CommentForm(forms.ModelForm):
    name = forms.CharField(label="Imię", widget=forms.TextInput)
    email = forms.EmailField(label="E-mail", widget=forms.TextInput)
    body = forms.CharField(label="Wpisz komentarz", widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ("name", "email", "body")

