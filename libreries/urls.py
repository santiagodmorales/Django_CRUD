from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('documents', views.documents, name='documents'),
    path('documents/create', views.create, name='create'),
    path('documents/edit/<int:id>', views.edit, name='edit'),
    path('documents/delete/<int:id>', views.delete, name='delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
