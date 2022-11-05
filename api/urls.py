from django.urls import path
from . import views

urlpatterns = [
    path('app', views.AppViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'delete'})),
    path('app/<slug:id>', views.AppViewSet.as_view({'get': 'get', 'post': 'edit'})),
    path('app/history', views.AppViewSet.as_view({'get': 'actionsHistory'})),
    path('app/<slug:id>/run', views.AppViewSet.as_view({'get': 'run'})),
]