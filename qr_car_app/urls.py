from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# update the urls after making other html
urlpatterns = [
    path("home.html", views.home, name='home'),
    path("send", views.home)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

