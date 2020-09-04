from django.shortcuts import render

def index(request):
    return render(request, 'bookselection/index.html')
