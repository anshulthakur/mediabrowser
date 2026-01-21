from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^images/$', views.image_list_view , name='mediabrowser-image-list'),
    re_path('^images/add/$', views.image_add_view, name='mediabrowser-add-image'),
    
    re_path('^documents/$', views.document_list_view, name='mediabrowser-document-list'),
    re_path('^documents/images/$', views.image_as_document_list_view, name='mediabrowser-image-document-list'),
    re_path('^documents/add/$', views.document_add_view, name='mediabrowser-add-document'),
    
    re_path('^delete/$', views.asset_delete_view, name='mediabrowser-delete'),
]
