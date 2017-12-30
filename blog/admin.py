from django.contrib import admin
from .models import Reporter,Article,Book,Paragraph

admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Book)
admin.site.register(Paragraph)
# Register your models here.
