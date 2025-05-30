from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author='Author Name'
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post content.')
        self.assertEqual(self.post.author, 'Author Name')

class PostListViewTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author='Author Name'
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('post_list'))
        self.assertTemplateUsed(response, 'blog/post_list.html')

class PostDetailViewTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author='Author Name'
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertTemplateUsed(response, 'blog/post_detail.html')