from django.urls import path
from .import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<post_id>[0-9]+)/', views.detail, name='detail'),
    path('addpost', views.addpost, name='addpost'),
    path('(?P<post_id>[0-9]+)/delete/', views.delete, name='delete'),
    # path('(?P<post_id>[0-9]+)/', views.UpdateView.as_view(), name='edit'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('(?P<post_id>[0-9]+)/favorite/', views.favorite, name='favorite'),
    path('favorites', views.favorites, name='favorites'),
]