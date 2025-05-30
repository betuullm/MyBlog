from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('admin/post/create/', login_required(views.post_create), name='post_create'),
    path('admin/', login_required(views.post_list), name='admin_post_list'),
    path('admin/post/<int:pk>/', login_required(views.post_detail), name='admin_post_detail'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]