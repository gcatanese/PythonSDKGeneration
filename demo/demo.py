import os
from pprint import pprint

from openapi_client.models.create_merchant_webhook_request import CreateMerchantWebhookRequest

import openapi_client

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def main():
    var = input("Choose 1->MyAPI Credential 2->Get webhooks 3->Create webhook: ")
    print("You entered: " + var)

    if var == "1":
        get_my_api()
    elif var == "2":
        get_merchant_webhooks()
    elif var == "3":
        create_merchant_webhook()
    else:
        print("Unrecognised choice")


def get_my_api():
    configuration = openapi_client.MgmtConfiguration()

    with openapi_client.ApiClient(configuration) as api_client:

        api_instance = openapi_client.MyAPICredentialApi(api_client)

        try:
            api_response = api_instance.get_me()
            print("The response of MyAPICredentialApi->get_me:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling MyAPICredentialApi->get_me: %s\n" % e)


def get_merchant_webhooks():
    configuration = openapi_client.MgmtConfiguration()

    with openapi_client.ApiClient(configuration) as api_client:

        api_instance = openapi_client.WebhooksMerchantLevelApi(api_client)

        try:
            api_response = api_instance.get_merchants_merchant_id_webhooks(
                merchant_id=os.environ.get("MERCHANT_ACCOUNT"))
            print("The response of WebhooksMerchantLevelApi->get webhooks:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling WebhooksMerchantLevelApi->get webhooks: %s\n" % e)


def create_merchant_webhook():
    configuration = openapi_client.MgmtConfiguration()

    with openapi_client.ApiClient(configuration) as api_client:

        api_instance = openapi_client.WebhooksMerchantLevelApi(api_client)

        try:
            api_response = api_instance.post_merchants_merchant_id_webhooks(
                merchant_id=os.environ.get("MERCHANT_ACCOUNT"),
                create_merchant_webhook_request=
                CreateMerchantWebhookRequest(
                    type="standard",
                    url="https://example.cpm",
                    active=False,
                    communicationFormat="JSON"))
            print("The response of WebhooksMerchantLevelApi->create:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling WebhooksMerchantLevelApi->create: %s\n" % e)


if __name__ == '__main__':
    main()
