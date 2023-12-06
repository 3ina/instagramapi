from django.shortcuts import render
from rest_framework.views import APIView
from instainfo.api.serializers import AccountSerializer
from instainfo.api.informationGathering import InstagramChecker
from django.shortcuts import HttpResponse
from django.http import JsonResponse
# Create your views here.

instachecker = InstagramChecker()
class Followers(APIView):
    def get(self, request,username, format=None):
        return JsonResponse(instachecker.getNumOfFollowers(username),safe=False)


class Following(APIView):
    def get(self, request,username, format=None):
        return JsonResponse(instachecker.getNumOfFollowing(username),safe=False)

class GetAllInformation(APIView):
    def get(self, request,username, format=None):
        return JsonResponse(instachecker.get_all_information(username),safe=False)

class Bio(APIView):
    def get(self, request,username, format=None):
        return JsonResponse(instachecker.get_bio(username),safe=False)


class ProfilePic(APIView):
    def get(self, request,username, format=None):
        return JsonResponse(instachecker.get_profile_url(username),safe=False)

