from django.contrib import admin

# Register your models here.
from .models import Paragraph ,Paper,Translated_Paragraph,Contact_Us

class PaperAdmin(admin.ModelAdmin):
    class Meta:
        model= Paper

admin.site.register(Paper,PaperAdmin)


class ParagraphAdmin(admin.ModelAdmin):
    class Meta:
        model= Paragraph

admin.site.register(Paragraph,ParagraphAdmin)



class TranslatedAdmin(admin.ModelAdmin):
    class Meta:
        model= Translated_Paragraph

admin.site.register(Translated_Paragraph,TranslatedAdmin)

class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model= Contact_Us

admin.site.register(Contact_Us,ContactAdmin)