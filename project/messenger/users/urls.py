from django.urls import path
from users.views import UserAPIList

urlpatterns = [
    path('user/<int:user_id>/', UserAPIList.as_view())#, get_user, name='get_user')
]
