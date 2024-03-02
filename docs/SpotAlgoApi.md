# binance_spot.SpotAlgoApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_algo_spot_historical_orders_get**](SpotAlgoApi.md#sapi_v1_algo_spot_historical_orders_get) | **GET** /sapi/v1/algo/spot/historicalOrders | Query Historical Algo Orders
[**sapi_v1_algo_spot_new_order_twap_post**](SpotAlgoApi.md#sapi_v1_algo_spot_new_order_twap_post) | **POST** /sapi/v1/algo/spot/newOrderTwap | Time-Weighted Average Price (Twap) New Order
[**sapi_v1_algo_spot_open_orders_get**](SpotAlgoApi.md#sapi_v1_algo_spot_open_orders_get) | **GET** /sapi/v1/algo/spot/openOrders | Query Current Algo Open Orders
[**sapi_v1_algo_spot_order_delete**](SpotAlgoApi.md#sapi_v1_algo_spot_order_delete) | **DELETE** /sapi/v1/algo/spot/order | Cancel Algo Order
[**sapi_v1_algo_spot_sub_orders_get**](SpotAlgoApi.md#sapi_v1_algo_spot_sub_orders_get) | **GET** /sapi/v1/algo/spot/subOrders | Query Sub Orders

# **sapi_v1_algo_spot_historical_orders_get**
> InlineResponse200161 sapi_v1_algo_spot_historical_orders_get(symbol, side, timestamp, signature, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)

Query Historical Algo Orders

Get all historical SPOT TWAP orders  Weight(IP): 1

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
api_instance = binance_spot.SpotAlgoApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
page_size = 'page_size_example' # str | Number of pages, minimum 10, maximum 200 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Historical Algo Orders
    api_response = api_instance.sapi_v1_algo_spot_historical_orders_get(symbol, side, timestamp, signature, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpotAlgoApi->sapi_v1_algo_spot_historical_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **page_size** | **str**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200161**](InlineResponse200161.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_spot_new_order_twap_post**
> InlineResponse200158 sapi_v1_algo_spot_new_order_twap_post(symbol, side, quantity, duration, timestamp, signature, client_algo_id=client_algo_id, limit_price=limit_price, recv_window=recv_window)

Time-Weighted Average Price (Twap) New Order

Place a new spot TWAP order with Algo service.  Weight(UID): 3000

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
api_instance = binance_spot.SpotAlgoApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
quantity = 1.2 # float | 
duration = 56 # int | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
client_algo_id = 'client_algo_id_example' # str |  (optional)
limit_price = 3.4 # float |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Time-Weighted Average Price (Twap) New Order
    api_response = api_instance.sapi_v1_algo_spot_new_order_twap_post(symbol, side, quantity, duration, timestamp, signature, client_algo_id=client_algo_id, limit_price=limit_price, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpotAlgoApi->sapi_v1_algo_spot_new_order_twap_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **quantity** | **float**|  | 
 **duration** | **int**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **client_algo_id** | **str**|  | [optional] 
 **limit_price** | **float**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200158**](InlineResponse200158.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_spot_open_orders_get**
> InlineResponse200160 sapi_v1_algo_spot_open_orders_get(timestamp, signature, recv_window=recv_window)

Query Current Algo Open Orders

Get all open SPOT TWAP orders  Weight(IP): 1

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
api_instance = binance_spot.SpotAlgoApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Current Algo Open Orders
    api_response = api_instance.sapi_v1_algo_spot_open_orders_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpotAlgoApi->sapi_v1_algo_spot_open_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200160**](InlineResponse200160.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_spot_order_delete**
> InlineResponse200159 sapi_v1_algo_spot_order_delete(algo_id, timestamp, signature, recv_window=recv_window)

Cancel Algo Order

Cancel an open TWAP order  Weight(IP): 1

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
api_instance = binance_spot.SpotAlgoApi(binance_spot.ApiClient(configuration))
algo_id = 789 # int | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Cancel Algo Order
    api_response = api_instance.sapi_v1_algo_spot_order_delete(algo_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpotAlgoApi->sapi_v1_algo_spot_order_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_id** | **int**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200159**](InlineResponse200159.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_spot_sub_orders_get**
> InlineResponse200162 sapi_v1_algo_spot_sub_orders_get(algo_id, timestamp, signature, page=page, page_size=page_size, recv_window=recv_window)

Query Sub Orders

Get respective sub orders for a specified algoId  Weight(IP): 1

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
api_instance = binance_spot.SpotAlgoApi(binance_spot.ApiClient(configuration))
algo_id = 789 # int | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
page = 56 # int | Default 1 (optional)
page_size = 'page_size_example' # str | Number of pages, minimum 10, maximum 200 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Sub Orders
    api_response = api_instance.sapi_v1_algo_spot_sub_orders_get(algo_id, timestamp, signature, page=page, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpotAlgoApi->sapi_v1_algo_spot_sub_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_id** | **int**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **page** | **int**| Default 1 | [optional] 
 **page_size** | **str**| Number of pages, minimum 10, maximum 200 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200162**](InlineResponse200162.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

