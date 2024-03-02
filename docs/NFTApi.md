# binance_spot.NFTApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_nft_history_deposit_get**](NFTApi.md#sapi_v1_nft_history_deposit_get) | **GET** /sapi/v1/nft/history/deposit | Get NFT Deposit History(USER_DATA)
[**sapi_v1_nft_history_transactions_get**](NFTApi.md#sapi_v1_nft_history_transactions_get) | **GET** /sapi/v1/nft/history/transactions | Get NFT Transaction History (USER_DATA)
[**sapi_v1_nft_history_withdraw_get**](NFTApi.md#sapi_v1_nft_history_withdraw_get) | **GET** /sapi/v1/nft/history/withdraw | Get NFT Withdraw History (USER_DATA)
[**sapi_v1_nft_user_get_asset_get**](NFTApi.md#sapi_v1_nft_user_get_asset_get) | **GET** /sapi/v1/nft/user/getAsset | Get NFT Asset (USER_DATA)

# **sapi_v1_nft_history_deposit_get**
> InlineResponse200232 sapi_v1_nft_history_deposit_get(timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)

Get NFT Deposit History(USER_DATA)

- The max interval between startTime and endTime is 90 days. - If startTime and endTime are not sent, the recent 7 days' data will be returned.  Weight(UID): 3000

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
api_instance = binance_spot.NFTApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 50, Max 50 (optional)
page = 56 # int | Default 1 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get NFT Deposit History(USER_DATA)
    api_response = api_instance.sapi_v1_nft_history_deposit_get(timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFTApi->sapi_v1_nft_history_deposit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 50, Max 50 | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200232**](InlineResponse200232.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_nft_history_transactions_get**
> InlineResponse200231 sapi_v1_nft_history_transactions_get(order_type, timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)

Get NFT Transaction History (USER_DATA)

- The max interval between startTime and endTime is 90 days. - If startTime and endTime are not sent, the recent 7 days' data will be returned.  Weight(UID): 3000

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
api_instance = binance_spot.NFTApi(binance_spot.ApiClient(configuration))
order_type = 56 # int | 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 50, Max 50 (optional)
page = 56 # int | Default 1 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get NFT Transaction History (USER_DATA)
    api_response = api_instance.sapi_v1_nft_history_transactions_get(order_type, timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFTApi->sapi_v1_nft_history_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_type** | **int**| 0: purchase order, 1: sell order, 2: royalty income, 3: primary market order, 4: mint fee | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 50, Max 50 | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200231**](InlineResponse200231.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_nft_history_withdraw_get**
> InlineResponse200233 sapi_v1_nft_history_withdraw_get(timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)

Get NFT Withdraw History (USER_DATA)

- The max interval between startTime and endTime is 90 days. - If startTime and endTime are not sent, the recent 7 days' data will be returned.  Weight(UID): 3000

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
api_instance = binance_spot.NFTApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 50, Max 50 (optional)
page = 56 # int | Default 1 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get NFT Withdraw History (USER_DATA)
    api_response = api_instance.sapi_v1_nft_history_withdraw_get(timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, page=page, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFTApi->sapi_v1_nft_history_withdraw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 50, Max 50 | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200233**](InlineResponse200233.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_nft_user_get_asset_get**
> InlineResponse200234 sapi_v1_nft_user_get_asset_get(timestamp, signature, limit=limit, page=page, recv_window=recv_window)

Get NFT Asset (USER_DATA)

Weight(UID): 3000

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
api_instance = binance_spot.NFTApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
limit = 56 # int | Default 50, Max 50 (optional)
page = 56 # int | Default 1 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get NFT Asset (USER_DATA)
    api_response = api_instance.sapi_v1_nft_user_get_asset_get(timestamp, signature, limit=limit, page=page, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NFTApi->sapi_v1_nft_user_get_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **limit** | **int**| Default 50, Max 50 | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200234**](InlineResponse200234.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

