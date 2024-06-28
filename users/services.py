import stripe
from forex_python.converter import CurrencyRates

stripe.api_key = "sk_test_51PVGK4JfUz4NtprNxOfHwVXzIJnV67mATLGZcIoe2djGHzOQEJnOlQd6BERFobLJ6mtuKvRoiByf5P1Pma9INH3Z00cvRLBXQu"


def create_stripe_product(instance):
    """Создает продукт в stripe"""

    title_product = (
        f"{instance.paid_course}" if instance.paid_course else instance.paid_lesson
    )
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


# def convert_rub_to_usd(amount):
#     """ Конвертируем рубли в доллары. """
#     c = CurrencyRates()
#     rate = c.get_rate('RUB', 'USD')
#     result = int(amount * rate)
#     return result


def create_stripe_price(amount, product):
    """Создает цену в stripe"""

    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        # product_data={"name": "Payment"},
        product=product,
    )


def create_stripe_session(price):
    """Создает сессию на оплату в stripe"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
