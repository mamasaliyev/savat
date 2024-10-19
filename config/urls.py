# urls.py (proyekt)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('register.urls')),
    path('api_n/', include('news.urls')),
    path('api_s/', include('savatcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
