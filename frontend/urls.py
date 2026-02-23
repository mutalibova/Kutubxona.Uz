from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('home/', views.home, name='home'),
    path('book_list/', views.book_list, name='book_list'),
    path('kirish/', views.kirish, name='kirish'),
    path('sahifam/', views.sahifam, name='sahifam'),
    path('nav/', views.nav, name='nav'),
    path('mutolaa/', views.mutolaa, name='mutolaa'),
    path('market/', views.market, name='market'),
    path('davra/', views.davra, name='davra'),
    path('kitob/<int:id>/', views.kitob_detail, name='kitob'),
    path('pdf/<int:id>/', views.pdf_view, name='pdf'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
