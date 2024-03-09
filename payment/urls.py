from django.urls import path
from . import views


app_name = 'payment'
urlpatterns = [
    path('pay/', views.SendRequestView.as_view(), name='payment'),
    path('pay/verify/', views.VerifyRequestView.as_view(), name='payment_verify'),
    path('pay/success/', views.PaymentSuccessView.as_view(), name='payment_success'),
    path('pay/failed/', views.PaymentFailedView.as_view(), name='payment_failed'),
]
