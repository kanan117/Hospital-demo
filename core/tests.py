from django.test import TestCase
from django.urls import reverse
from .models import Blogs


class BlogsTests(TestCase):

  def setUp(self):
    self.blog = Blogs.objects.create(
      title='Test Blog',
      author='Test Author',
      description='This is a test blog description')

  def test_blog_listing(self):
    response = self.client.get(reverse('blogs'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, self.blog.title)
    self.assertContains(response, self.blog.author)

  def test_blog_detail_view(self):
    response = self.client.get(reverse('blog_details', args=[self.blog.pk]))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, self.blog.title)
    self.assertContains(response, self.blog.author)
    self.assertContains(response, self.blog.description)
