from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="instagram API",
      default_version='v1',
      description="Instagram api for pgu university software engineering course",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="3inaroydl@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('admin/', admin.site.urls),
    path('getInformation/',include('instainfo.urls')),

]
