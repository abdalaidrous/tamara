from tamara.client import TamaraClient
from tamara.requests.payment.capture_request import CaptureRequest
from tests import api_token


def main():
    _api_token = api_token
    client = TamaraClient(_api_token, is_sandbox_env=True)
    keyword = {
        "order_id": "846cb1de-7ec8-45c2-9ed1-a5f31360ad05",
        "total_amount": {
            "amount": 100.55,
            "currency": "SAR"
        },
        "tax_amount": {
            "amount": "100.00",
            "currency": "SAR"
        },
        "shipping_amount": {
            "amount": "100.00",
            "currency": "SAR"
        },
        "discount_amount": {
            "amount": "100.00",
            "currency": "SAR"
        },
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
        "shipping_info": {
            "shipped_at": "2019-08-24T14:15:22Z",
            "shipping_company": "DHL",
            "tracking_number": "123456",
            "tracking_url": "https://shipping.com/tracking?id=123456"
        }
    }
    request = CaptureRequest.from_dictionary(keyword)
    response = client.capture(request)
    print(response.to_dictionary())


if __name__ == '__main__':
    main()
