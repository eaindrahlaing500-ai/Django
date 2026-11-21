
from decimal import Decimal

from django.db.models import Q, F, Case, When, DecimalField
from inventory.models import Product


# CHALLENGE 1: Advanced Conditional Search

products = Product.objects.filter(
    (
        Q(category__name="Electronics")
        & Q(price__gt=10000)
    )
    |
    (
        Q(status="DISCOUNTED")
        & ~Q(warehouse_country="China")
    )
)

print("Challenge 1 - Matching Products:")
for product in products:
    print(product.name)


# CHALLENGE 2: Dynamic Stock Threshold Alert

stock_alerts = Product.objects.filter(
    Q(stock_quantity__lte=F("reorder_level"))
    |
    (
        Q(is_promotional=True)
        & Q(stock_quantity__lt=F("reorder_level") * 2)
    )
)

print("\nChallenge 2 - Stock Alerts:")
for product in stock_alerts:
    print(product.name, product.stock_quantity)


# CHALLENGE 3: Atomic Price Increase

updated = Product.objects.filter(
    category__name="Gadgets"
).update(
    price=Case(
        When(
            price__gt=F("max_allowed_price") / Decimal("1.15"),
            then=F("max_allowed_price")
        ),
        default=F("price") * Decimal("1.15"),
        output_field=DecimalField(
            max_digits=10,
            decimal_places=2
        )
    )
)

print("\nChallenge 3 - Products Updated:", updated)


# CHALLENGE 4: Atomic Purchase Guard

def purchase_product(product_id, quantity):
    if quantity <= 0:
        return False

    updated = Product.objects.filter(
        id=product_id,
        stock_quantity__gte=quantity
    ).update(
        stock_quantity=F("stock_quantity") - quantity,
        total_sold=F("total_sold") + quantity,
        total_revenue=F("total_revenue") + F("price") * quantity
    )

    return updated == 1


print("\nChallenge 4 - Purchase function created")
