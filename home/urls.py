from django.urls import path
from home.views.default import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', index, name='admin'),
]
