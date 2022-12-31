from tamara.client import TamaraClient
from tamara.models.money import Money
from tamara.requests.checkout.check_payment_options_availability_request import CheckPaymentOptionsAvailabilityRequest
from tests import api_token


def main():
    _api_token = api_token
    client = TamaraClient(_api_token, is_sandbox_env=True)
    order = Money(currency="SAR", amount=100.00)
    request = CheckPaymentOptionsAvailabilityRequest(country='SA', order_value=order, phone_number="966561161022")
    response = client.check_payment_options_availability(request)
    print(response.to_dictionary())


if __name__ == '__main__':
    main()
