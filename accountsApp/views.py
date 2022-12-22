from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.

def signup_view(request):
    if request.method == 'POST': #checks if the request i a post method

         #instance of the form
        formVariable = UserCreationForm(request.POST)

        #checks if the form is valid(correct passwords,if user exists etc)
        if formVariable.is_valid():

            #save to databse
            formVariable.save() 

            #come back log the user in later video 22

            #here 'articles = is the app_name space' found in urls.py(articlesApp ) and
            # 'list => is the name of the url path found in urls.py(articlesApp )
            return redirect('articles:list')
    else:
        #instance of the form
        formVariable = UserCreationForm()
    return render(request, 'accountsAppFolder/signup.html',{'anyname':formVariable})

def login_View(request):
    if request.method == 'POST':
        formVariable = AuthenticationForm(data=request.POST) #checks if user password etc is correct
        if formVariable.is_valid():
            #come back log the user in later video 22
            userVariable = formVariable.get_user()
            login(request,userVariable)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')

    else:
        formVariable = AuthenticationForm()
    return render(request,'accountsAppFolder/login.html',{'anyname':formVariable})


def logout_View(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')