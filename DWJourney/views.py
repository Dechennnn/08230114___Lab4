from django.shortcuts import render

# Home page
def index(request):
    return render(request, 'index.html')

# About Me page
def about_me(request):
    return render(request, 'aboutme.html')
