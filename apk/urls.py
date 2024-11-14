from .import views
from django.urls import path
urlpatterns=[
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('product/',views.addproduct,name='product'),
    path('productlist/',views.productlist,name='productlist'),
    path('userlist/',views.userlist,name='userlist'),
    path('logout/',views.logout,name='logout'),
    path('editprofile/',views.editprofile,name='editprofile'),  
    path('deluser/<int:id>',views.deluser,name='deluser'),  
    path('delproduct/<int:id>',views.delproduct,name='delproduct'),  
    #Post Section
    path('add_post/',views.CreatePostView,name='add_post'),
    path('posts/', views.DisplayPostsView, name='view_all_posts'),
    path('posts/<int:post_id>/like/', views.like_post, name='like_post'),
    path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comments_delete/<int:cmt_id>/',views.DeleteCommentsView, name='delete_comments'),
    

]