from django.test import TestCase
from blog.models import BlogPost, Comment, Contact
from django.test import Client
from django.urls import reverse


class BlogTests(TestCase):

    def setUp(self):
        print("SET UP!")
        self.client = Client()

        first_post = BlogPost(title="First post", content="First post content")
        first_post.save()

        second_post = BlogPost(title="Second post", content="Second post content")
        second_post.save()

        comment = Comment(post=first_post, name="Joe", email="joe@gmail.com", body="comment body")
        comment.save()

        Contact(first_name="Michal", last_name="Nowotka", email_field="joe@gmail.com", note="contact me!").save()

    def tearDown(self) -> None:
        print("TEAR DOWN!")

    def test_post_exist(self):
        print("test_post_exist")
        self.assertEqual(BlogPost.objects.get(title="First post").content, "First post content")

    def test_comment_exist(self):
        print("test_comment_exist")
        self.assertEqual(Comment.objects.get(post="1").name, "Joe")

    def test_contact_exist(self):
        print("test_contact_exist")
        self.assertEqual(Contact.objects.get(last_name="Nowotka").last_name, "Nowotka")


    def test_main_page(self):
        print("test_main_page")
        response = self.client.get(reverse('main_page'))
        self.assertNumQueries(1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['blogpost_list']), 2)
        self.assertTemplateUsed(response, 'blog/main_page.html')

