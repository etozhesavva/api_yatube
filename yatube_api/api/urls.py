from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='worstapi')


urlpatterns = [
    path('api/v1/', include(router.urls), name='worstapi-list'),
    path('api/v1/api-token-auth/', views.obtain_auth_token,
         name='worstapi-detail'),
]
