
import unittest
from app.models import Comment,User,Blog
from app import db

class BlogTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'Kevinm', password = '1234', email = 'kevinmurimi@gmail.com')
        self.new_blog = Blog(id = 111, blog_title = 'Music', blog_content = 'Music is life')

    def tearDown(self):
        User.query.delete()
        Blog.query.delete()
        Comment.query.delete()

    def test_check_instance(self):
        # self.assertEquals(self.new_blog.blog_id,'111')
        self.assertEquals(self.new_blog.blog_title,'Music')
        self.assertEquals(self.new_blog.blog_content,'Music is life')
       

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        blog = Blog.get_blog(111)
        self.assertTrue(blog is not None)
