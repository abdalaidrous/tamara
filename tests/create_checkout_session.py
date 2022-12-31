from tamara.client import TamaraClient
from tamara.models.order.order import Order
from tamara.requests.checkout.create_checkout_session_request import CreateCheckoutSessionRequest
from tests import api_token


def main():
    _api_token = api_token
    client = TamaraClient(_api_token, is_sandbox_env=True)
    keyword = {
        "order_reference_id": "1234561",
        "order_number": "A1234561",
        "total_amount": {
            "amount": 100.55,
            "currency": "SAR"
        },
        "description": "string",
        "country_code": "SA",
        "payment_type": "PAY_BY_INSTALMENTS",
        "instalments": None,
        "locale": "en_US",
        "items": [
            {
                "reference_id": "12333456",
                "type": "Digital",
                "name": "Lego City 8601",
                "sku": "SA-12436",
                "image_url": "https://www.example.com/product.jpg",
                "quantity": 1,
                "unit_price": {
                    "amount": "100.00",
                    "currency": "SAR"
                },
                "discount_amount": {
                    "amount": "100.00",
                    "currency": "SAR"
                },
                "tax_amount": {
                    "amount": "100.00",
                    "currency": "SAR"
                },
                "total_amount": {
                    "amount": "100.00",
                    "currency": "SAR"
                }
            }
        ],
        "consumer": {
            "first_name": "Mona",
            "last_name": "Lisa",
            "phone_number": "561161022",
            "email": "user@example.com"
        },
        "billing_address": {
            "first_name": "Mona",
            "last_name": "Lisa",
            "line1": "3764 Al Urubah Rd",
            "line2": "string",
            "region": "As Sulimaniyah",
            "postal_code": "12345",
            "city": "Riyadh",
            "country_code": "SA",
            "phone_number": "502223333"
        },
        "shipping_address": {
            "first_name": "Mona",
            "last_name": "Lisa",
            "line1": "3764 Al Urubah Rd",
            "line2": "string",
            "region": "As Sulimaniyah",
            "postal_code": "12345",
            "city": "Riyadh",
            "country_code": "SA",
            "phone_number": "502223313"
        },
        "discount": {
            "name": "Christmas 2020",
            "amount": {
                "amount": "100.00",
                "currency": "SAR"
            }
        },
        "tax_amount": {
            "amount": "100.00",
            "currency": "SAR"
        },
        "shipping_amount": {
            "amount": "100.00",
            "currency": "SAR"
        },
        "merchant_url": {
            "success": "https://example.com/checkout/success",
            "failure": "https://example.com/checkout/failure",
            "cancel": "https://example.com/checkout/cancel",
            "notification": "https://webhook.site/a1b5c693-de4a-4ff3-858b-3bf4fe119bbe"
        },
        "platform": "Magento",
        "is_mobile": False,
        "expires_in_minutes": 0,
        "additional_data": {
            "delivery_method": "home delivery",
            "pickup_store": "Store A",
            "store_code": "Store code A",
            "vendor_amount": 0,
            "merchant_settlement_amount": 0,
            "vendor_reference_code": "string"
        }
    }
    order = Order.from_dictionary(keyword)
    request = CreateCheckoutSessionRequest(order)
    response = client.create_checkout_session(request)
    print(response.to_dictionary())


if __name__ == '__main__':
    main()
