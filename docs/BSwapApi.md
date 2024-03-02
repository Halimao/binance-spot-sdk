# binance_spot.BSwapApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_bswap_add_liquidity_preview_get**](BSwapApi.md#sapi_v1_bswap_add_liquidity_preview_get) | **GET** /sapi/v1/bswap/addLiquidityPreview | Add Liquidity Preview (USER_DATA)
[**sapi_v1_bswap_claim_rewards_post**](BSwapApi.md#sapi_v1_bswap_claim_rewards_post) | **POST** /sapi/v1/bswap/claimRewards | Claim rewards (TRADE)
[**sapi_v1_bswap_claimed_history_get**](BSwapApi.md#sapi_v1_bswap_claimed_history_get) | **GET** /sapi/v1/bswap/claimedHistory | Get Claimed History (USER_DATA)
[**sapi_v1_bswap_liquidity_add_post**](BSwapApi.md#sapi_v1_bswap_liquidity_add_post) | **POST** /sapi/v1/bswap/liquidityAdd | Add Liquidity (TRADE)
[**sapi_v1_bswap_liquidity_get**](BSwapApi.md#sapi_v1_bswap_liquidity_get) | **GET** /sapi/v1/bswap/liquidity | Liquidity information of a pool (USER_DATA)
[**sapi_v1_bswap_liquidity_ops_get**](BSwapApi.md#sapi_v1_bswap_liquidity_ops_get) | **GET** /sapi/v1/bswap/liquidityOps | Liquidity Operation Record (USER_DATA)
[**sapi_v1_bswap_liquidity_remove_post**](BSwapApi.md#sapi_v1_bswap_liquidity_remove_post) | **POST** /sapi/v1/bswap/liquidityRemove | Remove Liquidity (TRADE)
[**sapi_v1_bswap_pool_configure_get**](BSwapApi.md#sapi_v1_bswap_pool_configure_get) | **GET** /sapi/v1/bswap/poolConfigure | Pool Configure (USER_DATA)
[**sapi_v1_bswap_pools_get**](BSwapApi.md#sapi_v1_bswap_pools_get) | **GET** /sapi/v1/bswap/pools | List All Swap Pools (MARKET_DATA)
[**sapi_v1_bswap_quote_get**](BSwapApi.md#sapi_v1_bswap_quote_get) | **GET** /sapi/v1/bswap/quote | Request Quote (USER_DATA)
[**sapi_v1_bswap_remove_liquidity_preview_get**](BSwapApi.md#sapi_v1_bswap_remove_liquidity_preview_get) | **GET** /sapi/v1/bswap/removeLiquidityPreview | Remove Liquidity Preview (USER_DATA)
[**sapi_v1_bswap_swap_get**](BSwapApi.md#sapi_v1_bswap_swap_get) | **GET** /sapi/v1/bswap/swap | Swap History (USER_DATA)
[**sapi_v1_bswap_swap_post**](BSwapApi.md#sapi_v1_bswap_swap_post) | **POST** /sapi/v1/bswap/swap | Swap (TRADE)
[**sapi_v1_bswap_unclaimed_rewards_get**](BSwapApi.md#sapi_v1_bswap_unclaimed_rewards_get) | **GET** /sapi/v1/bswap/unclaimedRewards | Get Unclaimed Rewards Record (USER_DATA)

# **sapi_v1_bswap_add_liquidity_preview_get**
> InlineResponse200186 sapi_v1_bswap_add_liquidity_preview_get(pool_id, type, quote_asset, quote_qty, timestamp, signature, recv_window=recv_window)

Add Liquidity Preview (USER_DATA)

Calculate expected share amount for adding liquidity in single or dual token.  Weight(IP): 150

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
pool_id = 789 # int | 
type = 'type_example' # str | * `SINGLE` - for adding a single token * `COMBINATION` - for adding dual tokens
quote_asset = 'quote_asset_example' # str | 
quote_qty = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Add Liquidity Preview (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_add_liquidity_preview_get(pool_id, type, quote_asset, quote_qty, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_add_liquidity_preview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**|  | 
 **type** | **str**| * &#x60;SINGLE&#x60; - for adding a single token * &#x60;COMBINATION&#x60; - for adding dual tokens | 
 **quote_asset** | **str**|  | 
 **quote_qty** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200186**](InlineResponse200186.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_claim_rewards_post**
> InlineResponse200189 sapi_v1_bswap_claim_rewards_post(timestamp, signature, type=type, recv_window=recv_window)

Claim rewards (TRADE)

Claim swap rewards or liquidity rewards  Weight(UID): 1000

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
type = 56 # int | 0: Swap rewards, 1: Liquidity rewards, default to 0 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Claim rewards (TRADE)
    api_response = api_instance.sapi_v1_bswap_claim_rewards_post(timestamp, signature, type=type, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_claim_rewards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **type** | **int**| 0: Swap rewards, 1: Liquidity rewards, default to 0 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200189**](InlineResponse200189.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_claimed_history_get**
> list[InlineResponse200190] sapi_v1_bswap_claimed_history_get(timestamp, signature, pool_id=pool_id, asset_rewards=asset_rewards, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Claimed History (USER_DATA)

Get history of claimed rewards.  Weight(UID): 1000

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
pool_id = 789 # int |  (optional)
asset_rewards = 'asset_rewards_example' # str |  (optional)
type = 56 # int | 0: Swap rewards, 1: Liquidity rewards, default to 0 (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 3, max 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Claimed History (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_claimed_history_get(timestamp, signature, pool_id=pool_id, asset_rewards=asset_rewards, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_claimed_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **pool_id** | **int**|  | [optional] 
 **asset_rewards** | **str**|  | [optional] 
 **type** | **int**| 0: Swap rewards, 1: Liquidity rewards, default to 0 | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 3, max 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200190]**](InlineResponse200190.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_liquidity_add_post**
> InlineResponse200180 sapi_v1_bswap_liquidity_add_post(pool_id, asset, quantity, timestamp, signature, type=type, recv_window=recv_window)

Add Liquidity (TRADE)

Add liquidity to a pool.  Weight(UID): 1000 (Additional: 3 times one second)

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
pool_id = 789 # int | 
asset = 'asset_example' # str | 
quantity = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
type = 'type_example' # str | * `Single` - to add a single token * `Combination` - to add dual tokens (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Add Liquidity (TRADE)
    api_response = api_instance.sapi_v1_bswap_liquidity_add_post(pool_id, asset, quantity, timestamp, signature, type=type, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_liquidity_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**|  | 
 **asset** | **str**|  | 
 **quantity** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **type** | **str**| * &#x60;Single&#x60; - to add a single token * &#x60;Combination&#x60; - to add dual tokens | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200180**](InlineResponse200180.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_liquidity_get**
> list[InlineResponse200179] sapi_v1_bswap_liquidity_get(timestamp, signature, pool_id=pool_id, recv_window=recv_window)

Liquidity information of a pool (USER_DATA)

Get liquidity information and user share of a pool.  Weight(IP): - `1` for one pool; - `10` when the poolId parameter is omitted;

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
pool_id = 789 # int |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Liquidity information of a pool (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_liquidity_get(timestamp, signature, pool_id=pool_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_liquidity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **pool_id** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200179]**](InlineResponse200179.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_liquidity_ops_get**
> list[InlineResponse200181] sapi_v1_bswap_liquidity_ops_get(timestamp, signature, operation_id=operation_id, pool_id=pool_id, operation=operation, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Liquidity Operation Record (USER_DATA)

Get liquidity operation (add/remove) records.  Weight(UID): 3000

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
operation_id = 789 # int |  (optional)
pool_id = 789 # int |  (optional)
operation = 'operation_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Liquidity Operation Record (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_liquidity_ops_get(timestamp, signature, operation_id=operation_id, pool_id=pool_id, operation=operation, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_liquidity_ops_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **operation_id** | **int**|  | [optional] 
 **pool_id** | **int**|  | [optional] 
 **operation** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200181]**](InlineResponse200181.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_liquidity_remove_post**
> InlineResponse200180 sapi_v1_bswap_liquidity_remove_post(pool_id, type, share_amount, timestamp, signature, asset=asset, recv_window=recv_window)

Remove Liquidity (TRADE)

Remove liquidity from a pool, `type` include `SINGLE` and `COMBINATION`, asset is mandatory for single asset removal  Weight(UID): 1000 (Additional: 3 times one second)

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
pool_id = 789 # int | 
type = 'type_example' # str | * `SINGLE` - for single asset removal * `COMBINATION` - for combination of all coins removal
share_amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str | Mandatory for single asset removal (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Remove Liquidity (TRADE)
    api_response = api_instance.sapi_v1_bswap_liquidity_remove_post(pool_id, type, share_amount, timestamp, signature, asset=asset, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_liquidity_remove_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**|  | 
 **type** | **str**| * &#x60;SINGLE&#x60; - for single asset removal * &#x60;COMBINATION&#x60; - for combination of all coins removal | 
 **share_amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**| Mandatory for single asset removal | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200180**](InlineResponse200180.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_pool_configure_get**
> list[InlineResponse200185] sapi_v1_bswap_pool_configure_get(timestamp, signature, pool_id=pool_id, recv_window=recv_window)

Pool Configure (USER_DATA)

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
pool_id = 789 # int |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Pool Configure (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_pool_configure_get(timestamp, signature, pool_id=pool_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_pool_configure_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **pool_id** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200185]**](InlineResponse200185.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_pools_get**
> list[InlineResponse200178] sapi_v1_bswap_pools_get()

List All Swap Pools (MARKET_DATA)

Get metadata about all swap pools.  Weight(IP): 1

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))

try:
    # List All Swap Pools (MARKET_DATA)
    api_response = api_instance.sapi_v1_bswap_pools_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_pools_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200178]**](InlineResponse200178.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_quote_get**
> InlineResponse200182 sapi_v1_bswap_quote_get(quote_asset, base_asset, quote_qty, timestamp, signature, recv_window=recv_window)

Request Quote (USER_DATA)

Request a quote for swap quote asset (selling asset) for base asset (buying asset), essentially price/exchange rates.  quoteQty is quantity of quote asset (to sell).  Please be noted the quote is for reference only, the actual price will change as the liquidity changes, it's recommended to swap immediate after request a quote for slippage prevention.  Weight(UID): 150

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
quote_asset = 'quote_asset_example' # str | 
base_asset = 'base_asset_example' # str | 
quote_qty = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Request Quote (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_quote_get(quote_asset, base_asset, quote_qty, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_quote_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_asset** | **str**|  | 
 **base_asset** | **str**|  | 
 **quote_qty** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200182**](InlineResponse200182.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_remove_liquidity_preview_get**
> InlineResponse200187 sapi_v1_bswap_remove_liquidity_preview_get(pool_id, type, quote_asset, share_amount, timestamp, signature, recv_window=recv_window)

Remove Liquidity Preview (USER_DATA)

Calculate the expected asset amount of single token redemption or dual token redemption.  Weight(IP): 150

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
pool_id = 789 # int | 
type = 'type_example' # str | * `SINGLE` - remove and obtain a single token * `COMBINATION` - remove and obtain dual token
quote_asset = 'quote_asset_example' # str | 
share_amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Remove Liquidity Preview (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_remove_liquidity_preview_get(pool_id, type, quote_asset, share_amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_remove_liquidity_preview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **int**|  | 
 **type** | **str**| * &#x60;SINGLE&#x60; - remove and obtain a single token * &#x60;COMBINATION&#x60; - remove and obtain dual token | 
 **quote_asset** | **str**|  | 
 **share_amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200187**](InlineResponse200187.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_swap_get**
> list[InlineResponse200183] sapi_v1_bswap_swap_get(timestamp, signature, swap_id=swap_id, start_time=start_time, end_time=end_time, status=status, quote_asset=quote_asset, base_asset=base_asset, limit=limit, recv_window=recv_window)

Swap History (USER_DATA)

Get swap history.  Weight(UID): 3000

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
swap_id = 789 # int |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
status = 56 # int | * `0` - pending for swap * `1` - success * `2` - failed (optional)
quote_asset = 'quote_asset_example' # str |  (optional)
base_asset = 'base_asset_example' # str |  (optional)
limit = 56 # int | default 3, max 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Swap History (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_swap_get(timestamp, signature, swap_id=swap_id, start_time=start_time, end_time=end_time, status=status, quote_asset=quote_asset, base_asset=base_asset, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_swap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **swap_id** | **int**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **status** | **int**| * &#x60;0&#x60; - pending for swap * &#x60;1&#x60; - success * &#x60;2&#x60; - failed | [optional] 
 **quote_asset** | **str**|  | [optional] 
 **base_asset** | **str**|  | [optional] 
 **limit** | **int**| default 3, max 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200183]**](InlineResponse200183.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_swap_post**
> InlineResponse200184 sapi_v1_bswap_swap_post(quote_asset, base_asset, quote_qty, timestamp, signature, recv_window=recv_window)

Swap (TRADE)

Swap `quoteAsset` for `baseAsset`.  Weight(UID): 1000 (Additional: 3 times one second)

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
quote_asset = 'quote_asset_example' # str | 
base_asset = 'base_asset_example' # str | 
quote_qty = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Swap (TRADE)
    api_response = api_instance.sapi_v1_bswap_swap_post(quote_asset, base_asset, quote_qty, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_swap_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_asset** | **str**|  | 
 **base_asset** | **str**|  | 
 **quote_qty** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200184**](InlineResponse200184.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bswap_unclaimed_rewards_get**
> InlineResponse200188 sapi_v1_bswap_unclaimed_rewards_get(timestamp, signature, type=type, recv_window=recv_window)

Get Unclaimed Rewards Record (USER_DATA)

Get unclaimed rewards record.  Weight(UID): 1000

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
api_instance = binance_spot.BSwapApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
type = 56 # int | 0: Swap rewards, 1: Liquidity rewards, default to 0 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Unclaimed Rewards Record (USER_DATA)
    api_response = api_instance.sapi_v1_bswap_unclaimed_rewards_get(timestamp, signature, type=type, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BSwapApi->sapi_v1_bswap_unclaimed_rewards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **type** | **int**| 0: Swap rewards, 1: Liquidity rewards, default to 0 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200188**](InlineResponse200188.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

