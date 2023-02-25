from django import forms


class BlogPostForm(forms.Form):
    required_css_class = 'required'

    title = forms.CharField(max_length=30, label="Tytuł",
                            widget=forms.TextInput(attrs={'placeholder': "Tytuł posta"}))
    content = forms.CharField(widget=forms.Textarea, label="Treść")


class ContactForm(forms.Form):
    required_css_class = 'required'

    first_name = forms.CharField(max_length=30, label="Imię",
                                 widget=forms.TextInput(attrs={'placeholder': "Imię"})),
    last_name = forms.CharField(max_length=30, label="Nazwisko",
                                widget=forms.TextInput(attrs={'placeholder': "Nazwisko"})),
    email_field = forms.EmailField(max_length=254, label="e-mail",
                                   widget=forms.TextInput(attrs={'placeholder': "e-mail"})),
    note = forms.CharField(widget=forms.Textarea, label="Treść wiadomości")
