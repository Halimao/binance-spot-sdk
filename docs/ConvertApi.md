# binance_spot.ConvertApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_convert_accept_quote_post**](ConvertApi.md#sapi_v1_convert_accept_quote_post) | **POST** /sapi/v1/convert/acceptQuote | Accept Quote (TRADE)
[**sapi_v1_convert_asset_info_get**](ConvertApi.md#sapi_v1_convert_asset_info_get) | **GET** /sapi/v1/convert/assetInfo | Query order quantity precision per asset (USER_DATA)
[**sapi_v1_convert_exchange_info_get**](ConvertApi.md#sapi_v1_convert_exchange_info_get) | **GET** /sapi/v1/convert/exchangeInfo | List All Convert Pairs
[**sapi_v1_convert_get_quote_post**](ConvertApi.md#sapi_v1_convert_get_quote_post) | **POST** /sapi/v1/convert/getQuote | Send quote request (USER_DATA)
[**sapi_v1_convert_order_status_get**](ConvertApi.md#sapi_v1_convert_order_status_get) | **GET** /sapi/v1/convert/orderStatus | Order status (USER_DATA)
[**sapi_v1_convert_trade_flow_get**](ConvertApi.md#sapi_v1_convert_trade_flow_get) | **GET** /sapi/v1/convert/tradeFlow | Get Convert Trade History (USER_DATA)

# **sapi_v1_convert_accept_quote_post**
> InlineResponse200227 sapi_v1_convert_accept_quote_post(quote_id, timestamp, signature, recv_window=recv_window)

Accept Quote (TRADE)

Accept the offered quote by quote ID.  Weight(UID): 500

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
api_instance = binance_spot.ConvertApi(binance_spot.ApiClient(configuration))
quote_id = 'quote_id_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Accept Quote (TRADE)
    api_response = api_instance.sapi_v1_convert_accept_quote_post(quote_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertApi->sapi_v1_convert_accept_quote_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200227**](InlineResponse200227.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_convert_asset_info_get**
> list[InlineResponse200225] sapi_v1_convert_asset_info_get(timestamp, signature, recv_window=recv_window)

Query order quantity precision per asset (USER_DATA)

Query for supported asset precision information  Weight(IP): 100

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
api_instance = binance_spot.ConvertApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query order quantity precision per asset (USER_DATA)
    api_response = api_instance.sapi_v1_convert_asset_info_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertApi->sapi_v1_convert_asset_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200225]**](InlineResponse200225.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_convert_exchange_info_get**
> list[InlineResponse200224] sapi_v1_convert_exchange_info_get(from_asset=from_asset, to_asset=to_asset)

List All Convert Pairs

Query for all convertible token pairs and the tokens’ respective upper/lower limits  Weight(IP): 3000

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.ConvertApi()
from_asset = 'from_asset_example' # str | User spends coin (optional)
to_asset = 'to_asset_example' # str | User receives coin (optional)

try:
    # List All Convert Pairs
    api_response = api_instance.sapi_v1_convert_exchange_info_get(from_asset=from_asset, to_asset=to_asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertApi->sapi_v1_convert_exchange_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset** | **str**| User spends coin | [optional] 
 **to_asset** | **str**| User receives coin | [optional] 

### Return type

[**list[InlineResponse200224]**](InlineResponse200224.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_convert_get_quote_post**
> InlineResponse200226 sapi_v1_convert_get_quote_post(from_asset, to_asset, timestamp, signature, from_amount=from_amount, to_amount=to_amount, valid_time=valid_time, wallet_type=wallet_type, recv_window=recv_window)

Send quote request (USER_DATA)

Request a quote for the requested token pairs  Weight(UID): 200

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
api_instance = binance_spot.ConvertApi(binance_spot.ApiClient(configuration))
from_asset = 'from_asset_example' # str | 
to_asset = 'to_asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
from_amount = 3.4 # float | When specified, it is the amount you will be debited after the conversion (optional)
to_amount = 3.4 # float | When specified, it is the amount you will be debited after the conversion (optional)
valid_time = 'valid_time_example' # str | 10s, 30s, 1m, 2m, default 10s (optional)
wallet_type = 'wallet_type_example' # str | SPOT or FUNDING. Default is SPOT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Send quote request (USER_DATA)
    api_response = api_instance.sapi_v1_convert_get_quote_post(from_asset, to_asset, timestamp, signature, from_amount=from_amount, to_amount=to_amount, valid_time=valid_time, wallet_type=wallet_type, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertApi->sapi_v1_convert_get_quote_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_asset** | **str**|  | 
 **to_asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **from_amount** | **float**| When specified, it is the amount you will be debited after the conversion | [optional] 
 **to_amount** | **float**| When specified, it is the amount you will be debited after the conversion | [optional] 
 **valid_time** | **str**| 10s, 30s, 1m, 2m, default 10s | [optional] 
 **wallet_type** | **str**| SPOT or FUNDING. Default is SPOT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200226**](InlineResponse200226.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_convert_order_status_get**
> InlineResponse200228 sapi_v1_convert_order_status_get(timestamp, signature, order_id=order_id, quote_id=quote_id, recv_window=recv_window)

Order status (USER_DATA)

Query order status by order ID.  Weight(UID): 100

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
api_instance = binance_spot.ConvertApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 'order_id_example' # str |  (optional)
quote_id = 'quote_id_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Order status (USER_DATA)
    api_response = api_instance.sapi_v1_convert_order_status_get(timestamp, signature, order_id=order_id, quote_id=quote_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertApi->sapi_v1_convert_order_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **str**|  | [optional] 
 **quote_id** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200228**](InlineResponse200228.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_convert_trade_flow_get**
> InlineResponse200229 sapi_v1_convert_trade_flow_get(start_time, end_time, timestamp, signature, limit=limit, recv_window=recv_window)

Get Convert Trade History (USER_DATA)

- The max interval between startTime and endTime is 30 days.  Weight(UID): 3000

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
api_instance = binance_spot.ConvertApi(binance_spot.ApiClient(configuration))
start_time = 789 # int | UTC timestamp in ms
end_time = 789 # int | UTC timestamp in ms
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
limit = 56 # int | default 100, max 1000 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Convert Trade History (USER_DATA)
    api_response = api_instance.sapi_v1_convert_trade_flow_get(start_time, end_time, timestamp, signature, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertApi->sapi_v1_convert_trade_flow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| UTC timestamp in ms | 
 **end_time** | **int**| UTC timestamp in ms | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **limit** | **int**| default 100, max 1000 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200229**](InlineResponse200229.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

