# from django.contrib import admin

# # Register your models here.

# from core.models import Setting

# admin.site.register(Setting)

from django.contrib import admin
from core.models import Setting, News, Category, Comment, Tag, NewsTag, Page

admin.site.register(Setting)

admin.site.register(News)

admin.site.register(Category)

admin.site.register(Comment)

admin.site.register(Tag)

admin.site.register(NewsTag)

admin.site.register(Page)