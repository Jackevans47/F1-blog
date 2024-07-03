from django.contrib import admin
from django.urls import path, include

# from blog.views import blog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("blog/", blog, name="blog"),
    path("", include("blog.urls")),
]
urlpatterns += staticfiles_urlpatterns()
