# PythonSDKGeneration
Prototyping Adyen Python SDK generation from OpenAPI file using [python-nextgen](https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/python-nextgen) generator.

This is built using OpenAPI Generator v6.3.0-SNAPSHOT

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