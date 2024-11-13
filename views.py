from django.shortcuts import render, redirect


def register_view(request):
    if request 
    return render(request, 'register.html')


def login_view(request):
    return render(request, 'login.html')


def welcome_view(request):
    return render(request, 'welcome.html')


def publish_ride_view(request):
    return render(request, 'publish_ride.html')


def search_ride_view(request):
    return render(request, 'search_ride.html')


def book_ride_view(request):
    # No specific template is expected for this page
    return redirect('/welcome')
