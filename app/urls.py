"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'https://eskill-test.netlify.app/'
    client_class = OAuth2Client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('dj_rest_auth.urls')),

    path('api/registration/', include('dj_rest_auth.registration.urls')),
    
    path('developer-docs/', get_schema_view(
        title="Moreplex Backend Documentations",
        description="API documentation for Frontend Developers"
    ), name='openapi-schema'),

    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    path('api/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('api/google/', GoogleLogin.as_view(), name='google_login'),
]
