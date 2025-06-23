from django.contrib import admin
from django.urls import include, path
from vege.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
        path('',include('student.urls')),
    path("polls/", include("polls.urls")),
    path("receipes/",receipes,name='receipes'),
    path("login/",login_page,name='login'),
    path("register/",register_page,name='register'),
    path("delete_receipe/<id>",delete_receipe,name='delete_receipe'),
    path("update_receipe/<id>",update_receipe,name='update_receipe'),
    path("admin/", admin.site.urls),
    path("logout/", logout_page,name="logout"),
    path('profile/', user_details, name='user_details'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

