from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name = 'star-home'),
    url(r'profile/', views.profile, name='star-profile'),
    url(r'post_project/', views.post_project, name = 'star-post-project'),
    url(r'search/', views.search_results, name='star-search'),
    url(r'project/(\d+)/$', views.project_by_id, name='star-project'),
    url(r'accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name = 'login'),
    url(r'accounts/logout/', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name = 'logout'),
    url(r'accounts/register/', views.register_view, name = 'star-register'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)