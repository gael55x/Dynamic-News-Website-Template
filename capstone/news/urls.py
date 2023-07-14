from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('category1/', views.Category1, name='category1'),
    path('category2/', views.Category2, name='category2'),
    path('category3/', views.Category3, name='category3'),
    path('category4/', views.Category4, name='category4'),
    path('category5/', views.Category5, name='category5'),
    path('create_post/', views.Create_Post, name='create_post'),
    path('post_pending/<int:post_id>/', views.Post_pending, name='post_pending'),
    path('profile/', views.Profile, name='profile'),
    path('post_details/<int:post_id>/', views.Post_details, name='post_details'),
    path('registration_check/', views.registration_check, name='registration_check'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
