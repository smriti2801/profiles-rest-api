from django.conf.urls import url, include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

"""we don't need to set a base name for above router bcoz its' a model viewset
so, django knows what to call it's objects"""

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),
]
