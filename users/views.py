from django.shortcuts import render

# Create your views here.
def users_login(request):
    return render(request, "users/user_login.html")