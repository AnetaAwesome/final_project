from django import forms
from .models import BlogPost, Contact

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

    first_name = forms.CharField(widget=forms.TextInput, label="Imię"),
    last_name = forms.CharField(label="Nazwisko", widget=forms.TextInput(attrs={'placeholder': "Nazwisko"})),
    email_field = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder': "E-mail"})),
    note = forms.CharField(widget=forms.Textarea, label="Tresć Wiadomość")

    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email_field", "note")
