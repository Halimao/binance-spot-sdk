# binance_spot.FuturesApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_futures_hist_data_link_get**](FuturesApi.md#sapi_v1_futures_hist_data_link_get) | **GET** /sapi/v1/futures/histDataLink | Get Future TickLevel Orderbook Historical Data Download Link (USER_DATA)
[**sapi_v1_futures_transfer_get**](FuturesApi.md#sapi_v1_futures_transfer_get) | **GET** /sapi/v1/futures/transfer | Get Future Account Transaction History List (USER_DATA)
[**sapi_v1_futures_transfer_post**](FuturesApi.md#sapi_v1_futures_transfer_post) | **POST** /sapi/v1/futures/transfer | New Future Account Transfer (USER_DATA)

# **sapi_v1_futures_hist_data_link_get**
> InlineResponse200152 sapi_v1_futures_hist_data_link_get(symbol, data_type, timestamp, signature, start_time=start_time, end_time=end_time, recv_window=recv_window)

Get Future TickLevel Orderbook Historical Data Download Link (USER_DATA)

Weight(IP): 1

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
api_instance = binance_spot.FuturesApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | 
data_type = 'data_type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Future TickLevel Orderbook Historical Data Download Link (USER_DATA)
    api_response = api_instance.sapi_v1_futures_hist_data_link_get(symbol, data_type, timestamp, signature, start_time=start_time, end_time=end_time, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->sapi_v1_futures_hist_data_link_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **data_type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200152**](InlineResponse200152.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_futures_transfer_get**
> InlineResponse200150 sapi_v1_futures_transfer_get(asset, start_time, timestamp, signature, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Future Account Transaction History List (USER_DATA)

Weight(IP): 10

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
api_instance = binance_spot.FuturesApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
start_time = 789 # int | UTC timestamp in ms
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Future Account Transaction History List (USER_DATA)
    api_response = api_instance.sapi_v1_futures_transfer_get(asset, start_time, timestamp, signature, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->sapi_v1_futures_transfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **start_time** | **int**| UTC timestamp in ms | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200150**](InlineResponse200150.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_futures_transfer_post**
> InlineResponse200151 sapi_v1_futures_transfer_post(asset, amount, type, timestamp, signature, recv_window=recv_window)

New Future Account Transfer (USER_DATA)

Execute transfer between spot account and futures account.  Weight(IP): 1

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
api_instance = binance_spot.FuturesApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
amount = 1.2 # float | 
type = 789 # int | 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures account to spot account.
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # New Future Account Transfer (USER_DATA)
    api_response = api_instance.sapi_v1_futures_transfer_post(asset, amount, type, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->sapi_v1_futures_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **type** | **int**| 1: transfer from spot account to USDT-Ⓜ futures account. 2: transfer from USDT-Ⓜ futures account to spot account. 3: transfer from spot account to COIN-Ⓜ futures account. 4: transfer from COIN-Ⓜ futures account to spot account. | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200151**](InlineResponse200151.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

