from django.contrib import admin

from core.models import Setting, News, Category, Comment, Tag, NewsTag, Page, Story, Blogs, Contact


# Register your models here.
admin.site.site_header = 'Doctor Admin'

admin.site.register(Setting)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(NewsTag)
admin.site.register(Page)
admin.site.register(Story)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = [
        'name',
    ]

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = [
        'title',
    ]

@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_editable = ('is_published', )
