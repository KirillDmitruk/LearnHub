from django.urls import path

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView, PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView,
    PaymentDestroyAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    # users
    path("create/", UserCreateAPIView.as_view(), name="users_create"),
    path("", UserListAPIView.as_view(), name="users_list"),
    path("users_detail/<int:pk>/", UserRetrieveAPIView.as_view(), name="users_detail"),
    path("users_update/<int:pk>/", UserUpdateAPIView.as_view(), name="users_update"),
    path("users_delete/<int:pk>/", UserDestroyAPIView.as_view(), name="users_delete"),
    # payments
    path("payment_create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payment/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_detail"),
    path("payment_update/<int:pk>/", PaymentUpdateAPIView.as_view(), name="payment_update"),
    path("payment_delete/<int:pk>/", PaymentDestroyAPIView.as_view(), name="payment_delete"),
]
