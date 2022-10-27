from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),   # 클래스형 Vue
    path('api2/', include('api2.urls')), # DRF 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)