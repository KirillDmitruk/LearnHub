import stripe
from forex_python.converter import CurrencyRates

stripe.api_key = "pk_test_51PVGK4JfUz4NtprN5xqLPJcv9aJkro6Lpnf8rvEOw2tcgNX6fgiHDrRtks6DZVHn8ZmKOKF8Lya5gXBehFPZ0wni00jpfLbrIn"


def create_stripe_product(object):
    """Создает продукт в stripe"""

    return stripe.Product.create(name=object)


def convert_rub_to_usd(amount):
    """Конвертирует RUB в USD"""

    c = CurrencyRates()
    rate = c.get_rate("RUB", "USD")
    return int(amount * rate)


def create_stripe_price(amount):
    """Создает цену в stripe"""

    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Payment"},
    )


def create_stripe_session(price):
    """Создает сессию на оплату в stripe"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
