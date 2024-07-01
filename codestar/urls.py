from django.contrib import admin
from django.urls import path
from blog.views import my_blog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", my_blog, name="blog"),
]

urlpatterns += staticfiles_urlpatterns()