# binance_spot.MarketApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v3_agg_trades_get**](MarketApi.md#api_v3_agg_trades_get) | **GET** /api/v3/aggTrades | Compressed/Aggregate Trades List
[**api_v3_avg_price_get**](MarketApi.md#api_v3_avg_price_get) | **GET** /api/v3/avgPrice | Current Average Price
[**api_v3_depth_get**](MarketApi.md#api_v3_depth_get) | **GET** /api/v3/depth | Order Book
[**api_v3_exchange_info_get**](MarketApi.md#api_v3_exchange_info_get) | **GET** /api/v3/exchangeInfo | Exchange Information
[**api_v3_historical_trades_get**](MarketApi.md#api_v3_historical_trades_get) | **GET** /api/v3/historicalTrades | Old Trade Lookup
[**api_v3_klines_get**](MarketApi.md#api_v3_klines_get) | **GET** /api/v3/klines | Kline/Candlestick Data
[**api_v3_ping_get**](MarketApi.md#api_v3_ping_get) | **GET** /api/v3/ping | Test Connectivity
[**api_v3_ticker24hr_get**](MarketApi.md#api_v3_ticker24hr_get) | **GET** /api/v3/ticker/24hr | 24hr Ticker Price Change Statistics
[**api_v3_ticker_book_ticker_get**](MarketApi.md#api_v3_ticker_book_ticker_get) | **GET** /api/v3/ticker/bookTicker | Symbol Order Book Ticker
[**api_v3_ticker_get**](MarketApi.md#api_v3_ticker_get) | **GET** /api/v3/ticker | Rolling window price change statistics
[**api_v3_ticker_price_get**](MarketApi.md#api_v3_ticker_price_get) | **GET** /api/v3/ticker/price | Symbol Price Ticker
[**api_v3_time_get**](MarketApi.md#api_v3_time_get) | **GET** /api/v3/time | Check Server Time
[**api_v3_trades_get**](MarketApi.md#api_v3_trades_get) | **GET** /api/v3/trades | Recent Trades List
[**api_v3_ui_klines_get**](MarketApi.md#api_v3_ui_klines_get) | **GET** /api/v3/uiKlines | UIKlines

# **api_v3_agg_trades_get**
> list[AggTrade] api_v3_agg_trades_get(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)

Compressed/Aggregate Trades List

Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will have the quantity aggregated. - If `fromId`, `startTime`, and `endTime` are not sent, the most recent aggregate trades will be returned. - Note that if a trade has the following values, this was a duplicate aggregate trade and marked as invalid:    p = '0' // price    q = '0' // qty    f = -1 // ﬁrst_trade_id    l = -1 // last_trade_id  Weight(IP): 2

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
from_id = 789 # int | Trade id to fetch from. Default gets most recent trades. (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)

try:
    # Compressed/Aggregate Trades List
    api_response = api_instance.api_v3_agg_trades_get(symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_agg_trades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 

### Return type

[**list[AggTrade]**](AggTrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_avg_price_get**
> InlineResponse2003 api_v3_avg_price_get(symbol)

Current Average Price

Current average price for a symbol.  Weight(IP): 2

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT

try:
    # Current Average Price
    api_response = api_instance.api_v3_avg_price_get(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_avg_price_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_depth_get**
> InlineResponse2002 api_v3_depth_get(symbol, limit=limit)

Order Book

| Limit               | Weight(IP)  | |---------------------|-------------| | 1-100               | 5           | | 101-500             | 25          | | 501-1000            | 50          | | 1001-5000           | 250         |

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
limit = 100 # int | If limit > 5000, then the response will truncate to 5000 (optional) (default to 100)

try:
    # Order Book
    api_response = api_instance.api_v3_depth_get(symbol, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_depth_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **limit** | **int**| If limit &gt; 5000, then the response will truncate to 5000 | [optional] [default to 100]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_exchange_info_get**
> InlineResponse2001 api_v3_exchange_info_get(symbol=symbol, symbols=symbols, permissions=permissions)

Exchange Information

Current exchange trading rules and symbol information  - If any symbol provided in either symbol or symbols do not exist, the endpoint will throw an error.  Weight(IP): 10

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
symbols = 'symbols_example' # str |  (optional)
permissions = 'permissions_example' # str |  (optional)

try:
    # Exchange Information
    api_response = api_instance.api_v3_exchange_info_get(symbol=symbol, symbols=symbols, permissions=permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_exchange_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **symbols** | **str**|  | [optional] 
 **permissions** | **str**|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_historical_trades_get**
> list[Trade] api_v3_historical_trades_get(symbol, limit=limit, from_id=from_id)

Old Trade Lookup

Get older market trades.  Weight(IP): 10

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
limit = 56 # int | Default 500; max 1000. (optional)
from_id = 789 # int | Trade id to fetch from. Default gets most recent trades. (optional)

try:
    # Old Trade Lookup
    api_response = api_instance.api_v3_historical_trades_get(symbol, limit=limit, from_id=from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_historical_trades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 

### Return type

[**list[Trade]**](Trade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_klines_get**
> list[list[object]] api_v3_klines_get(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

Kline/Candlestick Data

Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.  - If `startTime` and `endTime` are not sent, the most recent klines are returned.  Weight(IP): 2

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
interval = 'interval_example' # str | kline intervals
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)

try:
    # Kline/Candlestick Data
    api_response = api_instance.api_v3_klines_get(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_klines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **interval** | **str**| kline intervals | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 

### Return type

**list[list[object]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ping_get**
> object api_v3_ping_get()

Test Connectivity

Test connectivity to the Rest API.  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()

try:
    # Test Connectivity
    api_response = api_instance.api_v3_ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ticker24hr_get**
> InlineResponse2004 api_v3_ticker24hr_get(symbol=symbol, symbols=symbols, type=type)

24hr Ticker Price Change Statistics

24 hour rolling window price change statistics. Careful when accessing this with no symbol.  - If the symbol is not sent, tickers for all symbols will be returned in an array.  Weight(IP): - `2` for a single symbol; - `80` when the symbol parameter is omitted;

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
symbols = 'symbols_example' # str |  (optional)
type = 'type_example' # str | Supported values: FULL or MINI. If none provided, the default is FULL (optional)

try:
    # 24hr Ticker Price Change Statistics
    api_response = api_instance.api_v3_ticker24hr_get(symbol=symbol, symbols=symbols, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_ticker24hr_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **symbols** | **str**|  | [optional] 
 **type** | **str**| Supported values: FULL or MINI. If none provided, the default is FULL | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ticker_book_ticker_get**
> InlineResponse2006 api_v3_ticker_book_ticker_get(symbol=symbol, symbols=symbols)

Symbol Order Book Ticker

Best price/qty on the order book for a symbol or symbols.  - If the symbol is not sent, bookTickers for all symbols will be returned in an array.  Weight(IP): - `2` for a single symbol; - `4` when the symbol parameter is omitted;

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
symbols = 'symbols_example' # str |  (optional)

try:
    # Symbol Order Book Ticker
    api_response = api_instance.api_v3_ticker_book_ticker_get(symbol=symbol, symbols=symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_ticker_book_ticker_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **symbols** | **str**|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ticker_get**
> InlineResponse2007 api_v3_ticker_get(symbol=symbol, symbols=symbols, window_size=window_size, type=type)

Rolling window price change statistics

The window used to compute statistics is typically slightly wider than requested windowSize.  openTime for /api/v3/ticker always starts on a minute, while the closeTime is the current time of the request. As such, the effective window might be up to 1 minute wider than requested.  E.g. If the closeTime is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the windowSize is 1d. the openTime will be: 1641201420000 (January 3, 2022, 09:17:00 UTC)  Weight(IP): 4 for each requested symbol regardless of windowSize.  The weight for this request will cap at 200 once the number of symbols in the request is more than 50.

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
symbols = 'symbols_example' # str |  (optional)
window_size = 'window_size_example' # str | Defaults to 1d if no parameter provided. Supported windowSize values: 1m,2m....59m for minutes 1h, 2h....23h - for hours 1d...7d - for days.  Units cannot be combined (e.g. 1d2h is not allowed) (optional)
type = 'type_example' # str | Supported values: FULL or MINI. If none provided, the default is FULL (optional)

try:
    # Rolling window price change statistics
    api_response = api_instance.api_v3_ticker_get(symbol=symbol, symbols=symbols, window_size=window_size, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_ticker_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **symbols** | **str**|  | [optional] 
 **window_size** | **str**| Defaults to 1d if no parameter provided. Supported windowSize values: 1m,2m....59m for minutes 1h, 2h....23h - for hours 1d...7d - for days.  Units cannot be combined (e.g. 1d2h is not allowed) | [optional] 
 **type** | **str**| Supported values: FULL or MINI. If none provided, the default is FULL | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ticker_price_get**
> InlineResponse2005 api_v3_ticker_price_get(symbol=symbol, symbols=symbols)

Symbol Price Ticker

Latest price for a symbol or symbols.  - If the symbol is not sent, prices for all symbols will be returned in an array.  Weight(IP): - `2` for a single symbol; - `4` when the symbol parameter is omitted;

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
symbols = 'symbols_example' # str |  (optional)

try:
    # Symbol Price Ticker
    api_response = api_instance.api_v3_ticker_price_get(symbol=symbol, symbols=symbols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_ticker_price_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **symbols** | **str**|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_time_get**
> InlineResponse200 api_v3_time_get()

Check Server Time

Test connectivity to the Rest API and get the current server time.  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()

try:
    # Check Server Time
    api_response = api_instance.api_v3_time_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_time_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_trades_get**
> list[Trade] api_v3_trades_get(symbol, limit=limit)

Recent Trades List

Get recent trades.  Weight(IP): 10

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
limit = 56 # int | Default 500; max 1000. (optional)

try:
    # Recent Trades List
    api_response = api_instance.api_v3_trades_get(symbol, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_trades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **limit** | **int**| Default 500; max 1000. | [optional] 

### Return type

[**list[Trade]**](Trade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v3_ui_klines_get**
> list[list[object]] api_v3_ui_klines_get(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)

UIKlines

The request is similar to klines having the same parameters and response.  uiKlines return modified kline data, optimized for presentation of candlestick charts.  Weight(IP): 2

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.MarketApi()
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
interval = 'interval_example' # str | kline intervals
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)

try:
    # UIKlines
    api_response = api_instance.api_v3_ui_klines_get(symbol, interval, start_time=start_time, end_time=end_time, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->api_v3_ui_klines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **interval** | **str**| kline intervals | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 

### Return type

**list[list[object]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

