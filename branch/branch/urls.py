from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
import api_server.urls
import frontend.urls
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    serializer_class = UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('frontend.urls', 'frontend'), namespace='frontend')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(api_server.urls)),
    path('openapi', get_schema_view(
        title="Clothing Store Chain",
        description="API for all different services availble",
        version="1.0.0"
    ), name='openapi-schema'),

]
