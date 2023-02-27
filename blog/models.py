from django.db import models
from django.forms import ModelForm

class BlogPost(models.Model):
    """  Simple class defining post on blog  """

    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Wpis"
        verbose_name_plural = "Wpisy"

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Contact(models.Model):
    """  Pass arguments to Contact form """

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_field = models.EmailField(max_length=254)
    note = models.TextField()

    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakty"

