from django.urls import path, include

from app.views import *
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('', PortfoliyomViews.as_view(), name='portfolio'),
    path('', index, name='index'),
    path('about/',views.AboutViews.as_view(),name='about'),
    path('team/',views.TeamViews.as_view(),name='Team'),
    path('service/',views.ServiceViews.as_view(),name='Service'),
    path('blog/',views.BlogViews.as_view(),name='bolog'),
    path('contact/',views.ContactViews.as_view(),name='contact')


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)