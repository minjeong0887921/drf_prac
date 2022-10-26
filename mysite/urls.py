from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('', include(router.urls)),
    path('api2/', include('api2.urls')),
]