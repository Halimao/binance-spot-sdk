# binance_spot.BLVTApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_blvt_redeem_post**](BLVTApi.md#sapi_v1_blvt_redeem_post) | **POST** /sapi/v1/blvt/redeem | Redeem BLVT (USER_DATA)
[**sapi_v1_blvt_redeem_record_get**](BLVTApi.md#sapi_v1_blvt_redeem_record_get) | **GET** /sapi/v1/blvt/redeem/record | Redemption Record (USER_DATA)
[**sapi_v1_blvt_subscribe_post**](BLVTApi.md#sapi_v1_blvt_subscribe_post) | **POST** /sapi/v1/blvt/subscribe | Subscribe BLVT (USER_DATA)
[**sapi_v1_blvt_subscribe_record_get**](BLVTApi.md#sapi_v1_blvt_subscribe_record_get) | **GET** /sapi/v1/blvt/subscribe/record | Query Subscription Record (USER_DATA)
[**sapi_v1_blvt_token_info_get**](BLVTApi.md#sapi_v1_blvt_token_info_get) | **GET** /sapi/v1/blvt/tokenInfo | BLVT Info (MARKET_DATA)
[**sapi_v1_blvt_user_limit_get**](BLVTApi.md#sapi_v1_blvt_user_limit_get) | **GET** /sapi/v1/blvt/userLimit | BLVT User Limit Info (USER_DATA)

# **sapi_v1_blvt_redeem_post**
> InlineResponse200175 sapi_v1_blvt_redeem_post(token_name, amount, timestamp, signature, recv_window=recv_window)

Redeem BLVT (USER_DATA)

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
api_instance = binance_spot.BLVTApi(binance_spot.ApiClient(configuration))
token_name = 'token_name_example' # str | BTCDOWN, BTCUP
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Redeem BLVT (USER_DATA)
    api_response = api_instance.sapi_v1_blvt_redeem_post(token_name, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BLVTApi->sapi_v1_blvt_redeem_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_name** | **str**| BTCDOWN, BTCUP | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200175**](InlineResponse200175.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_blvt_redeem_record_get**
> list[InlineResponse200176] sapi_v1_blvt_redeem_record_get(timestamp, signature, token_name=token_name, id=id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Redemption Record (USER_DATA)

- Only the data of the latest 90 days is available  Weight(IP): 1

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
api_instance = binance_spot.BLVTApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
token_name = 'token_name_example' # str | BTCDOWN, BTCUP (optional)
id = 789 # int |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | default 1000, max 1000 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Redemption Record (USER_DATA)
    api_response = api_instance.sapi_v1_blvt_redeem_record_get(timestamp, signature, token_name=token_name, id=id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BLVTApi->sapi_v1_blvt_redeem_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **token_name** | **str**| BTCDOWN, BTCUP | [optional] 
 **id** | **int**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| default 1000, max 1000 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200176]**](InlineResponse200176.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_blvt_subscribe_post**
> InlineResponse200173 sapi_v1_blvt_subscribe_post(token_name, cost, timestamp, signature, recv_window=recv_window)

Subscribe BLVT (USER_DATA)

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
api_instance = binance_spot.BLVTApi(binance_spot.ApiClient(configuration))
token_name = 'token_name_example' # str | BTCDOWN, BTCUP
cost = 1.2 # float | Spot balance
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Subscribe BLVT (USER_DATA)
    api_response = api_instance.sapi_v1_blvt_subscribe_post(token_name, cost, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BLVTApi->sapi_v1_blvt_subscribe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_name** | **str**| BTCDOWN, BTCUP | 
 **cost** | **float**| Spot balance | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200173**](InlineResponse200173.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_blvt_subscribe_record_get**
> InlineResponse200174 sapi_v1_blvt_subscribe_record_get(timestamp, signature, token_name=token_name, id=id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Subscription Record (USER_DATA)

- Only the data of the latest 90 days is available  Weight(IP): 1

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
api_instance = binance_spot.BLVTApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
token_name = 'token_name_example' # str | BTCDOWN, BTCUP (optional)
id = 789 # int |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Subscription Record (USER_DATA)
    api_response = api_instance.sapi_v1_blvt_subscribe_record_get(timestamp, signature, token_name=token_name, id=id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BLVTApi->sapi_v1_blvt_subscribe_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **token_name** | **str**| BTCDOWN, BTCUP | [optional] 
 **id** | **int**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200174**](InlineResponse200174.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_blvt_token_info_get**
> list[InlineResponse200172] sapi_v1_blvt_token_info_get(token_name=token_name)

BLVT Info (MARKET_DATA)

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
api_instance = binance_spot.BLVTApi(binance_spot.ApiClient(configuration))
token_name = 'token_name_example' # str | BTCDOWN, BTCUP (optional)

try:
    # BLVT Info (MARKET_DATA)
    api_response = api_instance.sapi_v1_blvt_token_info_get(token_name=token_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BLVTApi->sapi_v1_blvt_token_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_name** | **str**| BTCDOWN, BTCUP | [optional] 

### Return type

[**list[InlineResponse200172]**](InlineResponse200172.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_blvt_user_limit_get**
> list[InlineResponse200177] sapi_v1_blvt_user_limit_get(timestamp, signature, token_name=token_name, recv_window=recv_window)

BLVT User Limit Info (USER_DATA)

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
api_instance = binance_spot.BLVTApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
token_name = 'token_name_example' # str | BTCDOWN, BTCUP (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # BLVT User Limit Info (USER_DATA)
    api_response = api_instance.sapi_v1_blvt_user_limit_get(timestamp, signature, token_name=token_name, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BLVTApi->sapi_v1_blvt_user_limit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **token_name** | **str**| BTCDOWN, BTCUP | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200177]**](InlineResponse200177.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

