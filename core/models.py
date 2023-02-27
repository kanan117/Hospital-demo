from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Basemodel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

# class Setting(Basemodel):
#     number1= models.IntegerField()
#     number2=models.IntegerField()
#     e_mail=models.EmailField()
#     fb=models.URLField(max_length=100)
#     ig=models.URLField(max_length=100)
#     tw=models.URLField(max_length=100)
#     logo=models.ImageField(upload_to="logo")

# class News(Basemodel):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='news_images', blank=True, null=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

# class Category(Basemodel):
#     name = models.CharField(max_length=100)

# class Comment(Basemodel):
#     text = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')

# class Tag(Basemodel):
#     name = models.CharField(max_length=50)

# class NewsTag(Basemodel):
#     news = models.ForeignKey(News, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

# class Page(Basemodel):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     slug = models.SlugField(max_length=100, unique=True)

class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Setting(Basemodel):
    number1= models.IntegerField()
    number2 = models.IntegerField()
    e_mail = models.EmailField()
    fb = models.URLField(max_length=100)
    ig = models.URLField(max_length=100)
    tw = models.URLField(max_length=100)
    logo = models.ImageField(upload_to="logo")

    def __str__(self):
        return f"Setting #{self.id}"

class News(Basemodel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(Basemodel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(Basemodel):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.author} on {self.news}"

class Tag(Basemodel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class NewsTag(Basemodel):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tag} in {self.news}"

class Page(Basemodel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title