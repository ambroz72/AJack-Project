from django.urls import path,include
from AjaxApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_data/',views.add_data,name='add_data'),
    path('delete_data/',views.delete_data,name='delete_data'),
    path('edit_data/',views.edit_data,name='edit_data'),
]