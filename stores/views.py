'''
El import order in a Django project is:
1 Standard library imports.
2 Imports from core Django.
3 Imports from third-party apps including those unrelated to Django.
4 Imports from the apps that you created as part of your Django project
'''
# Imports from core Django.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView


from .models import Store

# Create your views here.

class StoreList(ListView):

    model= Store
    template_name = 'store_list.html'
    context_object_name = 'stores'
    paginate_by = 1


class DetailsStore(DetailView):

    model = Store
    template_name = 'stores/store_details.html'
    context_object_name  = 'details' #
    slug_field = 'name_store' #



# Example view.
def index(request):
    return render(request,'stores/index.html')

def stores(request):
    return HttpResponse('aqui una lista de tiendas')