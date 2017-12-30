# django-relational-models
Here we can see how one to many and many to many relationships can work . 
Here Django's One to Many and Many To One using foreign key has been coded . 
Forward and Reverse/Backward Relations can be easiliy understood by the code .
Also ManyToMany relationships in terms of Forward and Backward approach is also included into to code . 

##In the blog.models (app name is :blog):

Add This Code:

from django.db import models


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    

    def __str__(self):              # __unicode__ on Python 2
        return self.headline

    class Meta:
        ordering = ('headline',)
        
        
        
class Book(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Paragraph(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        
  #Here A reporter can have multiple articles (OneToMany aka Backward/Reverse Relation) 
  #but an artical can only have a single reporter(OneToOne aka Forward Relation)
  
  #Also A book can contains a lot of paragraphs and also many paragrapsh also can be in the same book 
  #or different books (preface can be found on any book) So this type of relation is 
  #called ManyToMany relation . Both forward and backward approaches are coded . 
  #Showing a book containing paragraphs is ManyToMany Backward/Reverse Relation
  #Showing a paragraph and its related books is ManyToMany Forward Relation
  
  
##In blog.views.py:
  from django.shortcuts import render

from .models import Article,Reporter,Paragraph,Book

def Index(request):
    a = Article.objects.all()
    b = Reporter.objects.all()
    c = Book.objects.all()
    d = Paragraph.objects.all()
    
    context  = {
        'article' : a,
        'reporter' : b,
        'book' : c,
        'paragraph' : d,
    }
    return render(request,'test.html',context)
    
 ##In blog.urls.py (create a urls.py file inside app directory) 
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$',views.Index,name='index'),
]

##in urls.py (project directory | main urls.py)
from django.conf.urls import url,include
from django.views.generic import TemplateView

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
]
##In templates/test.html

See the code in the test.html file 

  
  

