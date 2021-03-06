# Standard library imports
''' 
examples:
from __future__ import absolute_import
from math import sqrt
from os.path import abspath
'''

# Core Django imports
from django.urls import path

# Related third-party imports
'''
example:
from django_extensions.db.models import TimeStampedModel
'''
 
# Local application or library speciŀc imports
# Import views from app stores.
from .views import index

# Namespacing URL names 
app_name = 'stores'

urlpatterns = [
    path('', index, name='index'),
]