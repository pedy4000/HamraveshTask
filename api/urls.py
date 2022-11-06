from django.urls import path
from . import views

urlpatterns = [
    path('app', views.AppViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('app/history',
         views.AppViewSet.as_view({'get': 'container_history'})),
    path('app/<slug:id>', views.AppViewSet.as_view({'get': 'get', 'post': 'edit', 'delete': 'delete'})),
    path('app/<slug:id>/run', views.AppViewSet.as_view({'get': 'run'})),
]