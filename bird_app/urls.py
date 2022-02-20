from django.urls import path
from .views import SignUpView, UserDetailView, PostListView, PostCreateView, SearchView, postDetailView, updateUserDetailView, searchDoctorView, makeThreadView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('post/<int:pk>/', postDetailView, name='post_details'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('createPost/', PostCreateView.as_view(), name = 'post_create'),
    path('', PostListView.as_view(), name = 'home'),
    path('post/searchPost/', SearchView.as_view(), name = 'search_post'), 
    path('profile/update/<int:pk>/', updateUserDetailView.as_view(), name='user_detail_update'),
    path('search/', searchDoctorView, name='search_doctor'),
    path('makeThread/<int:pk>/', makeThreadView, name='make_thread'),
    #path('createPost/<int:pk>/', PostCreateView.as_view(), name = 'post_create'),
]