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

# Create your views here.
