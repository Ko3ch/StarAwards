from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from . models import Post,Profile,Rating

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='tomtom', password='tomtom')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='tomtom')
        self.post = Post.objects.create(id=1, title='test post', photo='https://cdn.pixabay.com/photo/2020/07/06/09/23/puppy-5376247__340.jpg', description='desc',
                                        user=self.user, url='http://test.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='tomtom')
        self.post = Post.objects.create(id=1, title='test post', photo='https://cdn.pixabay.com/photo/2020/07/06/09/23/puppy-5376247__340.jpg', description='desc',
                                        user=self.user, url='http://test.com')
        self.rate = Rating.objects.create(id=1, design=1, usability=1, content=1, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Rating))

    def test_save_rating(self):
        self.rate.save_rating()
        rate = Rating.objects.all()
        self.assertTrue(len(rate) > 0)

    def test_get_post_rating(self, id):
        self.rate.save()
        rate = Rating.get_ratings(post_id=id)
        self.assertTrue(len(rate) == 1)