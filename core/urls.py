from django.urls import path 

from .views import  IndexView ,SinglelView

app_name = "core"

urlpatterns = [
   
    path ('', IndexView.as_view() , name = 'index'),
    path ('<slug:slug>/', SinglelView.as_view() , name = 'singleview'),
]