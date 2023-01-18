# PythonSDKGeneration
Prototyping Adyen Python SDK generation from OpenAPI file using [python-nextgen](https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/python-nextgen) generator.  
Built using OpenAPI Generator v6.3.0-SNAPSHOT

<p align="center">
<b>Note: this is not the official Adyen Python SDK</b>
</p>

## Code generation

Clone [OpenAPI Generator 6.3.0](https://github.com/OpenAPITools/openapi-generator) into `projects` 
folder and build from source

Generate Python code:
```
java -jar /projects/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
   -i ManagementService-v1.json \
   -g ./python-nextgen \
   -t ./templates \ 
   -o ./mgmt_api
```

## Run the demo

Create a .env file
```dotenv
    API_KEY=
    MERCHANT_ACCOUNT=
```
Run the demo and choose the operation to perform
```
    python demo.py
```

## How to use Python Management API 

### Get API credential details

```python
    configuration = openapi_client.MgmtConfiguration()

    with openapi_client.ApiClient(configuration) as api_client:

        api_instance = openapi_client.MyAPICredentialApi(api_client)

        try:
            # Get API credential details
            api_response = api_instance.get_me()
            print("The response of MyAPICredentialApi->get_me:\n")
            pprint(api_response)
        except Exception as e:
            print("Exception when calling MyAPICredentialApi->get_me: %s\n" % e)

```

### Create Merchant Webhook
```python
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
```