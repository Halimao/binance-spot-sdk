# binance_spot.StakingApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_staking_personal_left_quota_get**](StakingApi.md#sapi_v1_staking_personal_left_quota_get) | **GET** /sapi/v1/staking/personalLeftQuota | Get Personal Left Quota of Staking Product (USER_DATA)
[**sapi_v1_staking_position_get**](StakingApi.md#sapi_v1_staking_position_get) | **GET** /sapi/v1/staking/position | Get Staking Product Position (USER_DATA)
[**sapi_v1_staking_product_list_get**](StakingApi.md#sapi_v1_staking_product_list_get) | **GET** /sapi/v1/staking/productList | Get Staking Product List (USER_DATA)
[**sapi_v1_staking_purchase_post**](StakingApi.md#sapi_v1_staking_purchase_post) | **POST** /sapi/v1/staking/purchase | Purchase Staking Product (USER_DATA)
[**sapi_v1_staking_redeem_post**](StakingApi.md#sapi_v1_staking_redeem_post) | **POST** /sapi/v1/staking/redeem | Redeem Staking Product (USER_DATA)
[**sapi_v1_staking_set_auto_staking_post**](StakingApi.md#sapi_v1_staking_set_auto_staking_post) | **POST** /sapi/v1/staking/setAutoStaking | Set Auto Staking (USER_DATA)
[**sapi_v1_staking_staking_record_get**](StakingApi.md#sapi_v1_staking_staking_record_get) | **GET** /sapi/v1/staking/stakingRecord | Get Staking History (USER_DATA)

# **sapi_v1_staking_personal_left_quota_get**
> list[InlineResponse200136] sapi_v1_staking_personal_left_quota_get(product, product_id, timestamp, signature, recv_window=recv_window)

Get Personal Left Quota of Staking Product (USER_DATA)

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
api_instance = binance_spot.StakingApi(binance_spot.ApiClient(configuration))
product = 'product_example' # str | * `STAKING` - for Locked Staking * `F_DEFI` - for flexible DeFi Staking * `L_DEFI` - for locked DeFi Staking
product_id = 'product_id_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Personal Left Quota of Staking Product (USER_DATA)
    api_response = api_instance.sapi_v1_staking_personal_left_quota_get(product, product_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->sapi_v1_staking_personal_left_quota_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| * &#x60;STAKING&#x60; - for Locked Staking * &#x60;F_DEFI&#x60; - for flexible DeFi Staking * &#x60;L_DEFI&#x60; - for locked DeFi Staking | 
 **product_id** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200136]**](InlineResponse200136.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_staking_position_get**
> list[InlineResponse200134] sapi_v1_staking_position_get(product, timestamp, signature, product_id=product_id, asset=asset, current=current, size=size, recv_window=recv_window)

Get Staking Product Position (USER_DATA)

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
api_instance = binance_spot.StakingApi(binance_spot.ApiClient(configuration))
product = 'product_example' # str | * `STAKING` - for Locked Staking * `F_DEFI` - for flexible DeFi Staking * `L_DEFI` - for locked DeFi Staking
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
product_id = 'product_id_example' # str |  (optional)
asset = 'asset_example' # str |  (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Staking Product Position (USER_DATA)
    api_response = api_instance.sapi_v1_staking_position_get(product, timestamp, signature, product_id=product_id, asset=asset, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->sapi_v1_staking_position_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| * &#x60;STAKING&#x60; - for Locked Staking * &#x60;F_DEFI&#x60; - for flexible DeFi Staking * &#x60;L_DEFI&#x60; - for locked DeFi Staking | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **product_id** | **str**|  | [optional] 
 **asset** | **str**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200134]**](InlineResponse200134.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_staking_product_list_get**
> list[InlineResponse200132] sapi_v1_staking_product_list_get(product, timestamp, signature, asset=asset, current=current, size=size, recv_window=recv_window)

Get Staking Product List (USER_DATA)

Get available Staking product list.  Weight(IP): 1

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
api_instance = binance_spot.StakingApi(binance_spot.ApiClient(configuration))
product = 'product_example' # str | * `STAKING` - for Locked Staking * `F_DEFI` - for flexible DeFi Staking * `L_DEFI` - for locked DeFi Staking
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Staking Product List (USER_DATA)
    api_response = api_instance.sapi_v1_staking_product_list_get(product, timestamp, signature, asset=asset, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->sapi_v1_staking_product_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| * &#x60;STAKING&#x60; - for Locked Staking * &#x60;F_DEFI&#x60; - for flexible DeFi Staking * &#x60;L_DEFI&#x60; - for locked DeFi Staking | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200132]**](InlineResponse200132.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_staking_purchase_post**
> InlineResponse200133 sapi_v1_staking_purchase_post(product, product_id, amount, timestamp, signature, renewable=renewable, recv_window=recv_window)

Purchase Staking Product (USER_DATA)

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
api_instance = binance_spot.StakingApi(binance_spot.ApiClient(configuration))
product = 'product_example' # str | * `STAKING` - for Locked Staking * `F_DEFI` - for flexible DeFi Staking * `L_DEFI` - for locked DeFi Staking
product_id = 'product_id_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
renewable = 'renewable_example' # str | true or false, default false. Active if product is `STAKING` or `L_DEFI` (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Purchase Staking Product (USER_DATA)
    api_response = api_instance.sapi_v1_staking_purchase_post(product, product_id, amount, timestamp, signature, renewable=renewable, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->sapi_v1_staking_purchase_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| * &#x60;STAKING&#x60; - for Locked Staking * &#x60;F_DEFI&#x60; - for flexible DeFi Staking * &#x60;L_DEFI&#x60; - for locked DeFi Staking | 
 **product_id** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **renewable** | **str**| true or false, default false. Active if product is &#x60;STAKING&#x60; or &#x60;L_DEFI&#x60; | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200133**](InlineResponse200133.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_staking_redeem_post**
> InlineResponse20054 sapi_v1_staking_redeem_post(product, product_id, timestamp, signature, position_id=position_id, amount=amount, recv_window=recv_window)

Redeem Staking Product (USER_DATA)

Redeem Staking product. Locked staking and Locked DeFI staking belong to early redemption, redeeming in advance will result in loss of interest that you have earned.  Weight(IP): 1

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
api_instance = binance_spot.StakingApi(binance_spot.ApiClient(configuration))
product = 'product_example' # str | * `STAKING` - for Locked Staking * `F_DEFI` - for flexible DeFi Staking * `L_DEFI` - for locked DeFi Staking
product_id = 'product_id_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
position_id = 'position_id_example' # str | Mandatory if product is `STAKING` or `L_DEFI` (optional)
amount = 1.2 # float | Mandatory if product is `F_DEFI` (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Redeem Staking Product (USER_DATA)
    api_response = api_instance.sapi_v1_staking_redeem_post(product, product_id, timestamp, signature, position_id=position_id, amount=amount, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->sapi_v1_staking_redeem_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| * &#x60;STAKING&#x60; - for Locked Staking * &#x60;F_DEFI&#x60; - for flexible DeFi Staking * &#x60;L_DEFI&#x60; - for locked DeFi Staking | 
 **product_id** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **position_id** | **str**| Mandatory if product is &#x60;STAKING&#x60; or &#x60;L_DEFI&#x60; | [optional] 
 **amount** | **float**| Mandatory if product is &#x60;F_DEFI&#x60; | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_staking_set_auto_staking_post**
> InlineResponse20054 sapi_v1_staking_set_auto_staking_post(product, position_id, renewable, timestamp, signature, recv_window=recv_window)

Set Auto Staking (USER_DATA)

Set auto staking on Locked Staking or Locked DeFi Staking  Weight(IP): 1

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
api_instance = binance_spot.StakingApi(binance_spot.ApiClient(configuration))
product = 'product_example' # str | * `STAKING` - for Locked Staking * `L_DEFI` - for locked DeFi Staking
position_id = 'position_id_example' # str | 
renewable = 'renewable_example' # str | true or false
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Set Auto Staking (USER_DATA)
    api_response = api_instance.sapi_v1_staking_set_auto_staking_post(product, position_id, renewable, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->sapi_v1_staking_set_auto_staking_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| * &#x60;STAKING&#x60; - for Locked Staking * &#x60;L_DEFI&#x60; - for locked DeFi Staking | 
 **position_id** | **str**|  | 
 **renewable** | **str**| true or false | 
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

# **sapi_v1_staking_staking_record_get**
> list[InlineResponse200135] sapi_v1_staking_staking_record_get(product, txn_type, timestamp, signature, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Staking History (USER_DATA)

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
api_instance = binance_spot.StakingApi(binance_spot.ApiClient(configuration))
product = 'product_example' # str | * `STAKING` - for Locked Staking * `F_DEFI` - for flexible DeFi Staking * `L_DEFI` - for locked DeFi Staking
txn_type = 'txn_type_example' # str | `SUBSCRIPTION`, `REDEMPTION`, `INTEREST`
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Staking History (USER_DATA)
    api_response = api_instance.sapi_v1_staking_staking_record_get(product, txn_type, timestamp, signature, asset=asset, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StakingApi->sapi_v1_staking_staking_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| * &#x60;STAKING&#x60; - for Locked Staking * &#x60;F_DEFI&#x60; - for flexible DeFi Staking * &#x60;L_DEFI&#x60; - for locked DeFi Staking | 
 **txn_type** | **str**| &#x60;SUBSCRIPTION&#x60;, &#x60;REDEMPTION&#x60;, &#x60;INTEREST&#x60; | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200135]**](InlineResponse200135.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

