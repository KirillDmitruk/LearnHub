import os

import stripe

stripe.api_key = os.getenv("STRIPE_API_KEY")


def create_stripe_product(instance):
    """Создает продукт в stripe"""

    title_product = (
        f"{instance.paid_course}" if instance.paid_course else instance.paid_lesson
    )
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


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
