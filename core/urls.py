from django.urls import path
from .views import ItemListView

app_name = 'core'

urlpatterns = [
    path('',ItemListView.as_view(), name='index_view')
]