from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error_message':'invalid login'})
    else:

        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        password_repeat = request.POST.get('psw-repeat')

        # Check if passwords match
        if password != password_repeat:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect('/')
    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')