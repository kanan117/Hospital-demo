from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .utils import slugify_KNN
from django.db.models.signals import pre_save
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext as _

from django.db import models


class BlogImage(models.Model):
    blog = models.ForeignKey("Blogs", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blogs')

    class Meta:
        verbose_name = 'Blog Image'
        verbose_name_plural = 'Blog Images'

    def __str__(self):
        return self.blog.title + ' Image'
    
    def __str__(self):
         return f"{self.blog.title} - {self.image.name}"
    
class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Setting(Basemodel):
    number1 = PhoneNumberField(max_length=20, blank=False)
    number2 = PhoneNumberField(max_length=20, blank=False)
    e_mail = models.EmailField()
    facebook = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    linkedin = models.URLField(max_length=100)
    logo = models.ImageField(upload_to="logo")
    creator = models.CharField(max_length=20)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    session = models.CharField(max_length=1000)

    def __str__(self):
        return "Setting"

    class Meta:
        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")

class News(Basemodel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

class Category(Basemodel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Category")

class Comment(Basemodel):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.news} haberi için {self.author} tarafından yapılan yorum"

    class Meta:
        verbose_name_plural = _("Comment")

class Tag(Basemodel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Tag")

class NewsTag(Basemodel):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.news} haberi için {self.tag} etiketi"

    class Meta:
        verbose_name_plural = _("NewsTag")
class Page(Basemodel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")


class Story(Basemodel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="stories")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=10000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_KNN(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.slug)])

class Contact(Basemodel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class Positions(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Positions")


class Doctors(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    email = models.EmailField()
    slug = models.SlugField(unique=True, blank=True)
    number = models.CharField(max_length=15)
    facebook = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    experience = models.CharField(max_length=2)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='Doctors')
    educational_History = models.CharField(max_length=100, null=True, default="N/A")
    positions = models.ForeignKey(Positions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_KNN(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('doctor_detail', args=[str(self.slug)])

    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")


