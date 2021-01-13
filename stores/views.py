'''
El import order in a Django project is:
1 Standard library imports.
2 Imports from core Django.
3 Imports from third-party apps including those unrelated to Django.
4 Imports from the apps that you created as part of your Django project
'''
# Imports from core Django.
from django.shortcuts import render

# Create your views here.

# Example view.
def index(request):
    return render(request,'stores/index.html')