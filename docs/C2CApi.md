# binance_spot.C2CApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_c2c_order_match_list_user_order_history_get**](C2CApi.md#sapi_v1_c2c_order_match_list_user_order_history_get) | **GET** /sapi/v1/c2c/orderMatch/listUserOrderHistory | Get C2C Trade History (USER_DATA)

# **sapi_v1_c2c_order_match_list_user_order_history_get**
> InlineResponse200191 sapi_v1_c2c_order_match_list_user_order_history_get(trade_type, timestamp, signature, start_timestamp=start_timestamp, end_timestamp=end_timestamp, page=page, rows=rows, recv_window=recv_window)

Get C2C Trade History (USER_DATA)

- If startTimestamp and endTimestamp are not sent, the recent 30-day data will be returned. - The max interval between startTimestamp and endTimestamp is 30 days.  Weight(IP): 1

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
api_instance = binance_spot.C2CApi(binance_spot.ApiClient(configuration))
trade_type = 'trade_type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_timestamp = 789 # int | UTC timestamp in ms (optional)
end_timestamp = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
rows = 56 # int | default 100, max 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get C2C Trade History (USER_DATA)
    api_response = api_instance.sapi_v1_c2c_order_match_list_user_order_history_get(trade_type, timestamp, signature, start_timestamp=start_timestamp, end_timestamp=end_timestamp, page=page, rows=rows, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling C2CApi->sapi_v1_c2c_order_match_list_user_order_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trade_type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_timestamp** | **int**| UTC timestamp in ms | [optional] 
 **end_timestamp** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **rows** | **int**| default 100, max 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200191**](InlineResponse200191.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

