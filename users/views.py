from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer
from users.services import (
    create_stripe_price,
    create_stripe_session,
    create_stripe_product,
)


class UserCreateAPIView(generics.CreateAPIView):
    """ Создание Пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (
        AllowAny,
    )  # Открывает доступ для неавторизованных пользователей

    def perform_create(self, serializer):  # один из вариантов создания user (более простой)
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """ Список Пользователей """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одного Пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование Пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление Пользователя """

    queryset = User.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    """ Создание платежа """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product = create_stripe_product(payment)
        # amount_in_usd = convert_rub_to_usd(payment.amount)
        price = create_stripe_price(payment.amount, product)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link

        payment.save()


class PaymentListAPIView(generics.ListAPIView):
    """ Список Платежей """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = (
        "payment_method",
        "paid_course",
        "paid_lesson",
    )
    ordering_fields = ("data",)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одного Платежа """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование Платежа """

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    """ Удаление Платежа """

    queryset = Payment.objects.all()
