from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name ='accounts'
urlpatterns = [
    path('', views.UserAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    # path('login/', views.login ),
    # path("token/refresh/", TokenRefreshView.as_view()),
    path('<str:username>/', views.UserDetail.as_view()),
]