from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name='indexPage'),
    path('signup/', views.sign, name='signUp')
]