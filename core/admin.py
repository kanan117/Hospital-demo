from django.contrib import admin
from core.models import Setting, Doctors, Positions, News, Category, Comment, Tag, NewsTag, Page, Story, Blogs, Contact
from modeltranslation.admin import TranslationAdmin


# Register your models here.

admin.site.site_header = 'Doctor Admin'

admin.site.register(Setting)
admin.site.register(Category)
admin.site.register(Positions)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(NewsTag)
admin.site.register(Page)
admin.site.register(Story)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    # fields = ['title', 'image', 'content']
    # readonly_fields = ['content', 'updated_at']



@admin.register(Blogs)
class BlogAdmin(TranslationAdmin):
    list_display = ('title', 'is_published')
    list_editable = ('is_published', )
    fields = ['title','image', 'description', 'category', 'author', 'is_published']

    # # define inline for BlogImage
    # class BlogImageInline(admin.TabularInline):
    #     model = BlogImage

    # inlines = [BlogImageInline]



@admin.register(Doctors)
class DoctorAdmin(TranslationAdmin):
    fields = [
        'name', 'age', 'email', 'number', 'facebook', 'instagram', 'twitter',
        'experience', 'is_published', 'image', 'educational_history', 'positions'
    ]
    list_display = (
        'name', 'age', 'number', 'is_published', 'email', 'positions'
    )
    list_editable = ('is_published',)
