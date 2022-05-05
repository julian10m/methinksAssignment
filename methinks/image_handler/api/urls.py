from django.urls import path
from . import views

app_name = 'imageHandler'

urlpatterns = [
    path('images/upload',
        views.ImageUploadView.as_view(),
        name='image_upload'),
    path('images/<pk>',
         views.ImageDetailView.as_view(),
         name='image_detail'),
    path('images/',
         views.ImageListView.as_view(),
         name='image_list'),
    path('comments/search/<int:pk>',
         views.CommentListView.as_view(),
         name='comments_search_list'),
    path('comments/register',
         views.CommentCreateView.as_view(),
         name='comments_register'),
]
