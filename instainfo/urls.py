from django.contrib import admin
from django.urls import path, include
from instainfo.api import views

urlpatterns = [
    path('get_followers/<str:username>',views.Followers.as_view()),
    path('get_followings/<str:username>', views.Following.as_view()),
    path('get_bio/<str:username>', views.Bio.as_view()),
    path('get_profile_url/<str:username>', views.ProfilePic.as_view()),
    path('get_all_information/<str:username>', views.GetAllInformation.as_view()),

]
