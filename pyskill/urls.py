from django.urls import path

from pyskill.apps import PyskillConfig
from pyskill.views import base

app_name = PyskillConfig.name

urlpatterns = [
    path('', base, name='base'),
   ]