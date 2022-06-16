from django.urls import path,re_path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('upload/project/', views.upload_project, name='add_project'),
    path('',views.welcome,name='welcome'),
    path('review/<project_title>', views.rate_project, name='rate'),
    re_path(r'^search/', views.search_project,name='search_results'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    # path('account/', include('django.contrib.auth.urls')),
    path('api/project/', views.ProjectList.as_view(),name=''),
    path('api/profile/', views.ProfileList.as_view(),name=''),
    




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)