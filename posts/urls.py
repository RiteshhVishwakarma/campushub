from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('my-posts/', views.MyPostsView.as_view(), name='my_posts'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/report/', views.ReportPostView.as_view(), name='report_post'),
]
