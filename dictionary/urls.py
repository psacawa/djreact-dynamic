from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path (r'', views.home),
    path (r'entries/', views.EntryList.as_view ()),
    path (r'entries/<int:pk>/', views.EntryDetail.as_view ()),
    path (r'entries/complete/', views.EntryCompletions.as_view ()),
]
urlpatterns = format_suffix_patterns (urlpatterns)

