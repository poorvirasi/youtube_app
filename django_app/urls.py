from django.urls import path
from django_app import views
urlpatterns = [
    path('',views.home,name='home_page'),
    path('about/',views.about,name='app_about'),
]
