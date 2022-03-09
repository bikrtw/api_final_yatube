from django.conf.urls import url
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='post-comments')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='v1',
        description="Документация для приложения posts проекта Yatube",
        # terms_of_service="URL страницы с пользовательским соглашением",
        contact=openapi.Contact(email="test@test.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^v1/swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^v1/swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^v1/redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
