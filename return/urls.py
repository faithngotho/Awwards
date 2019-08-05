from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.home,name='home'),
    url(r'register',views.register,name= 'signup'),
    url(r'^search/', views.search_project, name='search'),
    url(r'^newproject',views.add_project, name = "addproject"),
    url(r'profile',views.profile,name= 'profile'),
    url(r'update-user',views.user_update,name= 'user-up'),
    url(r'details',views.myprofile,name= 'details'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
