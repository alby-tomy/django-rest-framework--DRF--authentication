from django.urls import path, include
from .views import RegisterAPI, LoginAPI, UserListAPI, UserViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list_user',UserViewSets, basename='list_user')

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('userlist/', UserListAPI.as_view()),
    
    path('user_list/', include(router.urls)),
]