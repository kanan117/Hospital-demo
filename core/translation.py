from modeltranslation.translator import register, TranslationOptions

from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.translator import TranslationOptions, translator
from .models import Setting, Doctors, Positions, News, Category, Comment, Tag, NewsTag, Page, Story, Blogs, Contact, BlogImage

# class SettingTranslationOptions(TranslationOptions):
#     fields = ('number1','number2','creator','address1','address2')
# translator.register(Setting, SettingTranslationOptions)

# class DoctorsTranslationOptions(TranslationOptions):
#     fields = ('name', 'description', 'position')
# translator.register(Doctors, DoctorsTranslationOptions)

# class PositionsTranslationOptions(TranslationOptions):
#     fields = ('title',)
# translator.register(Positions, PositionsTranslationOptions)

class NewsTranslationOptions(TranslationOptions):
    fields = ('title','content','pub_date','image','author','category')
translator.register(News, NewsTranslationOptions)

# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')
# translator.register(Category, CategoryTranslationOptions)

# class CommentTranslationOptions(TranslationOptions):
#     fields = ('name', 'email', 'text')
# translator.register(Comment, CommentTranslationOptions)

# class TagTranslationOptions(TranslationOptions):
#     fields = ('title',)
# translator.register(Tag, TagTranslationOptions)

# class NewsTagTranslationOptions(TranslationOptions):
#     fields = ('news', 'tag')
# translator.register(NewsTag, NewsTagTranslationOptions)

# class PageTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')
# translator.register(Page, PageTranslationOptions)

# class StoryTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')
# translator.register(Story, StoryTranslationOptions)

# class BlogsTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')
# translator.register(Blogs, BlogsTranslationOptions)

# class ContactTranslationOptions(TranslationOptions):
#     fields = ('name', 'email', 'subject', 'message')
# translator.register(Contact, ContactTranslationOptions)

# class BlogImageTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')
# translator.register(BlogImage, BlogImageTranslationOptions)
