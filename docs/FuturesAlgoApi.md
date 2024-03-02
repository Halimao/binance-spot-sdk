# binance_spot.FuturesAlgoApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_algo_futures_historical_orders_get**](FuturesAlgoApi.md#sapi_v1_algo_futures_historical_orders_get) | **GET** /sapi/v1/algo/futures/historicalOrders | Query Historical Algo Orders (USER_DATA)
[**sapi_v1_algo_futures_new_order_twap_post**](FuturesAlgoApi.md#sapi_v1_algo_futures_new_order_twap_post) | **POST** /sapi/v1/algo/futures/newOrderTwap | Time-Weighted Average Price(Twap) New Order (TRADE)
[**sapi_v1_algo_futures_new_order_vp_post**](FuturesAlgoApi.md#sapi_v1_algo_futures_new_order_vp_post) | **POST** /sapi/v1/algo/futures/newOrderVp | Volume Participation(VP) New Order (TRADE)
[**sapi_v1_algo_futures_open_orders_get**](FuturesAlgoApi.md#sapi_v1_algo_futures_open_orders_get) | **GET** /sapi/v1/algo/futures/openOrders | Query Current Algo Open Orders (USER_DATA)
[**sapi_v1_algo_futures_order_delete**](FuturesAlgoApi.md#sapi_v1_algo_futures_order_delete) | **DELETE** /sapi/v1/algo/futures/order | Cancel Algo Order(TRADE)
[**sapi_v1_algo_futures_sub_orders_get**](FuturesAlgoApi.md#sapi_v1_algo_futures_sub_orders_get) | **GET** /sapi/v1/algo/futures/subOrders | Query Sub Orders (USER_DATA)

# **sapi_v1_algo_futures_historical_orders_get**
> InlineResponse200156 sapi_v1_algo_futures_historical_orders_get(timestamp, signature, symbol=symbol, side=side, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)

Query Historical Algo Orders (USER_DATA)

- You need to enable Futures Trading Permission for the api key which requests this endpoint. - Base URL: https://api.binance.com  Weight(IP): 1

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
api_instance = binance_spot.FuturesAlgoApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
side = 'side_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
page_size = 'page_size_example' # str | Page size, minimum 1, maximum 100, default 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Historical Algo Orders (USER_DATA)
    api_response = api_instance.sapi_v1_algo_futures_historical_orders_get(timestamp, signature, symbol=symbol, side=side, start_time=start_time, end_time=end_time, page=page, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesAlgoApi->sapi_v1_algo_futures_historical_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **side** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **page_size** | **str**| Page size, minimum 1, maximum 100, default 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200156**](InlineResponse200156.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_futures_new_order_twap_post**
> InlineResponse200153 sapi_v1_algo_futures_new_order_twap_post(symbol, side, quantity, duration, timestamp, signature, position_side=position_side, client_algo_id=client_algo_id, reduce_only=reduce_only, limit_price=limit_price, recv_window=recv_window)

Time-Weighted Average Price(Twap) New Order (TRADE)

Send in a Twap new order. Only support on USDⓈ-M Contracts.  You need to enable Futures Trading Permission for the api key which requests this endpoint. Base URL: https://api.binance.com  - Total Algo open orders max allowed: 10 orders. - Leverage of symbols and position mode will be the same as your futures account settings. You can set up through the trading page or fapi. - Receiving \"success\": true does not mean that your order will be executed. Please use the query order endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the order status. For example: Your futures balance is insufficient, or open position with reduce only or position side is inconsistent with your own setting. In these cases you will receive \"success\": true, but the order status will be expired after we check it. - quantity * 60 / duration should be larger than minQty - duration cannot be less than 5 mins or more than 24 hours. - For delivery contracts, TWAP end time should be one hour earlier than the delivery time of the symbol.  Weight(UID): 3000

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
api_instance = binance_spot.FuturesAlgoApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
quantity = 1.2 # float | Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
duration = 789 # int | Duration for TWAP orders in seconds. [300, 86400];Less than 5min => defaults to 5 min; Greater than 24h => defaults to 24h
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
position_side = 'position_side_example' # str | Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode. (optional)
client_algo_id = 'client_algo_id_example' # str | A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value (optional)
reduce_only = true # bool | 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open a position (optional)
limit_price = 1.2 # float | Limit price of the order; If it is not sent, will place order by market price by default (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Time-Weighted Average Price(Twap) New Order (TRADE)
    api_response = api_instance.sapi_v1_algo_futures_new_order_twap_post(symbol, side, quantity, duration, timestamp, signature, position_side=position_side, client_algo_id=client_algo_id, reduce_only=reduce_only, limit_price=limit_price, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesAlgoApi->sapi_v1_algo_futures_new_order_twap_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **quantity** | **float**| Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT | 
 **duration** | **int**| Duration for TWAP orders in seconds. [300, 86400];Less than 5min &#x3D;&gt; defaults to 5 min; Greater than 24h &#x3D;&gt; defaults to 24h | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **position_side** | **str**| Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode. | [optional] 
 **client_algo_id** | **str**| A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value | [optional] 
 **reduce_only** | **bool**| &#x27;true&#x27; or &#x27;false&#x27;. Default &#x27;false&#x27;; Cannot be sent in Hedge Mode; Cannot be sent when you open a position | [optional] 
 **limit_price** | **float**| Limit price of the order; If it is not sent, will place order by market price by default | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200153**](InlineResponse200153.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_futures_new_order_vp_post**
> InlineResponse200153 sapi_v1_algo_futures_new_order_vp_post(symbol, side, quantity, urgency, timestamp, signature, position_side=position_side, client_algo_id=client_algo_id, reduce_only=reduce_only, limit_price=limit_price, recv_window=recv_window)

Volume Participation(VP) New Order (TRADE)

Send in a VP new order. Only support on USDⓈ-M Contracts.  - You need to enable `Futures Trading Permission` for the api key which requests this endpoint. - Base URL: https://api.binance.com  - Total Algo open orders max allowed: 10 orders. - Leverage of symbols and position mode will be the same as your futures account settings. You can set up through the trading page or fapi. - Receiving \"success\": true does not mean that your order will be executed. Please use the query order endpoints(GET sapi/v1/algo/futures/openOrders or GET sapi/v1/algo/futures/historicalOrders) to check the order status. For example: Your futures balance is insufficient, or open position with reduce only or position side is inconsistent with your own setting. In these cases you will receive \"success\": true, but the order status will be expired after we check it.  Weight(UID): 3000

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
api_instance = binance_spot.FuturesAlgoApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
quantity = 1.2 # float | Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT
urgency = 'urgency_example' # str | Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
position_side = 'position_side_example' # str | Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode. (optional)
client_algo_id = 'client_algo_id_example' # str | A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value (optional)
reduce_only = true # bool | 'true' or 'false'. Default 'false'; Cannot be sent in Hedge Mode; Cannot be sent when you open a position (optional)
limit_price = 1.2 # float | Limit price of the order; If it is not sent, will place order by market price by default (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Volume Participation(VP) New Order (TRADE)
    api_response = api_instance.sapi_v1_algo_futures_new_order_vp_post(symbol, side, quantity, urgency, timestamp, signature, position_side=position_side, client_algo_id=client_algo_id, reduce_only=reduce_only, limit_price=limit_price, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesAlgoApi->sapi_v1_algo_futures_new_order_vp_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **quantity** | **float**| Quantity of base asset; The notional (quantity * mark price(base asset)) must be more than the equivalent of 10,000 USDT and less than the equivalent of 1,000,000 USDT | 
 **urgency** | **str**| Represent the relative speed of the current execution; ENUM: LOW, MEDIUM, HIGH | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **position_side** | **str**| Default BOTH for One-way Mode ; LONG or SHORT for Hedge Mode. It must be sent in Hedge Mode. | [optional] 
 **client_algo_id** | **str**| A unique id among Algo orders (length should be 32 characters)， If it is not sent, we will give default value | [optional] 
 **reduce_only** | **bool**| &#x27;true&#x27; or &#x27;false&#x27;. Default &#x27;false&#x27;; Cannot be sent in Hedge Mode; Cannot be sent when you open a position | [optional] 
 **limit_price** | **float**| Limit price of the order; If it is not sent, will place order by market price by default | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200153**](InlineResponse200153.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_futures_open_orders_get**
> InlineResponse200155 sapi_v1_algo_futures_open_orders_get(timestamp, signature, recv_window=recv_window)

Query Current Algo Open Orders (USER_DATA)

- You need to enable Futures Trading Permission for the api key which requests this endpoint. - Base URL: https://api.binance.com  Weight(IP): 1

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
api_instance = binance_spot.FuturesAlgoApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Current Algo Open Orders (USER_DATA)
    api_response = api_instance.sapi_v1_algo_futures_open_orders_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesAlgoApi->sapi_v1_algo_futures_open_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200155**](InlineResponse200155.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_futures_order_delete**
> InlineResponse200154 sapi_v1_algo_futures_order_delete(algo_id, timestamp, signature, recv_window=recv_window)

Cancel Algo Order(TRADE)

Cancel an active order. - You need to enable Futures Trading Permission for the api key which requests this endpoint. - Base URL: https://api.binance.com  Weight(IP): 1

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
api_instance = binance_spot.FuturesAlgoApi(binance_spot.ApiClient(configuration))
algo_id = 789 # int | Eg. 14511
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Cancel Algo Order(TRADE)
    api_response = api_instance.sapi_v1_algo_futures_order_delete(algo_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesAlgoApi->sapi_v1_algo_futures_order_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_id** | **int**| Eg. 14511 | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200154**](InlineResponse200154.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_algo_futures_sub_orders_get**
> InlineResponse200157 sapi_v1_algo_futures_sub_orders_get(algo_id, timestamp, signature, page=page, page_size=page_size, recv_window=recv_window)

Query Sub Orders (USER_DATA)

- You need to enable Futures Trading Permission for the api key which requests this endpoint. - Base URL: https://api.binance.com  Weight(IP): 1

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
api_instance = binance_spot.FuturesAlgoApi(binance_spot.ApiClient(configuration))
algo_id = 789 # int | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
page = 56 # int | Default 1 (optional)
page_size = 'page_size_example' # str | Page size, minimum 1, maximum 100, default 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Sub Orders (USER_DATA)
    api_response = api_instance.sapi_v1_algo_futures_sub_orders_get(algo_id, timestamp, signature, page=page, page_size=page_size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesAlgoApi->sapi_v1_algo_futures_sub_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **algo_id** | **int**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **page** | **int**| Default 1 | [optional] 
 **page_size** | **str**| Page size, minimum 1, maximum 100, default 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200157**](InlineResponse200157.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

