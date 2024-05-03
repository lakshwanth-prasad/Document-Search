from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URL Patterns to go the specified page for specified operations
urlpatterns = [
    path('', views.upload_and_index, name='upload'),
    path('search/home', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('view_document/<int:doc_id>/<str:term>/', views.view_document, name='view_document'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
