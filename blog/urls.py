from django.urls import path
from . import views

app_name="post"
urlpatterns = [
    path('',views.index,name='starting-page'),
    path('posts',views.posts,name='posts-page'),
    path('posts/<slug:slug>',views.singlepost,name='post-detail-page'),
]
