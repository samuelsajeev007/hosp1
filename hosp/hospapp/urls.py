from django.urls import path
from .import views
urlpatterns = [
   
    path('',views.index,name='in'),
    path('book',views.booking,name='bo'),
    path('cont',views.contact,name='co'),
    path('doct',views.docters,name='do'),
    path('abou',views.about,name='ab'),
    path('dept',views.department,name='de'),
]