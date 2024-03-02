# binance_spot.TradeApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_account_get**](TradeApi.md#api_v3_account_get) | **GET** /api/v3/account | Account Information (USER_DATA)
[**api_v3_all_order_list_get**](TradeApi.md#api_v3_all_order_list_get) | **GET** /api/v3/allOrderList | Query all OCO (USER_DATA)
[**api_v3_all_orders_get**](TradeApi.md#api_v3_all_orders_get) | **GET** /api/v3/allOrders | All Orders (USER_DATA)
[**api_v3_my_allocations_get**](TradeApi.md#api_v3_my_allocations_get) | **GET** /api/v3/myAllocations | Query Allocations (USER_DATA)
[**api_v3_my_prevented_matches_get**](TradeApi.md#api_v3_my_prevented_matches_get) | **GET** /api/v3/myPreventedMatches | Query Prevented Matches
[**api_v3_my_trades_get**](TradeApi.md#api_v3_my_trades_get) | **GET** /api/v3/myTrades | Account Trade List (USER_DATA)
[**api_v3_open_order_list_get**](TradeApi.md#api_v3_open_order_list_get) | **GET** /api/v3/openOrderList | Query Open OCO (USER_DATA)
[**api_v3_open_orders_delete**](TradeApi.md#api_v3_open_orders_delete) | **DELETE** /api/v3/openOrders | Cancel all Open Orders on a Symbol (TRADE)
[**api_v3_open_orders_get**](TradeApi.md#api_v3_open_orders_get) | **GET** /api/v3/openOrders | Current Open Orders (USER_DATA)
[**api_v3_order_cancel_replace_post**](TradeApi.md#api_v3_order_cancel_replace_post) | **POST** /api/v3/order/cancelReplace | Cancel an Existing Order and Send a New Order (Trade)
[**api_v3_order_delete**](TradeApi.md#api_v3_order_delete) | **DELETE** /api/v3/order | Cancel Order (TRADE)
[**api_v3_order_get**](TradeApi.md#api_v3_order_get) | **GET** /api/v3/order | Query Order (USER_DATA)
[**api_v3_order_list_delete**](TradeApi.md#api_v3_order_list_delete) | **DELETE** /api/v3/orderList | Cancel OCO (TRADE)
[**api_v3_order_list_get**](TradeApi.md#api_v3_order_list_get) | **GET** /api/v3/orderList | Query OCO (USER_DATA)
[**api_v3_order_oco_post**](TradeApi.md#api_v3_order_oco_post) | **POST** /api/v3/order/oco | New OCO (TRADE)
[**api_v3_order_post**](TradeApi.md#api_v3_order_post) | **POST** /api/v3/order | New Order (TRADE)
[**api_v3_order_test_post**](TradeApi.md#api_v3_order_test_post) | **POST** /api/v3/order/test | Test New Order (TRADE)
[**api_v3_rate_limit_order_get**](TradeApi.md#api_v3_rate_limit_order_get) | **GET** /api/v3/rateLimit/order | Query Current Order Count Usage (TRADE)
[**api_v3_sor_order_post**](TradeApi.md#api_v3_sor_order_post) | **POST** /api/v3/sor/order | New order using SOR (TRADE)
[**api_v3_sor_order_test_post**](TradeApi.md#api_v3_sor_order_test_post) | **POST** /api/v3/sor/order/test | Test new order using SOR (TRADE)

# **api_v3_account_get**
> Account api_v3_account_get(timestamp, signature, recv_window=recv_window)

Account Information (USER_DATA)

Get current account information.  Weight(IP): 20

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Account Information (USER_DATA)
    api_response = api_instance.api_v3_account_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_all_order_list_get**
> list[InlineResponse20012] api_v3_all_order_list_get(timestamp, signature, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query all OCO (USER_DATA)

Retrieves all OCO based on provided optional parameters  Weight(IP): 20

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
from_id = 789 # int | Trade id to fetch from. Default gets most recent trades. (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query all OCO (USER_DATA)
    api_response = api_instance.api_v3_all_order_list_get(timestamp, signature, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_all_order_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20012]**](InlineResponse20012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_all_orders_get**
> list[OrderDetails] api_v3_all_orders_get(symbol, timestamp, signature, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

All Orders (USER_DATA)

Get all account orders; active, canceled, or filled..  - If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned. - For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time. - If `startTime` and/or `endTime` provided, `orderId` is not required  Weight(IP): 20

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order id (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # All Orders (USER_DATA)
    api_response = api_instance.api_v3_all_orders_get(symbol, timestamp, signature, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_all_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order id | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[OrderDetails]**](OrderDetails.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_my_allocations_get**
> list[InlineResponse20017] api_v3_my_allocations_get(symbol, timestamp, signature, start_time=start_time, end_time=end_time, from_allocation_id=from_allocation_id, limit=limit, order_id=order_id, recv_window=recv_window)

Query Allocations (USER_DATA)

Retrieves allocations resulting from SOR order placement.  Weight: 20  Supported parameter combinations: Parameters                            Response symbol                                allocations from oldest to newest symbol + startTime                    oldest allocations since startTime symbol + endTime                      newest allocations until endTime symbol + startTime + endTime          allocations within the time range symbol + fromAllocationId            allocations by allocation ID symbol + orderId                      allocations related to an order starting with oldest symbol + orderId + fromAllocationId  allocations related to an order by allocation ID  Note: The time between startTime and endTime can't be longer than 24 hours.

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
from_allocation_id = 789 # int |  (optional)
limit = 56 # int | Default 500; max 1000. (optional)
order_id = 789 # int | Order id (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Allocations (USER_DATA)
    api_response = api_instance.api_v3_my_allocations_get(symbol, timestamp, signature, start_time=start_time, end_time=end_time, from_allocation_id=from_allocation_id, limit=limit, order_id=order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_my_allocations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **from_allocation_id** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **order_id** | **int**| Order id | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20017]**](InlineResponse20017.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_my_prevented_matches_get**
> list[InlineResponse20016] api_v3_my_prevented_matches_get(symbol, timestamp, signature, prevented_match_id=prevented_match_id, order_id=order_id, from_prevented_match_id=from_prevented_match_id, limit=limit, recv_window=recv_window)

Query Prevented Matches

Displays the list of orders that were expired because of STP.  For additional information on what a Prevented match is, as well as Self Trade Prevention (STP), please refer to our STP FAQ page.  These are the combinations supported:  * symbol + preventedMatchId * symbol + orderId * symbol + orderId + fromPreventedMatchId (limit will default to 500) * symbol + orderId + fromPreventedMatchId + limit  Weight(IP):  Case                            Weight If symbol is invalid:          2 Querying by preventedMatchId:  2 Querying by orderId:            20

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
prevented_match_id = 789 # int |  (optional)
order_id = 789 # int | Order id (optional)
from_prevented_match_id = 789 # int |  (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Prevented Matches
    api_response = api_instance.api_v3_my_prevented_matches_get(symbol, timestamp, signature, prevented_match_id=prevented_match_id, order_id=order_id, from_prevented_match_id=from_prevented_match_id, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_my_prevented_matches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **prevented_match_id** | **int**|  | [optional] 
 **order_id** | **int**| Order id | [optional] 
 **from_prevented_match_id** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20016]**](InlineResponse20016.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_my_trades_get**
> list[MyTrade] api_v3_my_trades_get(symbol, timestamp, signature, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Account Trade List (USER_DATA)

Get trades for a specific account and symbol.  If `fromId` is set, it will get id >= that `fromId`. Otherwise most recent orders are returned.  The time between startTime and endTime can't be longer than 24 hours. These are the supported combinations of all parameters:    symbol    symbol + orderId    symbol + startTime    symbol + endTime    symbol + fromId    symbol + startTime + endTime    symbol+ orderId + fromId  Weight(IP): 20

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | This can only be used in combination with symbol. (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
from_id = 789 # int | Trade id to fetch from. Default gets most recent trades. (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Account Trade List (USER_DATA)
    api_response = api_instance.api_v3_my_trades_get(symbol, timestamp, signature, order_id=order_id, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_my_trades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| This can only be used in combination with symbol. | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[MyTrade]**](MyTrade.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_open_order_list_get**
> list[InlineResponse20013] api_v3_open_order_list_get(timestamp, signature, recv_window=recv_window)

Query Open OCO (USER_DATA)

Weight(IP): 6

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Open OCO (USER_DATA)
    api_response = api_instance.api_v3_open_order_list_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_open_order_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20013]**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_open_orders_delete**
> list[object] api_v3_open_orders_delete(symbol, timestamp, signature, recv_window=recv_window)

Cancel all Open Orders on a Symbol (TRADE)

Cancels all active orders on a symbol. This includes OCO orders.  Weight(IP): 1

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Cancel all Open Orders on a Symbol (TRADE)
    api_response = api_instance.api_v3_open_orders_delete(symbol, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_open_orders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

**list[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_open_orders_get**
> list[OrderDetails] api_v3_open_orders_get(timestamp, signature, symbol=symbol, recv_window=recv_window)

Current Open Orders (USER_DATA)

Get all open orders on a symbol. Careful when accessing this with no symbol.  Weight(IP): - `6` for a single symbol; - `80` when the symbol parameter is omitted;

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Current Open Orders (USER_DATA)
    api_response = api_instance.api_v3_open_orders_get(timestamp, signature, symbol=symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_open_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[OrderDetails]**](OrderDetails.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_order_cancel_replace_post**
> InlineResponse2009 api_v3_order_cancel_replace_post(symbol, side, type, cancel_replace_mode, timestamp, signature, cancel_restrictions=cancel_restrictions, time_in_force=time_in_force, quantity=quantity, quote_order_qty=quote_order_qty, price=price, cancel_new_client_order_id=cancel_new_client_order_id, cancel_orig_client_order_id=cancel_orig_client_order_id, cancel_order_id=cancel_order_id, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, stop_price=stop_price, trailing_delta=trailing_delta, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)

Cancel an Existing Order and Send a New Order (Trade)

Cancels an existing order and places a new order on the same symbol.  Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.  A new order that was not attempted (i.e. when newOrderResult: NOT_ATTEMPTED), will still increase the order count by 1.  Weight(IP): 1

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
type = 'type_example' # str | Order type
cancel_replace_mode = 'cancel_replace_mode_example' # str | - `STOP_ON_FAILURE` If the cancel request fails, the new order placement will not be attempted. - `ALLOW_FAILURES` If new order placement will be attempted even if cancel request fails.
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
cancel_restrictions = 'cancel_restrictions_example' # str |  (optional)
time_in_force = 'time_in_force_example' # str | Order time in force (optional)
quantity = 1.2 # float | Order quantity (optional)
quote_order_qty = 1.2 # float | Quote quantity (optional)
price = 1.2 # float | Order price (optional)
cancel_new_client_order_id = 'cancel_new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
cancel_orig_client_order_id = 'cancel_orig_client_order_id_example' # str | Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence. (optional)
cancel_order_id = 789 # int | Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence. (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
strategy_id = 789 # int |  (optional)
strategy_type = 789 # int | The value cannot be less than 1000000. (optional)
stop_price = 1.2 # float | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. (optional)
trailing_delta = 1.2 # float | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. (optional)
iceberg_qty = 1.2 # float | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. (optional)
new_order_resp_type = 'new_order_resp_type_example' # str | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. (optional)
self_trade_prevention_mode = 'self_trade_prevention_mode_example' # str | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Cancel an Existing Order and Send a New Order (Trade)
    api_response = api_instance.api_v3_order_cancel_replace_post(symbol, side, type, cancel_replace_mode, timestamp, signature, cancel_restrictions=cancel_restrictions, time_in_force=time_in_force, quantity=quantity, quote_order_qty=quote_order_qty, price=price, cancel_new_client_order_id=cancel_new_client_order_id, cancel_orig_client_order_id=cancel_orig_client_order_id, cancel_order_id=cancel_order_id, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, stop_price=stop_price, trailing_delta=trailing_delta, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_order_cancel_replace_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **type** | **str**| Order type | 
 **cancel_replace_mode** | **str**| - &#x60;STOP_ON_FAILURE&#x60; If the cancel request fails, the new order placement will not be attempted. - &#x60;ALLOW_FAILURES&#x60; If new order placement will be attempted even if cancel request fails. | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **cancel_restrictions** | **str**|  | [optional] 
 **time_in_force** | **str**| Order time in force | [optional] 
 **quantity** | **float**| Order quantity | [optional] 
 **quote_order_qty** | **float**| Quote quantity | [optional] 
 **price** | **float**| Order price | [optional] 
 **cancel_new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **cancel_orig_client_order_id** | **str**| Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence. | [optional] 
 **cancel_order_id** | **int**| Either the cancelOrigClientOrderId or cancelOrderId must be provided. If both are provided, cancelOrderId takes precedence. | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**| The value cannot be less than 1000000. | [optional] 
 **stop_price** | **float**| Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. | [optional] 
 **trailing_delta** | **float**| Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. | [optional] 
 **iceberg_qty** | **float**| Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. | [optional] 
 **new_order_resp_type** | **str**| Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. | [optional] 
 **self_trade_prevention_mode** | **str**| The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_order_delete**
> Order api_v3_order_delete(symbol, timestamp, signature, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, cancel_restrictions=cancel_restrictions, recv_window=recv_window)

Cancel Order (TRADE)

Cancel an active order.  Either `orderId` or `origClientOrderId` must be sent.  Weight(IP): 1

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order id (optional)
orig_client_order_id = 'orig_client_order_id_example' # str | Order id from client (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
cancel_restrictions = 'cancel_restrictions_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Cancel Order (TRADE)
    api_response = api_instance.api_v3_order_delete(symbol, timestamp, signature, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, cancel_restrictions=cancel_restrictions, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_order_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order id | [optional] 
 **orig_client_order_id** | **str**| Order id from client | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **cancel_restrictions** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_order_get**
> OrderDetails api_v3_order_get(symbol, timestamp, signature, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Order (USER_DATA)

Check an order's status.  - Either `orderId` or `origClientOrderId` must be sent. - For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.  Weight(IP): 4

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order id (optional)
orig_client_order_id = 'orig_client_order_id_example' # str | Order id from client (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Order (USER_DATA)
    api_response = api_instance.api_v3_order_get(symbol, timestamp, signature, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_order_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order id | [optional] 
 **orig_client_order_id** | **str**| Order id from client | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**OrderDetails**](OrderDetails.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_order_list_delete**
> OcoOrder api_v3_order_list_delete(symbol, timestamp, signature, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Cancel OCO (TRADE)

Cancel an entire Order List  Canceling an individual leg will cancel the entire OCO  Weight(IP): 1

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_list_id = 789 # int | Order list id (optional)
list_client_order_id = 'list_client_order_id_example' # str | A unique Id for the entire orderList (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Cancel OCO (TRADE)
    api_response = api_instance.api_v3_order_list_delete(symbol, timestamp, signature, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_order_list_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_list_id** | **int**| Order list id | [optional] 
 **list_client_order_id** | **str**| A unique Id for the entire orderList | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**OcoOrder**](OcoOrder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_order_list_get**
> InlineResponse20011 api_v3_order_list_get(timestamp, signature, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query OCO (USER_DATA)

Retrieves a specific OCO based on provided optional parameters  Weight(IP): 4

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_list_id = 789 # int | Order list id (optional)
orig_client_order_id = 'orig_client_order_id_example' # str | Order id from client (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query OCO (USER_DATA)
    api_response = api_instance.api_v3_order_list_get(timestamp, signature, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_order_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_list_id** | **int**| Order list id | [optional] 
 **orig_client_order_id** | **str**| Order id from client | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_order_oco_post**
> InlineResponse20010 api_v3_order_oco_post(symbol, side, quantity, price, stop_price, timestamp, signature, list_client_order_id=list_client_order_id, limit_client_order_id=limit_client_order_id, limit_strategy_id=limit_strategy_id, limit_strategy_type=limit_strategy_type, limit_iceberg_qty=limit_iceberg_qty, trailing_delta=trailing_delta, stop_client_order_id=stop_client_order_id, stop_strategy_id=stop_strategy_id, stop_strategy_type=stop_strategy_type, stop_limit_price=stop_limit_price, stop_iceberg_qty=stop_iceberg_qty, stop_limit_time_in_force=stop_limit_time_in_force, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)

New OCO (TRADE)

Send in a new OCO  - Price Restrictions:   - `SELL`: Limit Price > Last Price > Stop Price   - `BUY`: Limit Price < Last Price < Stop Price - Quantity Restrictions:     - Both legs must have the same quantity     - `ICEBERG` quantities however do not have to be the same - Order Rate Limit     - `OCO` counts as 2 orders against the order rate limit.  Weight(IP): 1

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
quantity = 1.2 # float | 
price = 1.2 # float | Order price
stop_price = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
list_client_order_id = 'list_client_order_id_example' # str | A unique Id for the entire orderList (optional)
limit_client_order_id = 'limit_client_order_id_example' # str | A unique Id for the limit order (optional)
limit_strategy_id = 789 # int |  (optional)
limit_strategy_type = 789 # int | The value cannot be less than 1000000. (optional)
limit_iceberg_qty = 1.2 # float |  (optional)
trailing_delta = 1.2 # float |  (optional)
stop_client_order_id = 'stop_client_order_id_example' # str | A unique Id for the stop loss/stop loss limit leg (optional)
stop_strategy_id = 789 # int |  (optional)
stop_strategy_type = 789 # int |  (optional)
stop_limit_price = 1.2 # float | If provided, stopLimitTimeInForce is required. (optional)
stop_iceberg_qty = 1.2 # float |  (optional)
stop_limit_time_in_force = 'stop_limit_time_in_force_example' # str |  (optional)
new_order_resp_type = 'new_order_resp_type_example' # str | Set the response JSON. (optional)
self_trade_prevention_mode = 'self_trade_prevention_mode_example' # str | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # New OCO (TRADE)
    api_response = api_instance.api_v3_order_oco_post(symbol, side, quantity, price, stop_price, timestamp, signature, list_client_order_id=list_client_order_id, limit_client_order_id=limit_client_order_id, limit_strategy_id=limit_strategy_id, limit_strategy_type=limit_strategy_type, limit_iceberg_qty=limit_iceberg_qty, trailing_delta=trailing_delta, stop_client_order_id=stop_client_order_id, stop_strategy_id=stop_strategy_id, stop_strategy_type=stop_strategy_type, stop_limit_price=stop_limit_price, stop_iceberg_qty=stop_iceberg_qty, stop_limit_time_in_force=stop_limit_time_in_force, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_order_oco_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **quantity** | **float**|  | 
 **price** | **float**| Order price | 
 **stop_price** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **list_client_order_id** | **str**| A unique Id for the entire orderList | [optional] 
 **limit_client_order_id** | **str**| A unique Id for the limit order | [optional] 
 **limit_strategy_id** | **int**|  | [optional] 
 **limit_strategy_type** | **int**| The value cannot be less than 1000000. | [optional] 
 **limit_iceberg_qty** | **float**|  | [optional] 
 **trailing_delta** | **float**|  | [optional] 
 **stop_client_order_id** | **str**| A unique Id for the stop loss/stop loss limit leg | [optional] 
 **stop_strategy_id** | **int**|  | [optional] 
 **stop_strategy_type** | **int**|  | [optional] 
 **stop_limit_price** | **float**| If provided, stopLimitTimeInForce is required. | [optional] 
 **stop_iceberg_qty** | **float**|  | [optional] 
 **stop_limit_time_in_force** | **str**|  | [optional] 
 **new_order_resp_type** | **str**| Set the response JSON. | [optional] 
 **self_trade_prevention_mode** | **str**| The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_order_post**
> InlineResponse2008 api_v3_order_post(symbol, side, type, timestamp, signature, time_in_force=time_in_force, quantity=quantity, quote_order_qty=quote_order_qty, price=price, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, stop_price=stop_price, trailing_delta=trailing_delta, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)

New Order (TRADE)

Send in a new order.  - `LIMIT_MAKER` are `LIMIT` orders that will be rejected if they would immediately match and trade as a taker. - `STOP_LOSS` and `TAKE_PROFIT` will execute a `MARKET` order when the `stopPrice` is reached. - Any `LIMIT` or `LIMIT_MAKER` type order can be made an iceberg order by sending an `icebergQty`. - Any order with an `icebergQty` MUST have `timeInForce` set to `GTC`. - `MARKET` orders using `quantity` specifies how much a user wants to buy or sell based on the market price. - `MARKET` orders using `quoteOrderQty` specifies the amount the user wants to spend (when buying) or receive (when selling) of the quote asset; the correct quantity will be determined based on the market liquidity and `quoteOrderQty`. - `MARKET` orders using `quoteOrderQty` will not break `LOT_SIZE` filter rules; the order will execute a quantity that will have the notional value as close as possible to `quoteOrderQty`. - same `newClientOrderId` can be accepted only when the previous one is filled, otherwise the order will be rejected.  Trigger order price rules against market price for both `MARKET` and `LIMIT` versions:  - Price above market price: `STOP_LOSS` `BUY`, `TAKE_PROFIT` `SELL` - Price below market price: `STOP_LOSS` `SELL`, `TAKE_PROFIT` `BUY`   Weight(IP): 1

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
type = 'type_example' # str | Order type
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
time_in_force = 'time_in_force_example' # str | Order time in force (optional)
quantity = 1.2 # float | Order quantity (optional)
quote_order_qty = 1.2 # float | Quote quantity (optional)
price = 1.2 # float | Order price (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
strategy_id = 789 # int |  (optional)
strategy_type = 789 # int | The value cannot be less than 1000000. (optional)
stop_price = 1.2 # float | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. (optional)
trailing_delta = 1.2 # float | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. (optional)
iceberg_qty = 1.2 # float | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. (optional)
new_order_resp_type = 'new_order_resp_type_example' # str | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. (optional)
self_trade_prevention_mode = 'self_trade_prevention_mode_example' # str | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # New Order (TRADE)
    api_response = api_instance.api_v3_order_post(symbol, side, type, timestamp, signature, time_in_force=time_in_force, quantity=quantity, quote_order_qty=quote_order_qty, price=price, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, stop_price=stop_price, trailing_delta=trailing_delta, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **type** | **str**| Order type | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **time_in_force** | **str**| Order time in force | [optional] 
 **quantity** | **float**| Order quantity | [optional] 
 **quote_order_qty** | **float**| Quote quantity | [optional] 
 **price** | **float**| Order price | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**| The value cannot be less than 1000000. | [optional] 
 **stop_price** | **float**| Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. | [optional] 
 **trailing_delta** | **float**| Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. | [optional] 
 **iceberg_qty** | **float**| Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. | [optional] 
 **new_order_resp_type** | **str**| Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. | [optional] 
 **self_trade_prevention_mode** | **str**| The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_order_test_post**
> object api_v3_order_test_post(symbol, side, type, timestamp, signature, time_in_force=time_in_force, quantity=quantity, quote_order_qty=quote_order_qty, price=price, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, stop_price=stop_price, trailing_delta=trailing_delta, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, recv_window=recv_window)

Test New Order (TRADE)

Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.  Weight(IP): 1

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
type = 'type_example' # str | Order type
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
time_in_force = 'time_in_force_example' # str | Order time in force (optional)
quantity = 1.2 # float | Order quantity (optional)
quote_order_qty = 1.2 # float | Quote quantity (optional)
price = 1.2 # float | Order price (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
strategy_id = 789 # int |  (optional)
strategy_type = 789 # int | The value cannot be less than 1000000. (optional)
stop_price = 1.2 # float | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. (optional)
trailing_delta = 1.2 # float | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. (optional)
iceberg_qty = 1.2 # float | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. (optional)
new_order_resp_type = 'new_order_resp_type_example' # str | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Test New Order (TRADE)
    api_response = api_instance.api_v3_order_test_post(symbol, side, type, timestamp, signature, time_in_force=time_in_force, quantity=quantity, quote_order_qty=quote_order_qty, price=price, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, stop_price=stop_price, trailing_delta=trailing_delta, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_order_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **type** | **str**| Order type | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **time_in_force** | **str**| Order time in force | [optional] 
 **quantity** | **float**| Order quantity | [optional] 
 **quote_order_qty** | **float**| Quote quantity | [optional] 
 **price** | **float**| Order price | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**| The value cannot be less than 1000000. | [optional] 
 **stop_price** | **float**| Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. | [optional] 
 **trailing_delta** | **float**| Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. | [optional] 
 **iceberg_qty** | **float**| Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. | [optional] 
 **new_order_resp_type** | **str**| Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_rate_limit_order_get**
> list[InlineResponse20015] api_v3_rate_limit_order_get(timestamp, signature, recv_window=recv_window)

Query Current Order Count Usage (TRADE)

Displays the user's current order count usage for all intervals.  Weight(IP): 40

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Current Order Count Usage (TRADE)
    api_response = api_instance.api_v3_rate_limit_order_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_rate_limit_order_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20015]**](InlineResponse20015.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_sor_order_post**
> InlineResponse20014 api_v3_sor_order_post(symbol, side, type, quantity, timestamp, signature, time_in_force=time_in_force, price=price, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)

New order using SOR (TRADE)

Weight(IP): 6

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
type = 'type_example' # str | Order type
quantity = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
time_in_force = 'time_in_force_example' # str | Order time in force (optional)
price = 1.2 # float |  (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
strategy_id = 789 # int |  (optional)
strategy_type = 789 # int | The value cannot be less than 1000000. (optional)
iceberg_qty = 1.2 # float | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. (optional)
new_order_resp_type = 'new_order_resp_type_example' # str | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. (optional)
self_trade_prevention_mode = 'self_trade_prevention_mode_example' # str | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # New order using SOR (TRADE)
    api_response = api_instance.api_v3_sor_order_post(symbol, side, type, quantity, timestamp, signature, time_in_force=time_in_force, price=price, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_sor_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **type** | **str**| Order type | 
 **quantity** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **time_in_force** | **str**| Order time in force | [optional] 
 **price** | **float**|  | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**| The value cannot be less than 1000000. | [optional] 
 **iceberg_qty** | **float**| Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. | [optional] 
 **new_order_resp_type** | **str**| Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. | [optional] 
 **self_trade_prevention_mode** | **str**| The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_sor_order_test_post**
> object api_v3_sor_order_test_post(symbol, side, type, quantity, timestamp, signature, time_in_force=time_in_force, price=price, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)

Test new order using SOR (TRADE)

Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new order but does not send it into the matching engine.

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
api_instance = binance_spot.TradeApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
type = 'type_example' # str | Order type
quantity = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
time_in_force = 'time_in_force_example' # str | Order time in force (optional)
price = 1.2 # float |  (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
strategy_id = 789 # int |  (optional)
strategy_type = 789 # int | The value cannot be less than 1000000. (optional)
iceberg_qty = 1.2 # float | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. (optional)
new_order_resp_type = 'new_order_resp_type_example' # str | Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. (optional)
self_trade_prevention_mode = 'self_trade_prevention_mode_example' # str | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Test new order using SOR (TRADE)
    api_response = api_instance.api_v3_sor_order_test_post(symbol, side, type, quantity, timestamp, signature, time_in_force=time_in_force, price=price, new_client_order_id=new_client_order_id, strategy_id=strategy_id, strategy_type=strategy_type, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->api_v3_sor_order_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **type** | **str**| Order type | 
 **quantity** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **time_in_force** | **str**| Order time in force | [optional] 
 **price** | **float**|  | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **strategy_id** | **int**|  | [optional] 
 **strategy_type** | **int**| The value cannot be less than 1000000. | [optional] 
 **iceberg_qty** | **float**| Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. | [optional] 
 **new_order_resp_type** | **str**| Set the response JSON. MARKET and LIMIT order types default to FULL, all other orders default to ACK. | [optional] 
 **self_trade_prevention_mode** | **str**| The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

