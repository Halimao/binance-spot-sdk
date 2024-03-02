# binance_spot.RebateApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_rebate_tax_query_get**](RebateApi.md#sapi_v1_rebate_tax_query_get) | **GET** /sapi/v1/rebate/taxQuery | Get Spot Rebate History Records (USER_DATA)

# **sapi_v1_rebate_tax_query_get**
> InlineResponse200230 sapi_v1_rebate_tax_query_get(timestamp, signature, start_time=start_time, end_time=end_time, page=page, recv_window=recv_window)

Get Spot Rebate History Records (USER_DATA)

- The max interval between startTime and endTime is 90 days. - If startTime and endTime are not sent, the recent 7 days' data will be returned. - The earliest startTime is supported on June 10, 2020  Weight(UID): 3000

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
api_instance = binance_spot.RebateApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | default 1 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Spot Rebate History Records (USER_DATA)
    api_response = api_instance.sapi_v1_rebate_tax_query_get(timestamp, signature, start_time=start_time, end_time=end_time, page=page, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RebateApi->sapi_v1_rebate_tax_query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| default 1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200230**](InlineResponse200230.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

