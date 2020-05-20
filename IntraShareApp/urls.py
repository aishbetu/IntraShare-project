from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('allResponses/', views.allResponses, name='all_responses'),

    path('allResponses/response/<int:response_id>/', views.viewResponse, name='view_response'),

    path('company/add', views.add_company, name='add_company'),

    path('response/new/', views.new_response, name='new_response'),

    path('allResponses/<int:response_id>/update', views.update_response, name='update_response'),

    path('allResponses/<int:response_id>/delete', views.delete_response, name='delete_response'),

    path('comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),

    path('comment/<int:comment_id>/update', views.update_comment, name='update_comment'),
]