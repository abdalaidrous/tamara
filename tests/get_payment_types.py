from tamara.client import TamaraClient
from tamara.requests.checkout.get_payment_request import GetPaymentTypesRequest
from tests import api_token


def main():
    _api_token = api_token
    client = TamaraClient(_api_token, is_sandbox_env=True)
    request = GetPaymentTypesRequest(country='SA')
    response = client.get_payment_types(request)
    print(response.to_dictionary())


if __name__ == '__main__':
    main()
