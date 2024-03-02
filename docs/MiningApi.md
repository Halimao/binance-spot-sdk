# binance_spot.MiningApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_mining_hash_transfer_config_cancel_post**](MiningApi.md#sapi_v1_mining_hash_transfer_config_cancel_post) | **POST** /sapi/v1/mining/hash-transfer/config/cancel | Cancel Hashrate Resale configuration (USER_DATA)
[**sapi_v1_mining_hash_transfer_config_details_list_get**](MiningApi.md#sapi_v1_mining_hash_transfer_config_details_list_get) | **GET** /sapi/v1/mining/hash-transfer/config/details/list | Hashrate Resale List (USER_DATA)
[**sapi_v1_mining_hash_transfer_config_post**](MiningApi.md#sapi_v1_mining_hash_transfer_config_post) | **POST** /sapi/v1/mining/hash-transfer/config | Hashrate Resale Request (USER_DATA)
[**sapi_v1_mining_hash_transfer_profit_details_get**](MiningApi.md#sapi_v1_mining_hash_transfer_profit_details_get) | **GET** /sapi/v1/mining/hash-transfer/profit/details | Hashrate Resale Details (USER_DATA)
[**sapi_v1_mining_payment_list_get**](MiningApi.md#sapi_v1_mining_payment_list_get) | **GET** /sapi/v1/mining/payment/list | Earnings List (USER_DATA)
[**sapi_v1_mining_payment_other_get**](MiningApi.md#sapi_v1_mining_payment_other_get) | **GET** /sapi/v1/mining/payment/other | Extra Bonus List (USER_DATA)
[**sapi_v1_mining_payment_uid_get**](MiningApi.md#sapi_v1_mining_payment_uid_get) | **GET** /sapi/v1/mining/payment/uid | Mining Account Earning (USER_DATA)
[**sapi_v1_mining_pub_algo_list_get**](MiningApi.md#sapi_v1_mining_pub_algo_list_get) | **GET** /sapi/v1/mining/pub/algoList | Acquiring Algorithm (MARKET_DATA)
[**sapi_v1_mining_pub_coin_list_get**](MiningApi.md#sapi_v1_mining_pub_coin_list_get) | **GET** /sapi/v1/mining/pub/coinList | Acquiring CoinName (MARKET_DATA)
[**sapi_v1_mining_statistics_user_list_get**](MiningApi.md#sapi_v1_mining_statistics_user_list_get) | **GET** /sapi/v1/mining/statistics/user/list | Account List (USER_DATA)
[**sapi_v1_mining_statistics_user_status_get**](MiningApi.md#sapi_v1_mining_statistics_user_status_get) | **GET** /sapi/v1/mining/statistics/user/status | Statistic List (USER_DATA)
[**sapi_v1_mining_worker_detail_get**](MiningApi.md#sapi_v1_mining_worker_detail_get) | **GET** /sapi/v1/mining/worker/detail | Request for Detail Miner List (USER_DATA)
[**sapi_v1_mining_worker_list_get**](MiningApi.md#sapi_v1_mining_worker_list_get) | **GET** /sapi/v1/mining/worker/list | Request for Miner List (USER_DATA)

# **sapi_v1_mining_hash_transfer_config_cancel_post**
> InlineResponse200146 sapi_v1_mining_hash_transfer_config_cancel_post(config_id, user_name, timestamp, signature, recv_window=recv_window)

Cancel Hashrate Resale configuration (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
config_id = 'config_id_example' # str | Mining ID
user_name = 'user_name_example' # str | Mining Account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Cancel Hashrate Resale configuration (USER_DATA)
    api_response = api_instance.sapi_v1_mining_hash_transfer_config_cancel_post(config_id, user_name, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_hash_transfer_config_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| Mining ID | 
 **user_name** | **str**| Mining Account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200146**](InlineResponse200146.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_hash_transfer_config_details_list_get**
> InlineResponse200143 sapi_v1_mining_hash_transfer_config_details_list_get(timestamp, signature, page_index=page_index, page_size=page_size, recv_window=recv_window)

Hashrate Resale List (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
page_index = 56 # int | Page number, default is first page, start form 1 (optional)
page_size = 'page_size_example' # str | Number of pages, minimum 10, maximum 200 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Hashrate Resale List (USER_DATA)
    api_response = api_instance.sapi_v1_mining_hash_transfer_config_details_list_get(timestamp, signature, page_index=page_index, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_hash_transfer_config_details_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **page_index** | **int**| Page number, default is first page, start form 1 | [optional] 
 **page_size** | **str**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200143**](InlineResponse200143.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_hash_transfer_config_post**
> InlineResponse200145 sapi_v1_mining_hash_transfer_config_post(user_name, algo, to_pool_user, hash_rate, timestamp, signature, start_date=start_date, end_date=end_date, recv_window=recv_window)

Hashrate Resale Request (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
user_name = 'user_name_example' # str | Mining Account
algo = 'algo_example' # str | Algorithm(sha256)
to_pool_user = 'to_pool_user_example' # str | Mining Account
hash_rate = 'hash_rate_example' # str | Resale hashrate h/s must be transferred (BTC is greater than 500000000000 ETH is greater than 500000)
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_date = 'start_date_example' # str | Search date, millisecond timestamp, while empty query all (optional)
end_date = 'end_date_example' # str | Search date, millisecond timestamp, while empty query all (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Hashrate Resale Request (USER_DATA)
    api_response = api_instance.sapi_v1_mining_hash_transfer_config_post(user_name, algo, to_pool_user, hash_rate, timestamp, signature, start_date=start_date, end_date=end_date, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_hash_transfer_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| Mining Account | 
 **algo** | **str**| Algorithm(sha256) | 
 **to_pool_user** | **str**| Mining Account | 
 **hash_rate** | **str**| Resale hashrate h/s must be transferred (BTC is greater than 500000000000 ETH is greater than 500000) | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_date** | **str**| Search date, millisecond timestamp, while empty query all | [optional] 
 **end_date** | **str**| Search date, millisecond timestamp, while empty query all | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200145**](InlineResponse200145.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_hash_transfer_profit_details_get**
> InlineResponse200144 sapi_v1_mining_hash_transfer_profit_details_get(config_id, user_name, timestamp, signature, page_index=page_index, page_size=page_size, recv_window=recv_window)

Hashrate Resale Details (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
config_id = 'config_id_example' # str | Mining ID
user_name = 'user_name_example' # str | Mining Account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
page_index = 56 # int | Page number, default is first page, start form 1 (optional)
page_size = 'page_size_example' # str | Number of pages, minimum 10, maximum 200 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Hashrate Resale Details (USER_DATA)
    api_response = api_instance.sapi_v1_mining_hash_transfer_profit_details_get(config_id, user_name, timestamp, signature, page_index=page_index, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_hash_transfer_profit_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| Mining ID | 
 **user_name** | **str**| Mining Account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **page_index** | **int**| Page number, default is first page, start form 1 | [optional] 
 **page_size** | **str**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200144**](InlineResponse200144.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_payment_list_get**
> InlineResponse200141 sapi_v1_mining_payment_list_get(algo, user_name, timestamp, signature, coin=coin, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)

Earnings List (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
algo = 'algo_example' # str | Algorithm(sha256)
user_name = 'user_name_example' # str | Mining Account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
coin = 'coin_example' # str | Coin name (optional)
start_date = 'start_date_example' # str | Search date, millisecond timestamp, while empty query all (optional)
end_date = 'end_date_example' # str | Search date, millisecond timestamp, while empty query all (optional)
page_index = 56 # int | Page number, default is first page, start form 1 (optional)
page_size = 'page_size_example' # str | Number of pages, minimum 10, maximum 200 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Earnings List (USER_DATA)
    api_response = api_instance.sapi_v1_mining_payment_list_get(algo, user_name, timestamp, signature, coin=coin, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_payment_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | 
 **user_name** | **str**| Mining Account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **coin** | **str**| Coin name | [optional] 
 **start_date** | **str**| Search date, millisecond timestamp, while empty query all | [optional] 
 **end_date** | **str**| Search date, millisecond timestamp, while empty query all | [optional] 
 **page_index** | **int**| Page number, default is first page, start form 1 | [optional] 
 **page_size** | **str**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200141**](InlineResponse200141.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_payment_other_get**
> InlineResponse200142 sapi_v1_mining_payment_other_get(algo, user_name, timestamp, signature, coin=coin, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)

Extra Bonus List (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
algo = 'algo_example' # str | Algorithm(sha256)
user_name = 'user_name_example' # str | Mining Account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
coin = 'coin_example' # str | Coin name (optional)
start_date = 'start_date_example' # str | Search date, millisecond timestamp, while empty query all (optional)
end_date = 'end_date_example' # str | Search date, millisecond timestamp, while empty query all (optional)
page_index = 56 # int | Page number, default is first page, start form 1 (optional)
page_size = 'page_size_example' # str | Number of pages, minimum 10, maximum 200 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Extra Bonus List (USER_DATA)
    api_response = api_instance.sapi_v1_mining_payment_other_get(algo, user_name, timestamp, signature, coin=coin, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_payment_other_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | 
 **user_name** | **str**| Mining Account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **coin** | **str**| Coin name | [optional] 
 **start_date** | **str**| Search date, millisecond timestamp, while empty query all | [optional] 
 **end_date** | **str**| Search date, millisecond timestamp, while empty query all | [optional] 
 **page_index** | **int**| Page number, default is first page, start form 1 | [optional] 
 **page_size** | **str**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200142**](InlineResponse200142.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_payment_uid_get**
> InlineResponse200149 sapi_v1_mining_payment_uid_get(algo, timestamp, signature, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)

Mining Account Earning (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
algo = 'algo_example' # str | Algorithm(sha256)
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_date = 'start_date_example' # str | Search date, millisecond timestamp, while empty query all (optional)
end_date = 'end_date_example' # str | Search date, millisecond timestamp, while empty query all (optional)
page_index = 56 # int | Page number, default is first page, start form 1 (optional)
page_size = 'page_size_example' # str | Number of pages, minimum 10, maximum 200 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Mining Account Earning (USER_DATA)
    api_response = api_instance.sapi_v1_mining_payment_uid_get(algo, timestamp, signature, start_date=start_date, end_date=end_date, page_index=page_index, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_payment_uid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_date** | **str**| Search date, millisecond timestamp, while empty query all | [optional] 
 **end_date** | **str**| Search date, millisecond timestamp, while empty query all | [optional] 
 **page_index** | **int**| Page number, default is first page, start form 1 | [optional] 
 **page_size** | **str**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200149**](InlineResponse200149.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_pub_algo_list_get**
> InlineResponse200137 sapi_v1_mining_pub_algo_list_get()

Acquiring Algorithm (MARKET_DATA)

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))

try:
    # Acquiring Algorithm (MARKET_DATA)
    api_response = api_instance.sapi_v1_mining_pub_algo_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_pub_algo_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200137**](InlineResponse200137.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_pub_coin_list_get**
> InlineResponse200138 sapi_v1_mining_pub_coin_list_get()

Acquiring CoinName (MARKET_DATA)

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))

try:
    # Acquiring CoinName (MARKET_DATA)
    api_response = api_instance.sapi_v1_mining_pub_coin_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_pub_coin_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200138**](InlineResponse200138.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_statistics_user_list_get**
> InlineResponse200148 sapi_v1_mining_statistics_user_list_get(algo, user_name, timestamp, signature, recv_window=recv_window)

Account List (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
algo = 'algo_example' # str | Algorithm(sha256)
user_name = 'user_name_example' # str | Mining Account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Account List (USER_DATA)
    api_response = api_instance.sapi_v1_mining_statistics_user_list_get(algo, user_name, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_statistics_user_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | 
 **user_name** | **str**| Mining Account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200148**](InlineResponse200148.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_statistics_user_status_get**
> InlineResponse200147 sapi_v1_mining_statistics_user_status_get(algo, user_name, timestamp, signature, recv_window=recv_window)

Statistic List (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
algo = 'algo_example' # str | Algorithm(sha256)
user_name = 'user_name_example' # str | Mining Account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Statistic List (USER_DATA)
    api_response = api_instance.sapi_v1_mining_statistics_user_status_get(algo, user_name, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_statistics_user_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | 
 **user_name** | **str**| Mining Account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200147**](InlineResponse200147.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_worker_detail_get**
> InlineResponse200139 sapi_v1_mining_worker_detail_get(algo, user_name, worker_name, timestamp, signature, recv_window=recv_window)

Request for Detail Miner List (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
algo = 'algo_example' # str | Algorithm(sha256)
user_name = 'user_name_example' # str | Mining Account
worker_name = 'worker_name_example' # str | Miner’s name
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Request for Detail Miner List (USER_DATA)
    api_response = api_instance.sapi_v1_mining_worker_detail_get(algo, user_name, worker_name, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_worker_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | 
 **user_name** | **str**| Mining Account | 
 **worker_name** | **str**| Miner’s name | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200139**](InlineResponse200139.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_mining_worker_list_get**
> InlineResponse200140 sapi_v1_mining_worker_list_get(algo, user_name, timestamp, signature, page_index=page_index, sort=sort, sort_column=sort_column, worker_status=worker_status, recv_window=recv_window)

Request for Miner List (USER_DATA)

Weight(IP): 5

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
api_instance = binance_spot.MiningApi(binance_spot.ApiClient(configuration))
algo = 'algo_example' # str | Algorithm(sha256)
user_name = 'user_name_example' # str | Mining Account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
page_index = 56 # int | Page number, default is first page, start form 1 (optional)
sort = 56 # int | sort sequence(default=0)0 positive sequence, 1 negative sequence (optional)
sort_column = 56 # int | Sort by( default 1): 1: miner name, 2: real-time computing power, 3: daily average computing power, 4: real-time rejection rate, 5: last submission time (optional)
worker_status = 56 # int | miners status(default=0)0 all, 1 valid, 2 invalid, 3 failure (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Request for Miner List (USER_DATA)
    api_response = api_instance.sapi_v1_mining_worker_list_get(algo, user_name, timestamp, signature, page_index=page_index, sort=sort, sort_column=sort_column, worker_status=worker_status, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiningApi->sapi_v1_mining_worker_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo** | **str**| Algorithm(sha256) | 
 **user_name** | **str**| Mining Account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **page_index** | **int**| Page number, default is first page, start form 1 | [optional] 
 **sort** | **int**| sort sequence(default&#x3D;0)0 positive sequence, 1 negative sequence | [optional] 
 **sort_column** | **int**| Sort by( default 1): 1: miner name, 2: real-time computing power, 3: daily average computing power, 4: real-time rejection rate, 5: last submission time | [optional] 
 **worker_status** | **int**| miners status(default&#x3D;0)0 all, 1 valid, 2 invalid, 3 failure | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200140**](InlineResponse200140.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

