from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from users.models import User, Payments
from users.serializers import UserSerializer, PaymentSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_method', 'paid_course', 'paid_lesson',)
    ordering_fields = ('data',)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()