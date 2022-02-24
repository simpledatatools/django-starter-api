from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [

    # API
    path('api/users/', include('api.urls.user_urls')),
    
    # Web App
    path('', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Microfinance Admin Panel"
admin.site.site_title = "Microfinance Admin Panel"
admin.site.index_title = ""
