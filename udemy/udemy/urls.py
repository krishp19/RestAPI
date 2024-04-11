from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from user import router as user_api_router
from house import router as house_api_router


auth_api_urls = [
    path('',include('drf_social_oauth2.urls'))
]

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/',include('rest_framework.urls')))

api_url_patterns = [
    path(r'auth/',include(auth_api_urls)),
    path(r'accounts/',include(user_api_router.router.urls)),
    path(r'house/',include(house_api_router.router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(api_url_patterns))
]
