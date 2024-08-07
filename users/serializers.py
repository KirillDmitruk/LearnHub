from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализатор Оплаты """

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор Пользователя """

    payments_history = PaymentSerializer(many=True, source="payment", read_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "password", "payments_history")
