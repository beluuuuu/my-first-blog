from django.conf.urls import include, url
from django.contrib import admin
from blog import views
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]
