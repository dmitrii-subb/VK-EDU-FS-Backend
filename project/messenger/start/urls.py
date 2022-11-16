from django.urls import path
from start.views import home
from start.views import login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='index'),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
