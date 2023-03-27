from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Basemodel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Setting(Basemodel):
  number1 = PhoneNumberField(max_length=20,blank=False)
  number2 = PhoneNumberField(max_length=20,blank=False)
  e_mail = models.EmailField()
  facebook = models.URLField(max_length=100)
  instagram = models.URLField(max_length=100)
  twitter = models.URLField(max_length=100)
  linkedin = models.URLField(max_length=100)
  logo = models.ImageField(upload_to="media/logo")
  creator = models.CharField(max_length=20)
  address1 = models.CharField(max_length=20)
  address2 = models.CharField(max_length=20)
  session = models.CharField(max_length=1000)
  
  def __str__(self):
    return "Setting"

  class Meta:
    verbose_name = "Setting"
    verbose_name_plural = "Setting"


class News(Basemodel):
  title = models.CharField(max_length=200)
  content = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='media/news_images',
                            blank=True,
                            null=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
  category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)

  def __str__(self):
    return self.title
  class Meta:
    verbose_name = "News"
    verbose_name_plural = "News"

class Category(Basemodel):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = "Category"


class Comment(Basemodel):
  text = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
  news = models.ForeignKey(News,
                           on_delete=models.CASCADE,
                           related_name='comments')

  def __str__(self):
    return f"Comment by {self.author} on {self.news}"

  class Meta:
    verbose_name_plural = "Comment"


class Tag(Basemodel):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = "Tag"


class NewsTag(Basemodel):
  news = models.ForeignKey(News, on_delete=models.CASCADE)
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.tag} in {self.news}"

  class Meta:
    verbose_name_plural = "New Tag"


class Page(Basemodel):
  title = models.CharField(max_length=200)
  content = models.TextField()
  slug = models.SlugField(max_length=100, unique=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name_plural = "Page"


class Story(Basemodel):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to="media/stories")
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name_plural = "Story"


class Blogs(Basemodel):
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to='media/Blogs')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  is_published = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return self.id

  class Meta:
    verbose_name_plural = "Blogs"


class Contact(Basemodel):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  phone_number = models.CharField(max_length=100)
  message = models.TextField()
  

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = "Contact"


# from django.db import models

# class Subscriber(models.Model):
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.email
    
#     class Meta:
#       verbose_name_plural = "Subscriber"

# from django.db import models


# class SubscribeModel(models.Model):
#     sys_id = models.AutoField(primary_key=True, null=False, blank=True)
#     email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
#     status = models.CharField(max_length=64, null=False, blank=True)
#     created_date = models.DateTimeField(null=False, blank=True)
#     updated_date = models.DateTimeField(null=False, blank=True)

#     class Meta:
#         app_label = "appname"
#         db_table = "appname_subscribe"

#     def __str__(self):
#         return self.email


