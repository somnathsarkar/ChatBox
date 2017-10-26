from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =  [
            url(r'^$',views.home, name='home'),
            url(r'^account/(?P<parameter>\w+)/', views.account, name='account'),
            url(r'^mssgs',views.mssgs, name = 'mssgs'),
            url(r'^addfriends/results',views.addfriendsresults, name = 'addfriendsresults'),
            url(r'^addfriends',views.addfriends, name = 'addfriends'),
            url(r'^searchfriends/results',views.searchfriendsresults, name = 'searchfriendsresults'),
            url(r'^searchfriends',views.searchfriends, name = 'searchfriends'),
            url(r'^login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
            url(r'^logout/',auth_views.logout, {'next_page': 'login'}, name='logout'),
            url(r'^signup/', views.signup, name='signup'),
 ]