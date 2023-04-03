# from modeltranslation.translator import translator, TranslationOptions
# from core.models import Blogs

# class BlogsTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')

# translator.register(Blogs, BlogsTranslationOptions)


from modeltranslation.translator import translator, TranslationOptions
from core.models import Blogs , Doctors

class BlogsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',) # add more fields that you want to translate

translator.register(Blogs, BlogsTranslationOptions)

class DoctorsTranslationOptions(TranslationOptions):
    fields = ('educational_history',) # add more fields that you want to translate

translator.register(Doctors, DoctorsTranslationOptions)

