from django.contrib import admin
from main import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('accounts/', include('accounts.urls')),
    path('rental/', include('rental.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




