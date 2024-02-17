from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
    path('set_password/', views.SetPasswordView.as_view(), name='set_password'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('user_adress/', views.UserAddressView.as_view(), name='address'),
    path('forgot_password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot_password/verify/', views.ForgotPasswordVerifyView.as_view(), name='forgot_password_verify'),
    path('set_new_password/', views.SetNewPasswordView.as_view(), name='set_new_password'),
]
