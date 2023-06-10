from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog_list/', views.BlogList.as_view(), name='blog_list'),
    path('write_blog/', views.CreateBlog.as_view(), name='write_blog'),
    path('details/<int:id>/', views.blog_details, name='details'),
    path('author_details/<pk>/',
         views.AuthorDetails.as_view(), name='author_details'),
    path('like/<pk>/', views.like, name='like'),
    path('unlike/<pk>/', views.unlike, name='unlike'),
    path('myblog/', views.MyBlog.as_view(), name='myblog'),
    path('editblog/<pk>/', views.EditBlog.as_view(), name='editblog'),
    path('delete/<pk>/', views.DeleteBlog.as_view(), name='delete')
]
