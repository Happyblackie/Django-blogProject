from django.shortcuts import render,redirect

from .models import Article1

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .import forms
# Create your views here.

def articles_list(request):
    #you can decide not to order them: articlesVariable = Article1.objects.all()
    #a variable: articlesVariable 

    articlesVariable = Article1.objects.all().order_by('date')
    return render(request,'articlesAppFolder/articles_list.html',{'articles':articlesVariable})


def article_details(request,slug):
    articleVariable = Article1.objects.get(slug=slug)
    return render(request,'articlesAppFolder/article_details.html',{'article':articleVariable})
    #return HttpResponse(slug)


@login_required(login_url='/accounts/login') #decorator->protects the create page for this case
def article_Create(request):
    if request.method == 'POST':
        formVariable = forms.CreateArticle(request.POST,request.FILES) #->' request done along on FILES object for the media'
        if formVariable.is_valid():
            #save to database
            instanceVariable = formVariable.save(commit=False) #instance of the form
            instanceVariable.author = request.user #attach the author to the user
            instanceVariable.save()  #save
            return redirect('articles:list')
    else:
     formVariable = forms.CreateArticle()
    return render(request,'articlesAppFolder/article_create.html',{'anyname':formVariable})