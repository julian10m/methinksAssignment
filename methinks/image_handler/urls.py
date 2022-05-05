from django.urls import path
from . import views

app_name = 'imageHandler'

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('<int:id>', views.image_detail, name='image_detail'),
    path('test/<int:id>', views.test_vue, name='test_view'),
]
