from tamara.client import TamaraClient
from tamara.requests.order.authorise_order_request import AuthoriseOrderRequest
from tests import api_token


def main():
    _api_token = api_token
    client = TamaraClient(_api_token, is_sandbox_env=True)
    request = AuthoriseOrderRequest(order_id='846cb1de-7ec8-45c2-9ed1-a5f31360ad05')
    response = client.authorise_order(request)
    print(response.to_dictionary())


if __name__ == '__main__':
    main()
