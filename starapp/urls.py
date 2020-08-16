from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name = 'gram-home'),
    url(r'profile/', views.profile, name='star-profile'),
    url(r'post_project/', views.post_project, name = 'star-post-project'),
    url(r'search/', views.search_results, name='star-search'),
    url(r'project/(\d+)/$', views.project_by_id, name='start-project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)