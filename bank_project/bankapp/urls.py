
from django.urls import path
from .import views

urlpatterns = [

    path('',views.index, name='index'),
    path('login/',views.loginn, name='login'),
    path('register/',views.register, name='register'),
    path('submit/',views.save_appform, name='submit'),
    path('form/', views.appform, name='form_page'),


    path('ajax/load-cities/', views.load_branches, name='ajax_load_branches'), # AJAX

]