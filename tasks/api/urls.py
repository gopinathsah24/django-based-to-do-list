from django.urls import path

from tasks.api.views import api_detail_task_view,api_update_task_view,api_delete_view,api_create_view


app_name ="task"

urlpatterns = [
    path('detail/<int:pk>/',api_detail_task_view,name="detail"),
    path('delete/<int:pk>/',api_delete_view,name="delete"),
    path('update/<int:pk>/',api_update_task_view,name="update"),
    path('create/',api_create_view,name="create"),
]
