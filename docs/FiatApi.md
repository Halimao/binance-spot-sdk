# binance_spot.FiatApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_fiat_orders_get**](FiatApi.md#sapi_v1_fiat_orders_get) | **GET** /sapi/v1/fiat/orders | Fiat Deposit/Withdraw History (USER_DATA)
[**sapi_v1_fiat_payments_get**](FiatApi.md#sapi_v1_fiat_payments_get) | **GET** /sapi/v1/fiat/payments | Fiat Payments History (USER_DATA)

# **sapi_v1_fiat_orders_get**
> InlineResponse200126 sapi_v1_fiat_orders_get(transaction_type, timestamp, signature, begin_time=begin_time, end_time=end_time, page=page, rows=rows, recv_window=recv_window)

Fiat Deposit/Withdraw History (USER_DATA)

- If beginTime and endTime are not sent, the recent 30-day data will be returned.  Weight(UID): 90000

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
api_instance = binance_spot.FiatApi(binance_spot.ApiClient(configuration))
transaction_type = 56 # int | * `0` - deposit * `1` - withdraw
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
begin_time = 789 # int |  (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
rows = 56 # int | Default 100, max 500 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Fiat Deposit/Withdraw History (USER_DATA)
    api_response = api_instance.sapi_v1_fiat_orders_get(transaction_type, timestamp, signature, begin_time=begin_time, end_time=end_time, page=page, rows=rows, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiatApi->sapi_v1_fiat_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_type** | **int**| * &#x60;0&#x60; - deposit * &#x60;1&#x60; - withdraw | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **begin_time** | **int**|  | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **rows** | **int**| Default 100, max 500 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200126**](InlineResponse200126.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_fiat_payments_get**
> InlineResponse200127 sapi_v1_fiat_payments_get(transaction_type, timestamp, signature, begin_time=begin_time, end_time=end_time, page=page, rows=rows, recv_window=recv_window)

Fiat Payments History (USER_DATA)

- If beginTime and endTime are not sent, the recent 30-day data will be returned.  Weight(IP): 1

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
api_instance = binance_spot.FiatApi(binance_spot.ApiClient(configuration))
transaction_type = 56 # int | * `0` - deposit * `1` - withdraw
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
begin_time = 789 # int |  (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
rows = 56 # int | Default 100, max 500 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Fiat Payments History (USER_DATA)
    api_response = api_instance.sapi_v1_fiat_payments_get(transaction_type, timestamp, signature, begin_time=begin_time, end_time=end_time, page=page, rows=rows, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FiatApi->sapi_v1_fiat_payments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_type** | **int**| * &#x60;0&#x60; - deposit * &#x60;1&#x60; - withdraw | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **begin_time** | **int**|  | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **rows** | **int**| Default 100, max 500 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200127**](InlineResponse200127.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

