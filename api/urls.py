from django.urls import path

from api.views import user_list

app_name = "api"


urlpatterns = [
    path('users', user_list, name="user_list")
]
