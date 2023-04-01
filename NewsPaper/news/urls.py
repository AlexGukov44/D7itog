from django.urls import path
from .views import PostList, PostDetail, PostUpdateView, PostDeleteView, PostCreateView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_add'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
