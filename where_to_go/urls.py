from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from where_to_go import views


urlpatterns = [
    path('', views.show_index),
    path('admin/', admin.site.urls),
    path('places/<int:place_id>/', views.show_place),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
