from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate, login

# pass for navkirat is Nav@*000
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):

    if request.method == "POST":
        # check if user login with correct credentials 

        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            print('success')
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')