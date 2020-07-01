from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>', views.index, name='index'),
]