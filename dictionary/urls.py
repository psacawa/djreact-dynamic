from django.urls import path
from . import views


urlpatterns = [
    path (r'', views.home),
    path (r'entries/', views.EntryList.as_view ()),
    path (r'entries/<int:pk>', views.EntryDetail.as_view ()),
]
