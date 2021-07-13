from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def coloringPage(request):
    return render(request, 'coloring/coloringPage.html')

def welcomepage(request):
    return render(request, 'coloring/welcomepage.html')

def home(request):
    return render(request, 'coloring/home.html')

def cattemplate(request):
    return render(request, 'coloring/cattemplate.html')

def saved(request):
    return render(request, 'coloring/saved.html')

def settings(request):
    return render(request, 'coloring/settings.html')

def catdrawing(request):
    return render(request, 'coloring/catdrawing.html')