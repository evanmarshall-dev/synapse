from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('posts/', views.post_index, name='post_index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup')
]