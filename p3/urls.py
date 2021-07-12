from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coloring/', include('coloring.urls')),
]
def coloringPage(request):
    return render(request, 'coloring/templates/coloring/coloringPage.html')