from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    url('', include('starapp.urls')),
    url('admin/', admin.site.urls),
    url('tinymce/', include('tinymce.urls')),
]
