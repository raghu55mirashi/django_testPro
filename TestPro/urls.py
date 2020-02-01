from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('News.urls')),
    path('', include('Blog.urls')),
    path('', include('api.urls')),
    path('register/', include('accounts.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

