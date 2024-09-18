from django.urls import path
from .views import (register,
                    profile,
                    logout_view)


app_name = "users"

urlpatterns = [
    path('register/', register, name = "register"),
    path('logout/', logout_view, name = "logout"),
    path('profile/', profile, name = "profile"),
]
