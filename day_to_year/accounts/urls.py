from django.urls import path, include
from .views import *
from django.conf.urls import url


urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', register_view, name="signup"),
    path('myaccount/', myaccount, name = "myaccount"),
    path('profile/<str:user_id>', profile, name = "profile"),
    path('mypost/', mypost, name = "mypost"),
    path('mylike/', mylike, name = "mylike"),
    path('myinfo/', myinfo, name = "myinfo"),
    path('myinfo_update/', myinfo_update, name = "myinfoupdate"),
    path('change_password',change_password, name="change_password" ),
    path('profile_update/', profile_update, name = "profileupdate"),
]
