# binance_spot.GiftCardApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_giftcard_buy_code_post**](GiftCardApi.md#sapi_v1_giftcard_buy_code_post) | **POST** /sapi/v1/giftcard/buyCode | Buy a Binance Code (TRADE)
[**sapi_v1_giftcard_buy_code_token_limit_get**](GiftCardApi.md#sapi_v1_giftcard_buy_code_token_limit_get) | **GET** /sapi/v1/giftcard/buyCode/token-limit | Fetch Token Limit (USER_DATA)
[**sapi_v1_giftcard_create_code_post**](GiftCardApi.md#sapi_v1_giftcard_create_code_post) | **POST** /sapi/v1/giftcard/createCode | Create a Binance Code (USER_DATA)
[**sapi_v1_giftcard_cryptography_rsa_public_key_get**](GiftCardApi.md#sapi_v1_giftcard_cryptography_rsa_public_key_get) | **GET** /sapi/v1/giftcard/cryptography/rsa-public-key | Fetch RSA Public Key (USER_DATA)
[**sapi_v1_giftcard_redeem_code_post**](GiftCardApi.md#sapi_v1_giftcard_redeem_code_post) | **POST** /sapi/v1/giftcard/redeemCode | Redeem a Binance Code (USER_DATA)
[**sapi_v1_giftcard_verify_get**](GiftCardApi.md#sapi_v1_giftcard_verify_get) | **GET** /sapi/v1/giftcard/verify | Verify a Binance Code (USER_DATA)

# **sapi_v1_giftcard_buy_code_post**
> InlineResponse200235 sapi_v1_giftcard_buy_code_post(base_token, face_token, base_token_amount, timestamp, signature, recv_window=recv_window)

Buy a Binance Code (TRADE)

This API is for buying a fixed-value Binance Code, which means your Binance Code will be redeemable to a token that is different to the token that you are paying in. If the token you’re paying and the redeemable token are the same, please use the Create Binance Code endpoint. You can use supported crypto currency or fiat token as baseToken to buy Binance Code that is redeemable to your chosen faceToken. Once successfully purchased, the amount of baseToken would be deducted from your funding wallet.  To get started with, please make sure: - You have a Binance account - You have passed kyc - You have a sufficient balance in your Binance funding wallet - You need Enable Withdrawals for the API Key which requests this endpoint.  Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = binance_spot.Configuration()
configuration.api_key['X-MBX-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-MBX-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = binance_spot.GiftCardApi(binance_spot.ApiClient(configuration))
base_token = 'base_token_example' # str | The token you want to pay, example BUSD
face_token = 'face_token_example' # str | The token you want to buy, example BNB. If faceToken = baseToken, it's the same as createCode endpoint.
base_token_amount = 1.2 # float | The base token asset quantity, example  1.002
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Buy a Binance Code (TRADE)
    api_response = api_instance.sapi_v1_giftcard_buy_code_post(base_token, face_token, base_token_amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftCardApi->sapi_v1_giftcard_buy_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_token** | **str**| The token you want to pay, example BUSD | 
 **face_token** | **str**| The token you want to buy, example BNB. If faceToken &#x3D; baseToken, it&#x27;s the same as createCode endpoint. | 
 **base_token_amount** | **float**| The base token asset quantity, example  1.002 | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200235**](InlineResponse200235.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_giftcard_buy_code_token_limit_get**
> InlineResponse200239 sapi_v1_giftcard_buy_code_token_limit_get(base_token, timestamp, signature, recv_window=recv_window)

Fetch Token Limit (USER_DATA)

This API is to help you verify which tokens are available for you to purchase fixed-value gift cards as mentioned in section 2 and it's limitation.  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = binance_spot.Configuration()
configuration.api_key['X-MBX-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-MBX-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = binance_spot.GiftCardApi(binance_spot.ApiClient(configuration))
base_token = 'base_token_example' # str | The token you want to pay, example BUSD
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Fetch Token Limit (USER_DATA)
    api_response = api_instance.sapi_v1_giftcard_buy_code_token_limit_get(base_token, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftCardApi->sapi_v1_giftcard_buy_code_token_limit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_token** | **str**| The token you want to pay, example BUSD | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200239**](InlineResponse200239.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_giftcard_create_code_post**
> InlineResponse200235 sapi_v1_giftcard_create_code_post(token, amount, timestamp, signature, recv_window=recv_window)

Create a Binance Code (USER_DATA)

This API is for creating a Binance Code. To get started with, please make sure:  - You have a Binance account - You have passed kyc - You have a sufficient balance in your Binance funding wallet - You need Enable Withdrawals for the API Key which requests this endpoint.  Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = binance_spot.Configuration()
configuration.api_key['X-MBX-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-MBX-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = binance_spot.GiftCardApi(binance_spot.ApiClient(configuration))
token = 'token_example' # str | The coin type contained in the Binance Code
amount = 1.2 # float | The amount of the coin
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Create a Binance Code (USER_DATA)
    api_response = api_instance.sapi_v1_giftcard_create_code_post(token, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftCardApi->sapi_v1_giftcard_create_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The coin type contained in the Binance Code | 
 **amount** | **float**| The amount of the coin | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200235**](InlineResponse200235.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_giftcard_cryptography_rsa_public_key_get**
> InlineResponse200238 sapi_v1_giftcard_cryptography_rsa_public_key_get(timestamp, signature, recv_window=recv_window)

Fetch RSA Public Key (USER_DATA)

This API is for fetching the RSA Public Key. This RSA Public key will be used to encrypt the card code. Please note that the RSA Public key fetched is valid only for the current day.  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = binance_spot.Configuration()
configuration.api_key['X-MBX-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-MBX-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = binance_spot.GiftCardApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Fetch RSA Public Key (USER_DATA)
    api_response = api_instance.sapi_v1_giftcard_cryptography_rsa_public_key_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftCardApi->sapi_v1_giftcard_cryptography_rsa_public_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200238**](InlineResponse200238.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_giftcard_redeem_code_post**
> InlineResponse200236 sapi_v1_giftcard_redeem_code_post(code, timestamp, signature, external_uid=external_uid, recv_window=recv_window)

Redeem a Binance Code (USER_DATA)

This API is for redeeming the Binance Code. Once redeemed, the coins will be deposited in your funding wallet.  Please note that if you enter the wrong code 5 times within 24 hours, you will no longer be able to redeem any Binance Code that day.  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = binance_spot.Configuration()
configuration.api_key['X-MBX-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-MBX-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = binance_spot.GiftCardApi(binance_spot.ApiClient(configuration))
code = 'code_example' # str | Binance Code
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
external_uid = 'external_uid_example' # str | Each external unique ID represents a unique user on the partner platform. The function helps you to identify the redemption behavior of different users, such as redemption frequency and amount. It also helps risk and limit control of a single account, such as daily limit on redemption volume, frequency, and incorrect number of entries. This will also prevent a single user account reach the partner's daily redemption limits. We strongly recommend you to use this feature and transfer us the User ID of your users if you have different users redeeming Binance codes on your platform. To protect user data privacy, you may choose to transfer the user id in any desired format (max. 400 characters). (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Redeem a Binance Code (USER_DATA)
    api_response = api_instance.sapi_v1_giftcard_redeem_code_post(code, timestamp, signature, external_uid=external_uid, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftCardApi->sapi_v1_giftcard_redeem_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Binance Code | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **external_uid** | **str**| Each external unique ID represents a unique user on the partner platform. The function helps you to identify the redemption behavior of different users, such as redemption frequency and amount. It also helps risk and limit control of a single account, such as daily limit on redemption volume, frequency, and incorrect number of entries. This will also prevent a single user account reach the partner&#x27;s daily redemption limits. We strongly recommend you to use this feature and transfer us the User ID of your users if you have different users redeeming Binance codes on your platform. To protect user data privacy, you may choose to transfer the user id in any desired format (max. 400 characters). | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200236**](InlineResponse200236.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_giftcard_verify_get**
> InlineResponse200237 sapi_v1_giftcard_verify_get(reference_no, timestamp, signature, recv_window=recv_window)

Verify a Binance Code (USER_DATA)

This API is for verifying whether the Binance Code is valid or not by entering Binance Code or reference number.  Please note that if you enter the wrong binance code 5 times within an hour, you will no longer be able to verify any binance code for that hour.  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = binance_spot.Configuration()
configuration.api_key['X-MBX-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-MBX-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = binance_spot.GiftCardApi(binance_spot.ApiClient(configuration))
reference_no = 'reference_no_example' # str | reference number
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Verify a Binance Code (USER_DATA)
    api_response = api_instance.sapi_v1_giftcard_verify_get(reference_no, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftCardApi->sapi_v1_giftcard_verify_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference_no** | **str**| reference number | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200237**](InlineResponse200237.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

