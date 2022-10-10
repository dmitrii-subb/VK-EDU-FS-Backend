from django.urls import path
from users.views import user


urlpatterns = [
    path('<int:user_id>/', user, name='user')
]
