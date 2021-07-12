from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo')

def new_interaction(request):
    return render(request, 'coloring/new_interaction')

def coloringPage(request):
    return render(request, 'coloring/coloringPage.html')