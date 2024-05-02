from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenBlacklistView
)


app_name ='accounts'
urlpatterns = [
    path('', views.UserAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path('logout/',views.logout),
    path('password/', views.password ),
    # path("token/refresh/", TokenRefreshView.as_view()),
    path('<str:username>/', views.UserDetail.as_view()),
]