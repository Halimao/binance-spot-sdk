# binance_spot.SimpleEarnApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_simple_earn_account_get**](SimpleEarnApi.md#sapi_v1_simple_earn_account_get) | **GET** /sapi/v1/simple-earn/account | Simple Account (USER_DATA)
[**sapi_v1_simple_earn_flexible_history_collateral_record_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_history_collateral_record_get) | **GET** /sapi/v1/simple-earn/flexible/history/collateralRecord | Get Collateral Record (USER_DATA)
[**sapi_v1_simple_earn_flexible_history_rate_history_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_history_rate_history_get) | **GET** /sapi/v1/simple-earn/flexible/history/rateHistory | Get Rate History (USER_DATA)
[**sapi_v1_simple_earn_flexible_history_redemption_record_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_history_redemption_record_get) | **GET** /sapi/v1/simple-earn/flexible/history/redemptionRecord | Get Flexible Redemption Record (USER_DATA)
[**sapi_v1_simple_earn_flexible_history_rewards_record_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_history_rewards_record_get) | **GET** /sapi/v1/simple-earn/flexible/history/rewardsRecord | Get Flexible Rewards History (USER_DATA)
[**sapi_v1_simple_earn_flexible_history_subscription_record_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_history_subscription_record_get) | **GET** /sapi/v1/simple-earn/flexible/history/subscriptionRecord | Get Flexible Subscription Record (USER_DATA)
[**sapi_v1_simple_earn_flexible_list_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_list_get) | **GET** /sapi/v1/simple-earn/flexible/list | Get Simple Earn Flexible Product List (USER_DATA)
[**sapi_v1_simple_earn_flexible_personal_left_quota_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_personal_left_quota_get) | **GET** /sapi/v1/simple-earn/flexible/personalLeftQuota | Get Flexible Personal Left Quota (USER_DATA)
[**sapi_v1_simple_earn_flexible_position_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_position_get) | **GET** /sapi/v1/simple-earn/flexible/position | Get Flexible Product Position (USER_DATA)
[**sapi_v1_simple_earn_flexible_redeem_post**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_redeem_post) | **POST** /sapi/v1/simple-earn/flexible/redeem | Redeem Flexible Product (TRADE)
[**sapi_v1_simple_earn_flexible_set_auto_subscribe_post**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_set_auto_subscribe_post) | **POST** /sapi/v1/simple-earn/flexible/setAutoSubscribe | Set Flexible Auto Subscribe (USER_DATA)
[**sapi_v1_simple_earn_flexible_subscribe_post**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_subscribe_post) | **POST** /sapi/v1/simple-earn/flexible/subscribe | Subscribe Flexible Product (TRADE)
[**sapi_v1_simple_earn_flexible_subscription_preview_get**](SimpleEarnApi.md#sapi_v1_simple_earn_flexible_subscription_preview_get) | **GET** /sapi/v1/simple-earn/flexible/subscriptionPreview | Get Flexible Subscription Preview (USER_DATA)
[**sapi_v1_simple_earn_locked_history_redemption_record_get**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_history_redemption_record_get) | **GET** /sapi/v1/simple-earn/locked/history/redemptionRecord | Get Locked Redemption Record (USER_DATA)
[**sapi_v1_simple_earn_locked_history_rewards_record_get**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_history_rewards_record_get) | **GET** /sapi/v1/simple-earn/locked/history/rewardsRecord | Get Locked Rewards History (USER_DATA)
[**sapi_v1_simple_earn_locked_history_subscription_record_get**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_history_subscription_record_get) | **GET** /sapi/v1/simple-earn/locked/history/subscriptionRecord | Get Locked Subscription Record (USER_DATA)
[**sapi_v1_simple_earn_locked_list_get**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_list_get) | **GET** /sapi/v1/simple-earn/locked/list | Get Simple Earn Locked Product List (USER_DATA)
[**sapi_v1_simple_earn_locked_personal_left_quota_get**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_personal_left_quota_get) | **GET** /sapi/v1/simple-earn/locked/personalLeftQuota | Get Locked Personal Left Quota (USER_DATA)
[**sapi_v1_simple_earn_locked_position_get**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_position_get) | **GET** /sapi/v1/simple-earn/locked/position | Get Locked Product Position (USER_DATA)
[**sapi_v1_simple_earn_locked_redeem_post**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_redeem_post) | **POST** /sapi/v1/simple-earn/locked/redeem | Redeem Locked Product (TRADE)
[**sapi_v1_simple_earn_locked_set_auto_subscribe_post**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_set_auto_subscribe_post) | **POST** /sapi/v1/simple-earn/locked/setAutoSubscribe | Set Locked Auto Subscribe (USER_DATA)
[**sapi_v1_simple_earn_locked_subscribe_post**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_subscribe_post) | **POST** /sapi/v1/simple-earn/locked/subscribe | Subscribe Locked Product (TRADE)
[**sapi_v1_simple_earn_locked_subscription_preview_get**](SimpleEarnApi.md#sapi_v1_simple_earn_locked_subscription_preview_get) | **GET** /sapi/v1/simple-earn/locked/subscriptionPreview | Get Locked Subscription Preview (USER_DATA)

# **sapi_v1_simple_earn_account_get**
> InlineResponse200263 sapi_v1_simple_earn_account_get(timestamp, signature, recv_window=recv_window)

Simple Account (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Simple Account (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_account_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200263**](InlineResponse200263.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_history_collateral_record_get**
> InlineResponse200273 sapi_v1_simple_earn_flexible_history_collateral_record_get(timestamp, signature, product_id=product_id, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Collateral Record (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
product_id = 'product_id_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Collateral Record (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_history_collateral_record_get(timestamp, signature, product_id=product_id, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_history_collateral_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **product_id** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200273**](InlineResponse200273.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_history_rate_history_get**
> InlineResponse200272 sapi_v1_simple_earn_flexible_history_rate_history_get(product_id, timestamp, signature, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Rate History (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
product_id = 'product_id_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Rate History (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_history_rate_history_get(product_id, timestamp, signature, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_history_rate_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200272**](InlineResponse200272.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_history_redemption_record_get**
> InlineResponse200266 sapi_v1_simple_earn_flexible_history_redemption_record_get(product_id=product_id, redeem_id=redeem_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size)

Get Flexible Redemption Record (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
product_id = 'product_id_example' # str |  (optional)
redeem_id = 'redeem_id_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)

try:
    # Get Flexible Redemption Record (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_history_redemption_record_get(product_id=product_id, redeem_id=redeem_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_history_redemption_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | [optional] 
 **redeem_id** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 

### Return type

[**InlineResponse200266**](InlineResponse200266.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_history_rewards_record_get**
> InlineResponse200268 sapi_v1_simple_earn_flexible_history_rewards_record_get(type, product_id=product_id, asset=asset, start_time=start_time, end_time=end_time)

Get Flexible Rewards History (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
type = 'type_example' # str | \"BONUS\", \"REALTIME\", \"REWARDS\"
product_id = 'product_id_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)

try:
    # Get Flexible Rewards History (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_history_rewards_record_get(type, product_id=product_id, asset=asset, start_time=start_time, end_time=end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_history_rewards_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| \&quot;BONUS\&quot;, \&quot;REALTIME\&quot;, \&quot;REWARDS\&quot; | 
 **product_id** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 

### Return type

[**InlineResponse200268**](InlineResponse200268.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_history_subscription_record_get**
> InlineResponse200264 sapi_v1_simple_earn_flexible_history_subscription_record_get(timestamp, signature, product_id=product_id, purchase_id=purchase_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Flexible Subscription Record (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
product_id = 'product_id_example' # str |  (optional)
purchase_id = 'purchase_id_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Flexible Subscription Record (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_history_subscription_record_get(timestamp, signature, product_id=product_id, purchase_id=purchase_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_history_subscription_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **product_id** | **str**|  | [optional] 
 **purchase_id** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200264**](InlineResponse200264.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_list_get**
> InlineResponse200256 sapi_v1_simple_earn_flexible_list_get(timestamp, signature, asset=asset, current=current, size=size, recv_window=recv_window)

Get Simple Earn Flexible Product List (USER_DATA)

Get available Simple Earn flexible product list  Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Simple Earn Flexible Product List (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_list_get(timestamp, signature, asset=asset, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200256**](InlineResponse200256.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_personal_left_quota_get**
> InlineResponse200136 sapi_v1_simple_earn_flexible_personal_left_quota_get(product_id, timestamp, signature, recv_window=recv_window)

Get Flexible Personal Left Quota (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
product_id = 'product_id_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Flexible Personal Left Quota (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_personal_left_quota_get(product_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_personal_left_quota_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200136**](InlineResponse200136.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_position_get**
> InlineResponse200261 sapi_v1_simple_earn_flexible_position_get(timestamp, signature, asset=asset, product_id=product_id, current=current, size=size, recv_window=recv_window)

Get Flexible Product Position (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
product_id = 'product_id_example' # str |  (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Flexible Product Position (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_position_get(timestamp, signature, asset=asset, product_id=product_id, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_position_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **product_id** | **str**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200261**](InlineResponse200261.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_redeem_post**
> InlineResponse200260 sapi_v1_simple_earn_flexible_redeem_post(product_id, timestamp, signature, redeem_all=redeem_all, amount=amount, dest_account=dest_account, recv_window=recv_window)

Redeem Flexible Product (TRADE)

Weight(IP): 1  Rate Limit: 1/3s per account

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
product_id = 'product_id_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
redeem_all = true # bool | true or false, default to false (optional)
amount = 1.2 # float | if redeemAll is false, amount is mandatory (optional)
dest_account = 'dest_account_example' # str | SPOT,FUND,ALL, default SPOT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Redeem Flexible Product (TRADE)
    api_response = api_instance.sapi_v1_simple_earn_flexible_redeem_post(product_id, timestamp, signature, redeem_all=redeem_all, amount=amount, dest_account=dest_account, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_redeem_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **redeem_all** | **bool**| true or false, default to false | [optional] 
 **amount** | **float**| if redeemAll is false, amount is mandatory | [optional] 
 **dest_account** | **str**| SPOT,FUND,ALL, default SPOT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200260**](InlineResponse200260.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_set_auto_subscribe_post**
> InlineResponse20054 sapi_v1_simple_earn_flexible_set_auto_subscribe_post(product_id, auto_subscribe, timestamp, signature, recv_window=recv_window)

Set Flexible Auto Subscribe (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
product_id = 'product_id_example' # str | 
auto_subscribe = true # bool | true or false
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Set Flexible Auto Subscribe (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_set_auto_subscribe_post(product_id, auto_subscribe, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_set_auto_subscribe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **auto_subscribe** | **bool**| true or false | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_subscribe_post**
> InlineResponse200258 sapi_v1_simple_earn_flexible_subscribe_post(product_id, amount, timestamp, signature, auto_subscribe=auto_subscribe, source_account=source_account, recv_window=recv_window)

Subscribe Flexible Product (TRADE)

Weight(IP): 1  Rate Limit: 1/3s per account

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
product_id = 'product_id_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
auto_subscribe = true # bool | true or false, default true. (optional)
source_account = 'source_account_example' # str | SPOT,FUND,ALL, default SPOT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Subscribe Flexible Product (TRADE)
    api_response = api_instance.sapi_v1_simple_earn_flexible_subscribe_post(product_id, amount, timestamp, signature, auto_subscribe=auto_subscribe, source_account=source_account, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_subscribe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **auto_subscribe** | **bool**| true or false, default true. | [optional] 
 **source_account** | **str**| SPOT,FUND,ALL, default SPOT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200258**](InlineResponse200258.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_flexible_subscription_preview_get**
> InlineResponse200270 sapi_v1_simple_earn_flexible_subscription_preview_get(product_id, amount, timestamp, signature, recv_window=recv_window)

Get Flexible Subscription Preview (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
product_id = 'product_id_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Flexible Subscription Preview (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_flexible_subscription_preview_get(product_id, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_flexible_subscription_preview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200270**](InlineResponse200270.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_history_redemption_record_get**
> InlineResponse200267 sapi_v1_simple_earn_locked_history_redemption_record_get(timestamp, signature, position_id=position_id, redeem_id=redeem_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Locked Redemption Record (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
position_id = 'position_id_example' # str |  (optional)
redeem_id = 'redeem_id_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Locked Redemption Record (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_locked_history_redemption_record_get(timestamp, signature, position_id=position_id, redeem_id=redeem_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_history_redemption_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **position_id** | **str**|  | [optional] 
 **redeem_id** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200267**](InlineResponse200267.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_history_rewards_record_get**
> InlineResponse200269 sapi_v1_simple_earn_locked_history_rewards_record_get(timestamp, signature, position_id=position_id, asset=asset, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)

Get Locked Rewards History (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
position_id = 'position_id_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Locked Rewards History (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_locked_history_rewards_record_get(timestamp, signature, position_id=position_id, asset=asset, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_history_rewards_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **position_id** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200269**](InlineResponse200269.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_history_subscription_record_get**
> InlineResponse200265 sapi_v1_simple_earn_locked_history_subscription_record_get(timestamp, signature, purchase_id=purchase_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Locked Subscription Record (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
purchase_id = 'purchase_id_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Locked Subscription Record (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_locked_history_subscription_record_get(timestamp, signature, purchase_id=purchase_id, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_history_subscription_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **purchase_id** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200265**](InlineResponse200265.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_list_get**
> InlineResponse200257 sapi_v1_simple_earn_locked_list_get(timestamp, signature, asset=asset, current=current, size=size, recv_window=recv_window)

Get Simple Earn Locked Product List (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Simple Earn Locked Product List (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_locked_list_get(timestamp, signature, asset=asset, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200257**](InlineResponse200257.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_personal_left_quota_get**
> InlineResponse200136 sapi_v1_simple_earn_locked_personal_left_quota_get(project_id, timestamp, signature, recv_window=recv_window)

Get Locked Personal Left Quota (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
project_id = 'project_id_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Locked Personal Left Quota (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_locked_personal_left_quota_get(project_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_personal_left_quota_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200136**](InlineResponse200136.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_position_get**
> InlineResponse200262 sapi_v1_simple_earn_locked_position_get(timestamp, signature, asset=asset, position_id=position_id, project_id=project_id, current=current, size=size, recv_window=recv_window)

Get Locked Product Position (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
position_id = 'position_id_example' # str |  (optional)
project_id = 'project_id_example' # str |  (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Locked Product Position (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_locked_position_get(timestamp, signature, asset=asset, position_id=position_id, project_id=project_id, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_position_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **position_id** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200262**](InlineResponse200262.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_redeem_post**
> InlineResponse200260 sapi_v1_simple_earn_locked_redeem_post(position_id, timestamp, signature, recv_window=recv_window)

Redeem Locked Product (TRADE)

Weight(IP): 1  Rate Limit: 1/3s per account

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
position_id = 'position_id_example' # str | 1234
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Redeem Locked Product (TRADE)
    api_response = api_instance.sapi_v1_simple_earn_locked_redeem_post(position_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_redeem_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **str**| 1234 | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200260**](InlineResponse200260.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_set_auto_subscribe_post**
> InlineResponse20054 sapi_v1_simple_earn_locked_set_auto_subscribe_post(position_id, auto_subscribe, timestamp, signature, recv_window=recv_window)

Set Locked Auto Subscribe (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
position_id = 'position_id_example' # str | 
auto_subscribe = true # bool | true or false
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Set Locked Auto Subscribe (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_locked_set_auto_subscribe_post(position_id, auto_subscribe, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_set_auto_subscribe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **str**|  | 
 **auto_subscribe** | **bool**| true or false | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_subscribe_post**
> InlineResponse200259 sapi_v1_simple_earn_locked_subscribe_post(project_id, amount, timestamp, signature, auto_subscribe=auto_subscribe, source_account=source_account, recv_window=recv_window)

Subscribe Locked Product (TRADE)

Weight(IP): 1  Rate Limit: 1/3s per account

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
project_id = 'project_id_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
auto_subscribe = true # bool | true or false, default true. (optional)
source_account = 'source_account_example' # str | SPOT,FUND,ALL, default SPOT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Subscribe Locked Product (TRADE)
    api_response = api_instance.sapi_v1_simple_earn_locked_subscribe_post(project_id, amount, timestamp, signature, auto_subscribe=auto_subscribe, source_account=source_account, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_subscribe_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **auto_subscribe** | **bool**| true or false, default true. | [optional] 
 **source_account** | **str**| SPOT,FUND,ALL, default SPOT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200259**](InlineResponse200259.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_simple_earn_locked_subscription_preview_get**
> list[InlineResponse200271] sapi_v1_simple_earn_locked_subscription_preview_get(project_id, amount, timestamp, signature, auto_subscribe=auto_subscribe, recv_window=recv_window)

Get Locked Subscription Preview (USER_DATA)

Weight(IP): 150

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
api_instance = binance_spot.SimpleEarnApi(binance_spot.ApiClient(configuration))
project_id = 'project_id_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
auto_subscribe = true # bool | true or false, default true. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Locked Subscription Preview (USER_DATA)
    api_response = api_instance.sapi_v1_simple_earn_locked_subscription_preview_get(project_id, amount, timestamp, signature, auto_subscribe=auto_subscribe, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimpleEarnApi->sapi_v1_simple_earn_locked_subscription_preview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **auto_subscribe** | **bool**| true or false, default true. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200271]**](InlineResponse200271.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

