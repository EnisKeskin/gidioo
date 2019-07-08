
from django.contrib import admin
from django.urls import path, include
from gidioo import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'entry', views.EntryViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'repeater', views.RepeaterViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'entry-tag', views.EntryTagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token)
]
