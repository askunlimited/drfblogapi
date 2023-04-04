from . import views
from django.urls import path

urlpatterns = [
    # path('homepage/', views.homepage, name='homepage'),
    path('', views.PostListCreateView.as_view(), name='list_posts'),
    path('<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name='post_detail'),

]
