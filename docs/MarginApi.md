# binance_spot.MarginApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_bnb_burn_get**](MarginApi.md#sapi_v1_bnb_burn_get) | **GET** /sapi/v1/bnbBurn | Get BNB Burn Status(USER_DATA)
[**sapi_v1_bnb_burn_post**](MarginApi.md#sapi_v1_bnb_burn_post) | **POST** /sapi/v1/bnbBurn | Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
[**sapi_v1_margin_account_get**](MarginApi.md#sapi_v1_margin_account_get) | **GET** /sapi/v1/margin/account | Query Cross Margin Account Details (USER_DATA)
[**sapi_v1_margin_all_assets_get**](MarginApi.md#sapi_v1_margin_all_assets_get) | **GET** /sapi/v1/margin/allAssets | Get All Margin Assets (MARKET_DATA)
[**sapi_v1_margin_all_order_list_get**](MarginApi.md#sapi_v1_margin_all_order_list_get) | **GET** /sapi/v1/margin/allOrderList | Query Margin Account&#x27;s all OCO (USER_DATA)
[**sapi_v1_margin_all_orders_get**](MarginApi.md#sapi_v1_margin_all_orders_get) | **GET** /sapi/v1/margin/allOrders | Query Margin Account&#x27;s All Orders (USER_DATA)
[**sapi_v1_margin_all_pairs_get**](MarginApi.md#sapi_v1_margin_all_pairs_get) | **GET** /sapi/v1/margin/allPairs | Get All Cross Margin Pairs (MARKET_DATA)
[**sapi_v1_margin_asset_get**](MarginApi.md#sapi_v1_margin_asset_get) | **GET** /sapi/v1/margin/asset | Query Margin Asset (MARKET_DATA)
[**sapi_v1_margin_available_inventory_get**](MarginApi.md#sapi_v1_margin_available_inventory_get) | **GET** /sapi/v1/margin/available-inventory | Query Margin Available Inventory (USER_DATA)
[**sapi_v1_margin_capital_flow_get**](MarginApi.md#sapi_v1_margin_capital_flow_get) | **GET** /sapi/v1/margin/capital-flow | Get cross or isolated margin capital flow(USER_DATA)
[**sapi_v1_margin_cross_margin_collateral_ratio_get**](MarginApi.md#sapi_v1_margin_cross_margin_collateral_ratio_get) | **GET** /sapi/v1/margin/crossMarginCollateralRatio | Cross margin collateral ratio (MARKET_DATA)
[**sapi_v1_margin_cross_margin_data_get**](MarginApi.md#sapi_v1_margin_cross_margin_data_get) | **GET** /sapi/v1/margin/crossMarginData | Query Cross Margin Fee Data (USER_DATA)
[**sapi_v1_margin_delist_schedule_get**](MarginApi.md#sapi_v1_margin_delist_schedule_get) | **GET** /sapi/v1/margin/delist-schedule | Get tokens or symbols delist schedule for cross margin and isolated margin (MARKET_DATA)
[**sapi_v1_margin_dribblet_get**](MarginApi.md#sapi_v1_margin_dribblet_get) | **GET** /sapi/v1/margin/dribblet | Margin Dustlog (USER_DATA)
[**sapi_v1_margin_dust_get**](MarginApi.md#sapi_v1_margin_dust_get) | **GET** /sapi/v1/margin/dust | Get Assets That Can Be Converted Into BNB (USER_DATA)
[**sapi_v1_margin_dust_post**](MarginApi.md#sapi_v1_margin_dust_post) | **POST** /sapi/v1/margin/dust | Dust Transfer (TRADE)
[**sapi_v1_margin_exchange_small_liability_get**](MarginApi.md#sapi_v1_margin_exchange_small_liability_get) | **GET** /sapi/v1/margin/exchange-small-liability | Get Small Liability Exchange Coin List (USER_DATA)
[**sapi_v1_margin_exchange_small_liability_history_get**](MarginApi.md#sapi_v1_margin_exchange_small_liability_history_get) | **GET** /sapi/v1/margin/exchange-small-liability-history | Get Small Liability Exchange History (USER_DATA)
[**sapi_v1_margin_force_liquidation_rec_get**](MarginApi.md#sapi_v1_margin_force_liquidation_rec_get) | **GET** /sapi/v1/margin/forceLiquidationRec | Get Force Liquidation Record (USER_DATA)
[**sapi_v1_margin_interest_history_get**](MarginApi.md#sapi_v1_margin_interest_history_get) | **GET** /sapi/v1/margin/interestHistory | Get Interest History (USER_DATA)
[**sapi_v1_margin_interest_rate_history_get**](MarginApi.md#sapi_v1_margin_interest_rate_history_get) | **GET** /sapi/v1/margin/interestRateHistory | Margin Interest Rate History (USER_DATA)
[**sapi_v1_margin_isolated_account_delete**](MarginApi.md#sapi_v1_margin_isolated_account_delete) | **DELETE** /sapi/v1/margin/isolated/account | Disable Isolated Margin Account (TRADE)
[**sapi_v1_margin_isolated_account_get**](MarginApi.md#sapi_v1_margin_isolated_account_get) | **GET** /sapi/v1/margin/isolated/account | Query Isolated Margin Account Info (USER_DATA)
[**sapi_v1_margin_isolated_account_limit_get**](MarginApi.md#sapi_v1_margin_isolated_account_limit_get) | **GET** /sapi/v1/margin/isolated/accountLimit | Query Enabled Isolated Margin Account Limit (USER_DATA)
[**sapi_v1_margin_isolated_account_post**](MarginApi.md#sapi_v1_margin_isolated_account_post) | **POST** /sapi/v1/margin/isolated/account | Enable Isolated Margin Account (TRADE)
[**sapi_v1_margin_isolated_all_pairs_get**](MarginApi.md#sapi_v1_margin_isolated_all_pairs_get) | **GET** /sapi/v1/margin/isolated/allPairs | Get All Isolated Margin Symbol(USER_DATA)
[**sapi_v1_margin_isolated_margin_data_get**](MarginApi.md#sapi_v1_margin_isolated_margin_data_get) | **GET** /sapi/v1/margin/isolatedMarginData | Query Isolated Margin Fee Data (USER_DATA)
[**sapi_v1_margin_isolated_margin_tier_get**](MarginApi.md#sapi_v1_margin_isolated_margin_tier_get) | **GET** /sapi/v1/margin/isolatedMarginTier | Query Isolated Margin Tier Data (USER_DATA)
[**sapi_v1_margin_isolated_pair_get**](MarginApi.md#sapi_v1_margin_isolated_pair_get) | **GET** /sapi/v1/margin/isolated/pair | Query Isolated Margin Symbol (USER_DATA)
[**sapi_v1_margin_isolated_transfer_get**](MarginApi.md#sapi_v1_margin_isolated_transfer_get) | **GET** /sapi/v1/margin/isolated/transfer | Get Isolated Margin Transfer History (USER_DATA)
[**sapi_v1_margin_isolated_transfer_post**](MarginApi.md#sapi_v1_margin_isolated_transfer_post) | **POST** /sapi/v1/margin/isolated/transfer | Isolated Margin Account Transfer (MARGIN)
[**sapi_v1_margin_leverage_bracket_get**](MarginApi.md#sapi_v1_margin_leverage_bracket_get) | **GET** /sapi/v1/margin/leverageBracket | Query Liability Coin Leverage Bracket in Cross Margin Pro Mode (MARKET_DATA)
[**sapi_v1_margin_loan_get**](MarginApi.md#sapi_v1_margin_loan_get) | **GET** /sapi/v1/margin/loan | Query Loan Record (USER_DATA)
[**sapi_v1_margin_loan_post**](MarginApi.md#sapi_v1_margin_loan_post) | **POST** /sapi/v1/margin/loan | Margin Account Borrow (MARGIN)
[**sapi_v1_margin_manual_liquidation_post**](MarginApi.md#sapi_v1_margin_manual_liquidation_post) | **POST** /sapi/v1/margin/manual-liquidation | Margin manual liquidation(MARGIN)
[**sapi_v1_margin_max_borrowable_get**](MarginApi.md#sapi_v1_margin_max_borrowable_get) | **GET** /sapi/v1/margin/maxBorrowable | Query Max Borrow (USER_DATA)
[**sapi_v1_margin_max_leverage_post**](MarginApi.md#sapi_v1_margin_max_leverage_post) | **POST** /sapi/v1/margin/max-leverage | Adjust cross margin max leverage (USER_DATA)
[**sapi_v1_margin_max_transferable_get**](MarginApi.md#sapi_v1_margin_max_transferable_get) | **GET** /sapi/v1/margin/maxTransferable | Query Max Transfer-Out Amount (USER_DATA)
[**sapi_v1_margin_my_trades_get**](MarginApi.md#sapi_v1_margin_my_trades_get) | **GET** /sapi/v1/margin/myTrades | Query Margin Account&#x27;s Trade List (USER_DATA)
[**sapi_v1_margin_next_hourly_interest_rate_get**](MarginApi.md#sapi_v1_margin_next_hourly_interest_rate_get) | **GET** /sapi/v1/margin/next-hourly-interest-rate | Get a future hourly interest rate (USER_DATA)
[**sapi_v1_margin_open_order_list_get**](MarginApi.md#sapi_v1_margin_open_order_list_get) | **GET** /sapi/v1/margin/openOrderList | Query Margin Account&#x27;s Open OCO (USER_DATA)
[**sapi_v1_margin_open_orders_delete**](MarginApi.md#sapi_v1_margin_open_orders_delete) | **DELETE** /sapi/v1/margin/openOrders | Margin Account Cancel all Open Orders on a Symbol (TRADE)
[**sapi_v1_margin_open_orders_get**](MarginApi.md#sapi_v1_margin_open_orders_get) | **GET** /sapi/v1/margin/openOrders | Query Margin Account&#x27;s Open Orders (USER_DATA)
[**sapi_v1_margin_order_delete**](MarginApi.md#sapi_v1_margin_order_delete) | **DELETE** /sapi/v1/margin/order | Margin Account Cancel Order (TRADE)
[**sapi_v1_margin_order_get**](MarginApi.md#sapi_v1_margin_order_get) | **GET** /sapi/v1/margin/order | Query Margin Account&#x27;s Order (USER_DATA)
[**sapi_v1_margin_order_list_delete**](MarginApi.md#sapi_v1_margin_order_list_delete) | **DELETE** /sapi/v1/margin/orderList | Margin Account Cancel OCO (TRADE)
[**sapi_v1_margin_order_list_get**](MarginApi.md#sapi_v1_margin_order_list_get) | **GET** /sapi/v1/margin/orderList | Query Margin Account&#x27;s OCO (USER_DATA)
[**sapi_v1_margin_order_oco_post**](MarginApi.md#sapi_v1_margin_order_oco_post) | **POST** /sapi/v1/margin/order/oco | Margin Account New OCO (TRADE)
[**sapi_v1_margin_order_post**](MarginApi.md#sapi_v1_margin_order_post) | **POST** /sapi/v1/margin/order | Margin Account New Order (TRADE)
[**sapi_v1_margin_pair_get**](MarginApi.md#sapi_v1_margin_pair_get) | **GET** /sapi/v1/margin/pair | Query Cross Margin Pair (MARKET_DATA)
[**sapi_v1_margin_price_index_get**](MarginApi.md#sapi_v1_margin_price_index_get) | **GET** /sapi/v1/margin/priceIndex | Query Margin PriceIndex (MARKET_DATA)
[**sapi_v1_margin_rate_limit_order_get**](MarginApi.md#sapi_v1_margin_rate_limit_order_get) | **GET** /sapi/v1/margin/rateLimit/order | Query Current Margin Order Count Usage (TRADE)
[**sapi_v1_margin_repay_get**](MarginApi.md#sapi_v1_margin_repay_get) | **GET** /sapi/v1/margin/repay | Query Repay Record (USER_DATA)
[**sapi_v1_margin_repay_post**](MarginApi.md#sapi_v1_margin_repay_post) | **POST** /sapi/v1/margin/repay | Margin Account Repay (MARGIN)
[**sapi_v1_margin_trade_coeff_get**](MarginApi.md#sapi_v1_margin_trade_coeff_get) | **GET** /sapi/v1/margin/tradeCoeff | Get Summary of Margin account (USER_DATA)
[**sapi_v1_margin_transfer_get**](MarginApi.md#sapi_v1_margin_transfer_get) | **GET** /sapi/v1/margin/transfer | Get Cross Margin Transfer History (USER_DATA)
[**sapi_v1_margin_transfer_post**](MarginApi.md#sapi_v1_margin_transfer_post) | **POST** /sapi/v1/margin/transfer | Cross Margin Account Transfer (MARGIN)

# **sapi_v1_bnb_burn_get**
> BnbBurnStatus sapi_v1_bnb_burn_get(timestamp, signature, recv_window=recv_window)

Get BNB Burn Status(USER_DATA)

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get BNB Burn Status(USER_DATA)
    api_response = api_instance.sapi_v1_bnb_burn_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_bnb_burn_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**BnbBurnStatus**](BnbBurnStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_bnb_burn_post**
> BnbBurnStatus sapi_v1_bnb_burn_post(timestamp, signature, spot_bnb_burn=spot_bnb_burn, interest_bnb_burn=interest_bnb_burn, recv_window=recv_window)

Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)

- \"spotBNBBurn\" and \"interestBNBBurn\" should be sent at least one.  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
spot_bnb_burn = 'spot_bnb_burn_example' # str | Determines whether to use BNB to pay for trading fees on SPOT (optional)
interest_bnb_burn = 'interest_bnb_burn_example' # str | Determines whether to use BNB to pay for margin loan's interest (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)
    api_response = api_instance.sapi_v1_bnb_burn_post(timestamp, signature, spot_bnb_burn=spot_bnb_burn, interest_bnb_burn=interest_bnb_burn, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_bnb_burn_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **spot_bnb_burn** | **str**| Determines whether to use BNB to pay for trading fees on SPOT | [optional] 
 **interest_bnb_burn** | **str**| Determines whether to use BNB to pay for margin loan&#x27;s interest | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**BnbBurnStatus**](BnbBurnStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_account_get**
> InlineResponse20029 sapi_v1_margin_account_get(timestamp, signature, recv_window=recv_window)

Query Cross Margin Account Details (USER_DATA)

Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Cross Margin Account Details (USER_DATA)
    api_response = api_instance.sapi_v1_margin_account_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_all_assets_get**
> list[InlineResponse20023] sapi_v1_margin_all_assets_get()

Get All Margin Assets (MARKET_DATA)

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))

try:
    # Get All Margin Assets (MARKET_DATA)
    api_response = api_instance.sapi_v1_margin_all_assets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_all_assets_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20023]**](InlineResponse20023.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_all_order_list_get**
> list[InlineResponse20012] sapi_v1_margin_all_order_list_get(timestamp, signature, is_isolated=is_isolated, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Margin Account's all OCO (USER_DATA)

Retrieves all OCO for a specific margin account based on provided optional parameters  Weight(IP): 200

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
symbol = 'symbol_example' # str | Mandatory for isolated margin, not supported for cross margin (optional)
from_id = 'from_id_example' # str | If supplied, neither `startTime` or `endTime` can be provided (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default Value: 500; Max Value: 1000 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Margin Account's all OCO (USER_DATA)
    api_response = api_instance.sapi_v1_margin_all_order_list_get(timestamp, signature, is_isolated=is_isolated, symbol=symbol, from_id=from_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_all_order_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **symbol** | **str**| Mandatory for isolated margin, not supported for cross margin | [optional] 
 **from_id** | **str**| If supplied, neither &#x60;startTime&#x60; or &#x60;endTime&#x60; can be provided | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default Value: 500; Max Value: 1000 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20012]**](InlineResponse20012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_all_orders_get**
> list[MarginOrderDetail] sapi_v1_margin_all_orders_get(symbol, timestamp, signature, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Query Margin Account's All Orders (USER_DATA)

- If `orderId` is set, it will get orders >= that orderId. Otherwise most recent orders are returned. - For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.  Weight(IP): 200  Request Limit: 60 times/min per IP

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
order_id = 789 # int | Order id (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Margin Account's All Orders (USER_DATA)
    api_response = api_instance.sapi_v1_margin_all_orders_get(symbol, timestamp, signature, is_isolated=is_isolated, order_id=order_id, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_all_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **order_id** | **int**| Order id | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[MarginOrderDetail]**](MarginOrderDetail.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_all_pairs_get**
> list[InlineResponse20024] sapi_v1_margin_all_pairs_get()

Get All Cross Margin Pairs (MARKET_DATA)

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))

try:
    # Get All Cross Margin Pairs (MARKET_DATA)
    api_response = api_instance.sapi_v1_margin_all_pairs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_all_pairs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20024]**](InlineResponse20024.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_asset_get**
> InlineResponse20021 sapi_v1_margin_asset_get(asset)

Query Margin Asset (MARKET_DATA)

Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 

try:
    # Query Margin Asset (MARKET_DATA)
    api_response = api_instance.sapi_v1_margin_asset_get(asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_available_inventory_get**
> InlineResponse20051 sapi_v1_margin_available_inventory_get(type, timestamp, signature)

Query Margin Available Inventory (USER_DATA)

Margin available Inventory query  Weight(UID): 50

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
type = 'type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature

try:
    # Query Margin Available Inventory (USER_DATA)
    api_response = api_instance.sapi_v1_margin_available_inventory_get(type, timestamp, signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_available_inventory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_capital_flow_get**
> list[InlineResponse20049] sapi_v1_margin_capital_flow_get(timestamp, signature, asset=asset, symbol=symbol, type=type, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Get cross or isolated margin capital flow(USER_DATA)

Get cross or isolated margin capital flow  Weight(IP): 100

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
symbol = 'symbol_example' # str | Required when querying isolated data (optional)
type = 'type_example' # str |  (optional)
start_time = 789 # int | Only supports querying the data of the last 90 days (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
from_id = 789 # int | If fromId is set, the data with id > fromId will be returned. Otherwise the latest data will be returned (optional)
limit = 789 # int | The number of data items returned each time is limited. Default 500; Max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get cross or isolated margin capital flow(USER_DATA)
    api_response = api_instance.sapi_v1_margin_capital_flow_get(timestamp, signature, asset=asset, symbol=symbol, type=type, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_capital_flow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **symbol** | **str**| Required when querying isolated data | [optional] 
 **type** | **str**|  | [optional] 
 **start_time** | **int**| Only supports querying the data of the last 90 days | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **from_id** | **int**| If fromId is set, the data with id &gt; fromId will be returned. Otherwise the latest data will be returned | [optional] 
 **limit** | **int**| The number of data items returned each time is limited. Default 500; Max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20049]**](InlineResponse20049.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_cross_margin_collateral_ratio_get**
> list[InlineResponse20045] sapi_v1_margin_cross_margin_collateral_ratio_get()

Cross margin collateral ratio (MARKET_DATA)

 Weight(IP): 100

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))

try:
    # Cross margin collateral ratio (MARKET_DATA)
    api_response = api_instance.sapi_v1_margin_cross_margin_collateral_ratio_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_cross_margin_collateral_ratio_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20045]**](InlineResponse20045.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_cross_margin_data_get**
> list[InlineResponse20040] sapi_v1_margin_cross_margin_data_get(timestamp, signature, vip_level=vip_level, coin=coin, recv_window=recv_window)

Query Cross Margin Fee Data (USER_DATA)

Get cross margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee  Weight(IP): 1 when coin is specified; 5 when the coin parameter is omitted

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
vip_level = 56 # int | Defaults to user's vip level (optional)
coin = 'coin_example' # str | Coin name (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Cross Margin Fee Data (USER_DATA)
    api_response = api_instance.sapi_v1_margin_cross_margin_data_get(timestamp, signature, vip_level=vip_level, coin=coin, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_cross_margin_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **vip_level** | **int**| Defaults to user&#x27;s vip level | [optional] 
 **coin** | **str**| Coin name | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20040]**](InlineResponse20040.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_delist_schedule_get**
> list[InlineResponse20050] sapi_v1_margin_delist_schedule_get(timestamp, signature, recv_window=recv_window)

Get tokens or symbols delist schedule for cross margin and isolated margin (MARKET_DATA)

Get tokens or symbols delist schedule for cross margin and isolated margin  Weight(IP): 100

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get tokens or symbols delist schedule for cross margin and isolated margin (MARKET_DATA)
    api_response = api_instance.sapi_v1_margin_delist_schedule_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_delist_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20050]**](InlineResponse20050.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_dribblet_get**
> InlineResponse20044 sapi_v1_margin_dribblet_get(timestamp, signature, start_time=start_time, end_time=end_time, recv_window=recv_window)

Margin Dustlog (USER_DATA)

Query the historical information of user margin account small-value asset conversion BNB.  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Dustlog (USER_DATA)
    api_response = api_instance.sapi_v1_margin_dribblet_get(timestamp, signature, start_time=start_time, end_time=end_time, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_dribblet_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_dust_get**
> InlineResponse20052 sapi_v1_margin_dust_get(timestamp, signature, recv_window=recv_window)

Get Assets That Can Be Converted Into BNB (USER_DATA)

Get assets that can be converted into BNB.  Weight(IP): 100

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Assets That Can Be Converted Into BNB (USER_DATA)
    api_response = api_instance.sapi_v1_margin_dust_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_dust_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_dust_post**
> InlineResponse20053 sapi_v1_margin_dust_post(asset, timestamp, signature, recv_window=recv_window)

Dust Transfer (TRADE)

Convert dust assets to BNB  Weight(UID): 3000

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Dust Transfer (TRADE)
    api_response = api_instance.sapi_v1_margin_dust_post(asset, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_dust_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_exchange_small_liability_get**
> list[InlineResponse20046] sapi_v1_margin_exchange_small_liability_get(timestamp, signature, recv_window=recv_window)

Get Small Liability Exchange Coin List (USER_DATA)

Query the coins which can be small liability exchange  Weight(UID): 100

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Small Liability Exchange Coin List (USER_DATA)
    api_response = api_instance.sapi_v1_margin_exchange_small_liability_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_exchange_small_liability_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20046]**](InlineResponse20046.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_exchange_small_liability_history_get**
> InlineResponse20047 sapi_v1_margin_exchange_small_liability_history_get(timestamp, signature, current=current, size=size, start_time=start_time, end_time=end_time, recv_window=recv_window)

Get Small Liability Exchange History (USER_DATA)

Get Small liability Exchange History  Weight(UID): 100

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Small Liability Exchange History (USER_DATA)
    api_response = api_instance.sapi_v1_margin_exchange_small_liability_history_get(timestamp, signature, current=current, size=size, start_time=start_time, end_time=end_time, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_exchange_small_liability_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_force_liquidation_rec_get**
> InlineResponse20028 sapi_v1_margin_force_liquidation_rec_get(timestamp, signature, start_time=start_time, end_time=end_time, isolated_symbol=isolated_symbol, current=current, size=size, recv_window=recv_window)

Get Force Liquidation Record (USER_DATA)

- Response in descending order  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
isolated_symbol = 'isolated_symbol_example' # str | Isolated symbol (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Force Liquidation Record (USER_DATA)
    api_response = api_instance.sapi_v1_margin_force_liquidation_rec_get(timestamp, signature, start_time=start_time, end_time=end_time, isolated_symbol=isolated_symbol, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_force_liquidation_rec_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **isolated_symbol** | **str**| Isolated symbol | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_interest_history_get**
> InlineResponse20027 sapi_v1_margin_interest_history_get(timestamp, signature, asset=asset, isolated_symbol=isolated_symbol, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Get Interest History (USER_DATA)

- Response in descending order - If `isolatedSymbol` is not sent, crossed margin data will be returned - Set `archived` to `true` to query data from 6 months ago - `type` in response has 4 enums:   - `PERIODIC` interest charged per hour   - `ON_BORROW` first interest charged on borrow   - `PERIODIC_CONVERTED` interest charged per hour converted into BNB   - `ON_BORROW_CONVERTED` first interest charged on borrow converted into BNB  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
isolated_symbol = 'isolated_symbol_example' # str | Isolated symbol (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
archived = 'archived_example' # str | Default: false. Set to true for archived data from 6 months ago (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Interest History (USER_DATA)
    api_response = api_instance.sapi_v1_margin_interest_history_get(timestamp, signature, asset=asset, isolated_symbol=isolated_symbol, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_interest_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **isolated_symbol** | **str**| Isolated symbol | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **archived** | **str**| Default: false. Set to true for archived data from 6 months ago | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_interest_rate_history_get**
> list[InlineResponse20039] sapi_v1_margin_interest_rate_history_get(asset, timestamp, signature, vip_level=vip_level, start_time=start_time, end_time=end_time, recv_window=recv_window)

Margin Interest Rate History (USER_DATA)

The max interval between startTime and endTime is 30 days.  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
vip_level = 56 # int | Defaults to user's vip level (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Interest Rate History (USER_DATA)
    api_response = api_instance.sapi_v1_margin_interest_rate_history_get(asset, timestamp, signature, vip_level=vip_level, start_time=start_time, end_time=end_time, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_interest_rate_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **vip_level** | **int**| Defaults to user&#x27;s vip level | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20039]**](InlineResponse20039.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_account_delete**
> InlineResponse20036 sapi_v1_margin_isolated_account_delete(symbol, timestamp, signature, recv_window=recv_window)

Disable Isolated Margin Account (TRADE)

Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every 24 hours .  Weight(UID): 300

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Disable Isolated Margin Account (TRADE)
    api_response = api_instance.sapi_v1_margin_isolated_account_delete(symbol, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_account_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_account_get**
> IsolatedMarginAccountInfo sapi_v1_margin_isolated_account_get(timestamp, signature, symbols=symbols, recv_window=recv_window)

Query Isolated Margin Account Info (USER_DATA)

- If \"symbols\" is not sent, all isolated assets will be returned. - If \"symbols\" is sent, only the isolated assets of the sent symbols will be returned.  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
symbols = 'symbols_example' # str | Max 5 symbols can be sent; separated by ',' (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Isolated Margin Account Info (USER_DATA)
    api_response = api_instance.sapi_v1_margin_isolated_account_get(timestamp, signature, symbols=symbols, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **symbols** | **str**| Max 5 symbols can be sent; separated by &#x27;,&#x27; | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**IsolatedMarginAccountInfo**](IsolatedMarginAccountInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_account_limit_get**
> InlineResponse20037 sapi_v1_margin_isolated_account_limit_get(timestamp, signature, recv_window=recv_window)

Query Enabled Isolated Margin Account Limit (USER_DATA)

Query enabled isolated margin account limit.  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Enabled Isolated Margin Account Limit (USER_DATA)
    api_response = api_instance.sapi_v1_margin_isolated_account_limit_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_account_limit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_account_post**
> InlineResponse20036 sapi_v1_margin_isolated_account_post(symbol, timestamp, signature, recv_window=recv_window)

Enable Isolated Margin Account (TRADE)

Enable isolated margin account for a specific symbol.  Weight(UID): 300

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Enable Isolated Margin Account (TRADE)
    api_response = api_instance.sapi_v1_margin_isolated_account_post(symbol, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_all_pairs_get**
> list[InlineResponse20038] sapi_v1_margin_isolated_all_pairs_get(timestamp, signature, recv_window=recv_window)

Get All Isolated Margin Symbol(USER_DATA)

Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get All Isolated Margin Symbol(USER_DATA)
    api_response = api_instance.sapi_v1_margin_isolated_all_pairs_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_all_pairs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20038]**](InlineResponse20038.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_margin_data_get**
> list[InlineResponse20041] sapi_v1_margin_isolated_margin_data_get(timestamp, signature, vip_level=vip_level, symbol=symbol, recv_window=recv_window)

Query Isolated Margin Fee Data (USER_DATA)

Get isolated margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee  Weight(IP): 1 when a single is specified; 10 when the symbol parameter is omitted

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
vip_level = 56 # int | Defaults to user's vip level (optional)
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Isolated Margin Fee Data (USER_DATA)
    api_response = api_instance.sapi_v1_margin_isolated_margin_data_get(timestamp, signature, vip_level=vip_level, symbol=symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_margin_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **vip_level** | **int**| Defaults to user&#x27;s vip level | [optional] 
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20041]**](InlineResponse20041.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_margin_tier_get**
> list[InlineResponse20042] sapi_v1_margin_isolated_margin_tier_get(symbol, timestamp, signature, tier=tier, recv_window=recv_window)

Query Isolated Margin Tier Data (USER_DATA)

Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
tier = 'tier_example' # str | All margin tier data will be returned if tier is omitted (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Isolated Margin Tier Data (USER_DATA)
    api_response = api_instance.sapi_v1_margin_isolated_margin_tier_get(symbol, timestamp, signature, tier=tier, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_margin_tier_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **tier** | **str**| All margin tier data will be returned if tier is omitted | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20042]**](InlineResponse20042.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_pair_get**
> InlineResponse20038 sapi_v1_margin_isolated_pair_get(symbol, timestamp, signature, recv_window=recv_window)

Query Isolated Margin Symbol (USER_DATA)

Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Isolated Margin Symbol (USER_DATA)
    api_response = api_instance.sapi_v1_margin_isolated_pair_get(symbol, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_pair_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_transfer_get**
> MarginTransferDetails sapi_v1_margin_isolated_transfer_get(symbol, timestamp, signature, asset=asset, type=type, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Get Isolated Margin Transfer History (USER_DATA)

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
type = 'type_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Isolated Margin Transfer History (USER_DATA)
    api_response = api_instance.sapi_v1_margin_isolated_transfer_get(symbol, timestamp, signature, asset=asset, type=type, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_transfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**MarginTransferDetails**](MarginTransferDetails.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_isolated_transfer_post**
> object sapi_v1_margin_isolated_transfer_post(asset, symbol, trans_from, trans_to, amount, timestamp, signature, recv_window=recv_window)

Isolated Margin Account Transfer (MARGIN)

Weight(UID): 600

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
trans_from = 'trans_from_example' # str | 
trans_to = 'trans_to_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Isolated Margin Account Transfer (MARGIN)
    api_response = api_instance.sapi_v1_margin_isolated_transfer_post(asset, symbol, trans_from, trans_to, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_isolated_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **trans_from** | **str**|  | 
 **trans_to** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_leverage_bracket_get**
> list[InlineResponse20055] sapi_v1_margin_leverage_bracket_get()

Query Liability Coin Leverage Bracket in Cross Margin Pro Mode (MARKET_DATA)

Liability Coin Leverage Bracket in Cross Margin Pro Mode  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))

try:
    # Query Liability Coin Leverage Bracket in Cross Margin Pro Mode (MARKET_DATA)
    api_response = api_instance.sapi_v1_margin_leverage_bracket_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_leverage_bracket_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20055]**](InlineResponse20055.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_loan_get**
> InlineResponse20019 sapi_v1_margin_loan_get(asset, timestamp, signature, isolated_symbol=isolated_symbol, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Query Loan Record (USER_DATA)

- `txId` or `startTime` must be sent. `txId` takes precedence. - Response in descending order - If `isolatedSymbol` is not sent, crossed margin data will be returned - Set `archived` to `true` to query data from 6 months ago  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
isolated_symbol = 'isolated_symbol_example' # str | Isolated symbol (optional)
tx_id = 789 # int | the tranId in  `POST /sapi/v1/margin/loan` (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
archived = 'archived_example' # str | Default: false. Set to true for archived data from 6 months ago (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Loan Record (USER_DATA)
    api_response = api_instance.sapi_v1_margin_loan_get(asset, timestamp, signature, isolated_symbol=isolated_symbol, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_loan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **isolated_symbol** | **str**| Isolated symbol | [optional] 
 **tx_id** | **int**| the tranId in  &#x60;POST /sapi/v1/margin/loan&#x60; | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **archived** | **str**| Default: false. Set to true for archived data from 6 months ago | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_loan_post**
> Transaction sapi_v1_margin_loan_post(asset, amount, timestamp, signature, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)

Margin Account Borrow (MARGIN)

Apply for a loan.  - If \"isIsolated\" = \"TRUE\", \"symbol\" must be sent - \"isIsolated\" = \"FALSE\" for crossed margin loan  Weight(UID): 3000

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Account Borrow (MARGIN)
    api_response = api_instance.sapi_v1_margin_loan_post(asset, amount, timestamp, signature, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_loan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_manual_liquidation_post**
> list[InlineResponse20046] sapi_v1_margin_manual_liquidation_post(type, timestamp, signature, symbol=symbol)

Margin manual liquidation(MARGIN)

Margin manual liquidation  Weight(UID): 3000

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
type = 'type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
symbol = 'symbol_example' # str |  (optional)

try:
    # Margin manual liquidation(MARGIN)
    api_response = api_instance.sapi_v1_margin_manual_liquidation_post(type, timestamp, signature, symbol=symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_manual_liquidation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **symbol** | **str**|  | [optional] 

### Return type

[**list[InlineResponse20046]**](InlineResponse20046.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_max_borrowable_get**
> InlineResponse20033 sapi_v1_margin_max_borrowable_get(asset, timestamp, signature, isolated_symbol=isolated_symbol, recv_window=recv_window)

Query Max Borrow (USER_DATA)

- If `isolatedSymbol` is not sent, crossed margin data will be sent. - `borrowLimit` is also available from https://www.binance.com/en/margin-fee  Weight(IP): 50

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
isolated_symbol = 'isolated_symbol_example' # str | Isolated symbol (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Max Borrow (USER_DATA)
    api_response = api_instance.sapi_v1_margin_max_borrowable_get(asset, timestamp, signature, isolated_symbol=isolated_symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_max_borrowable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **isolated_symbol** | **str**| Isolated symbol | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_max_leverage_post**
> InlineResponse20054 sapi_v1_margin_max_leverage_post(max_leverage, timestamp, signature, recv_window=recv_window)

Adjust cross margin max leverage (USER_DATA)

Adjust cross margin max leverage  Weight(UID): 3000

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
max_leverage = 56 # int | Can only adjust 3 or 5
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Adjust cross margin max leverage (USER_DATA)
    api_response = api_instance.sapi_v1_margin_max_leverage_post(max_leverage, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_max_leverage_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_leverage** | **int**| Can only adjust 3 or 5 | 
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

# **sapi_v1_margin_max_transferable_get**
> InlineResponse20034 sapi_v1_margin_max_transferable_get(asset, timestamp, signature, isolated_symbol=isolated_symbol, recv_window=recv_window)

Query Max Transfer-Out Amount (USER_DATA)

- If `isolatedSymbol` is not sent, crossed margin data will be sent.  Weight(IP): 50

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
isolated_symbol = 'isolated_symbol_example' # str | Isolated symbol (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Max Transfer-Out Amount (USER_DATA)
    api_response = api_instance.sapi_v1_margin_max_transferable_get(asset, timestamp, signature, isolated_symbol=isolated_symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_max_transferable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **isolated_symbol** | **str**| Isolated symbol | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_my_trades_get**
> list[MarginTrade] sapi_v1_margin_my_trades_get(symbol, timestamp, signature, is_isolated=is_isolated, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)

Query Margin Account's Trade List (USER_DATA)

- If `fromId` is set, it will get orders >= that `fromId`. Otherwise most recent trades are returned.  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
from_id = 789 # int | Trade id to fetch from. Default gets most recent trades. (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Margin Account's Trade List (USER_DATA)
    api_response = api_instance.sapi_v1_margin_my_trades_get(symbol, timestamp, signature, is_isolated=is_isolated, start_time=start_time, end_time=end_time, from_id=from_id, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_my_trades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **from_id** | **int**| Trade id to fetch from. Default gets most recent trades. | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[MarginTrade]**](MarginTrade.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_next_hourly_interest_rate_get**
> list[InlineResponse20048] sapi_v1_margin_next_hourly_interest_rate_get(timestamp, signature, assets=assets, is_isolated=is_isolated, recv_window=recv_window)

Get a future hourly interest rate (USER_DATA)

Get user the next hourly estimate interest  Weight(UID): 100

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
assets = 'assets_example' # str | List of assets, separated by commas, up to 20 (optional)
is_isolated = 'is_isolated_example' # str | for isolated margin or not, \"TRUE\", \"FALSE\" (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get a future hourly interest rate (USER_DATA)
    api_response = api_instance.sapi_v1_margin_next_hourly_interest_rate_get(timestamp, signature, assets=assets, is_isolated=is_isolated, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_next_hourly_interest_rate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **assets** | **str**| List of assets, separated by commas, up to 20 | [optional] 
 **is_isolated** | **str**| for isolated margin or not, \&quot;TRUE\&quot;, \&quot;FALSE\&quot; | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20048]**](InlineResponse20048.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_open_order_list_get**
> list[InlineResponse20032] sapi_v1_margin_open_order_list_get(timestamp, signature, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)

Query Margin Account's Open OCO (USER_DATA)

Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
symbol = 'symbol_example' # str | Mandatory for isolated margin, not supported for cross margin (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Margin Account's Open OCO (USER_DATA)
    api_response = api_instance.sapi_v1_margin_open_order_list_get(timestamp, signature, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_open_order_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **symbol** | **str**| Mandatory for isolated margin, not supported for cross margin | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20032]**](InlineResponse20032.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_open_orders_delete**
> list[object] sapi_v1_margin_open_orders_delete(symbol, timestamp, signature, is_isolated=is_isolated, recv_window=recv_window)

Margin Account Cancel all Open Orders on a Symbol (TRADE)

- Cancels all active orders on a symbol for margin account. - This includes OCO orders.  Weight(IP): 1 

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Account Cancel all Open Orders on a Symbol (TRADE)
    api_response = api_instance.sapi_v1_margin_open_orders_delete(symbol, timestamp, signature, is_isolated=is_isolated, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_open_orders_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

**list[object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_open_orders_get**
> list[MarginOrderDetail] sapi_v1_margin_open_orders_get(timestamp, signature, symbol=symbol, is_isolated=is_isolated, recv_window=recv_window)

Query Margin Account's Open Orders (USER_DATA)

- If the `symbol` is not sent, orders for all symbols will be returned in an array. - When all symbols are returned, the number of requests counted against the rate limiter is equal to the number of symbols currently trading on the exchange - If isIsolated =\"TRUE\", symbol must be sent.  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Margin Account's Open Orders (USER_DATA)
    api_response = api_instance.sapi_v1_margin_open_orders_get(timestamp, signature, symbol=symbol, is_isolated=is_isolated, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_open_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[MarginOrderDetail]**](MarginOrderDetail.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_order_delete**
> MarginOrder sapi_v1_margin_order_delete(symbol, timestamp, signature, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Margin Account Cancel Order (TRADE)

Cancel an active order for margin account.  Either `orderId` or `origClientOrderId` must be sent.  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
order_id = 789 # int | Order id (optional)
orig_client_order_id = 'orig_client_order_id_example' # str | Order id from client (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Account Cancel Order (TRADE)
    api_response = api_instance.sapi_v1_margin_order_delete(symbol, timestamp, signature, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_order_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **order_id** | **int**| Order id | [optional] 
 **orig_client_order_id** | **str**| Order id from client | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**MarginOrder**](MarginOrder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_order_get**
> MarginOrderDetail sapi_v1_margin_order_get(symbol, timestamp, signature, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account's Order (USER_DATA)

- Either `orderId` or `origClientOrderId` must be sent. - For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
order_id = 789 # int | Order id (optional)
orig_client_order_id = 'orig_client_order_id_example' # str | Order id from client (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Margin Account's Order (USER_DATA)
    api_response = api_instance.sapi_v1_margin_order_get(symbol, timestamp, signature, is_isolated=is_isolated, order_id=order_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_order_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **order_id** | **int**| Order id | [optional] 
 **orig_client_order_id** | **str**| Order id from client | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**MarginOrderDetail**](MarginOrderDetail.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_order_list_delete**
> MarginOcoOrder sapi_v1_margin_order_list_delete(symbol, timestamp, signature, is_isolated=is_isolated, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)

Margin Account Cancel OCO (TRADE)

Cancel an entire Order List for a margin account  - Canceling an individual leg will cancel the entire OCO - Either `orderListId` or `listClientOrderId` must be provided  Weight(UID): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
order_list_id = 789 # int | Order list id (optional)
list_client_order_id = 'list_client_order_id_example' # str | A unique Id for the entire orderList (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Account Cancel OCO (TRADE)
    api_response = api_instance.sapi_v1_margin_order_list_delete(symbol, timestamp, signature, is_isolated=is_isolated, order_list_id=order_list_id, list_client_order_id=list_client_order_id, new_client_order_id=new_client_order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_order_list_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **order_list_id** | **int**| Order list id | [optional] 
 **list_client_order_id** | **str**| A unique Id for the entire orderList | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**MarginOcoOrder**](MarginOcoOrder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_order_list_get**
> InlineResponse20031 sapi_v1_margin_order_list_get(timestamp, signature, is_isolated=is_isolated, symbol=symbol, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)

Query Margin Account's OCO (USER_DATA)

Retrieves a specific OCO based on provided optional parameters  - Either `orderListId` or `origClientOrderId` must be provided  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
symbol = 'symbol_example' # str | Mandatory for isolated margin, not supported for cross margin (optional)
order_list_id = 789 # int | Order list id (optional)
orig_client_order_id = 'orig_client_order_id_example' # str | Order id from client (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Margin Account's OCO (USER_DATA)
    api_response = api_instance.sapi_v1_margin_order_list_get(timestamp, signature, is_isolated=is_isolated, symbol=symbol, order_list_id=order_list_id, orig_client_order_id=orig_client_order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_order_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **symbol** | **str**| Mandatory for isolated margin, not supported for cross margin | [optional] 
 **order_list_id** | **int**| Order list id | [optional] 
 **orig_client_order_id** | **str**| Order id from client | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_order_oco_post**
> InlineResponse20030 sapi_v1_margin_order_oco_post(symbol, side, quantity, price, stop_price, timestamp, signature, is_isolated=is_isolated, list_client_order_id=list_client_order_id, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, stop_client_order_id=stop_client_order_id, stop_limit_price=stop_limit_price, stop_iceberg_qty=stop_iceberg_qty, stop_limit_time_in_force=stop_limit_time_in_force, new_order_resp_type=new_order_resp_type, side_effect_type=side_effect_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)

Margin Account New OCO (TRADE)

Send in a new OCO for a margin account  - Price Restrictions:   - SELL: Limit Price > Last Price > Stop Price   - BUY: Limit Price < Last Price < Stop Price - Quantity Restrictions:   - Both legs must have the same quantity   - ICEBERG quantities however do not have to be the same. - Order Rate Limit   - OCO counts as 2 orders against the order rate limit.  Weight(UID): 6

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
quantity = 1.2 # float | 
price = 1.2 # float | Order price
stop_price = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
list_client_order_id = 'list_client_order_id_example' # str | A unique Id for the entire orderList (optional)
limit_client_order_id = 'limit_client_order_id_example' # str | A unique Id for the limit order (optional)
limit_iceberg_qty = 1.2 # float |  (optional)
stop_client_order_id = 'stop_client_order_id_example' # str | A unique Id for the stop loss/stop loss limit leg (optional)
stop_limit_price = 1.2 # float | If provided, stopLimitTimeInForce is required. (optional)
stop_iceberg_qty = 1.2 # float |  (optional)
stop_limit_time_in_force = 'stop_limit_time_in_force_example' # str |  (optional)
new_order_resp_type = 'new_order_resp_type_example' # str | Set the response JSON. (optional)
side_effect_type = 'side_effect_type_example' # str | Default `NO_SIDE_EFFECT` (optional)
self_trade_prevention_mode = 'self_trade_prevention_mode_example' # str | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Account New OCO (TRADE)
    api_response = api_instance.sapi_v1_margin_order_oco_post(symbol, side, quantity, price, stop_price, timestamp, signature, is_isolated=is_isolated, list_client_order_id=list_client_order_id, limit_client_order_id=limit_client_order_id, limit_iceberg_qty=limit_iceberg_qty, stop_client_order_id=stop_client_order_id, stop_limit_price=stop_limit_price, stop_iceberg_qty=stop_iceberg_qty, stop_limit_time_in_force=stop_limit_time_in_force, new_order_resp_type=new_order_resp_type, side_effect_type=side_effect_type, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_order_oco_post: %s\n" % e)
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
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **list_client_order_id** | **str**| A unique Id for the entire orderList | [optional] 
 **limit_client_order_id** | **str**| A unique Id for the limit order | [optional] 
 **limit_iceberg_qty** | **float**|  | [optional] 
 **stop_client_order_id** | **str**| A unique Id for the stop loss/stop loss limit leg | [optional] 
 **stop_limit_price** | **float**| If provided, stopLimitTimeInForce is required. | [optional] 
 **stop_iceberg_qty** | **float**|  | [optional] 
 **stop_limit_time_in_force** | **str**|  | [optional] 
 **new_order_resp_type** | **str**| Set the response JSON. | [optional] 
 **side_effect_type** | **str**| Default &#x60;NO_SIDE_EFFECT&#x60; | [optional] 
 **self_trade_prevention_mode** | **str**| The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_order_post**
> InlineResponse20026 sapi_v1_margin_order_post(symbol, side, type, quantity, auto_repay_at_cancel, timestamp, signature, is_isolated=is_isolated, quote_order_qty=quote_order_qty, price=price, stop_price=stop_price, new_client_order_id=new_client_order_id, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, side_effect_type=side_effect_type, time_in_force=time_in_force, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)

Margin Account New Order (TRADE)

Post a new order for margin account.  Weight(UID): 6

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT
side = 'side_example' # str | 
type = 'type_example' # str | Order type
quantity = 1.2 # float | 
auto_repay_at_cancel = true # bool | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
quote_order_qty = 1.2 # float | Quote quantity (optional)
price = 1.2 # float | Order price (optional)
stop_price = 1.2 # float | Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. (optional)
new_client_order_id = 'new_client_order_id_example' # str | Used to uniquely identify this cancel. Automatically generated by default (optional)
iceberg_qty = 1.2 # float | Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. (optional)
new_order_resp_type = 'new_order_resp_type_example' # str | Set the response JSON. (optional)
side_effect_type = 'side_effect_type_example' # str | Default `NO_SIDE_EFFECT` (optional)
time_in_force = 'time_in_force_example' # str | Order time in force (optional)
self_trade_prevention_mode = 'self_trade_prevention_mode_example' # str | The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Account New Order (TRADE)
    api_response = api_instance.sapi_v1_margin_order_post(symbol, side, type, quantity, auto_repay_at_cancel, timestamp, signature, is_isolated=is_isolated, quote_order_qty=quote_order_qty, price=price, stop_price=stop_price, new_client_order_id=new_client_order_id, iceberg_qty=iceberg_qty, new_order_resp_type=new_order_resp_type, side_effect_type=side_effect_type, time_in_force=time_in_force, self_trade_prevention_mode=self_trade_prevention_mode, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 
 **side** | **str**|  | 
 **type** | **str**| Order type | 
 **quantity** | **float**|  | 
 **auto_repay_at_cancel** | **bool**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **quote_order_qty** | **float**| Quote quantity | [optional] 
 **price** | **float**| Order price | [optional] 
 **stop_price** | **float**| Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders. | [optional] 
 **new_client_order_id** | **str**| Used to uniquely identify this cancel. Automatically generated by default | [optional] 
 **iceberg_qty** | **float**| Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order. | [optional] 
 **new_order_resp_type** | **str**| Set the response JSON. | [optional] 
 **side_effect_type** | **str**| Default &#x60;NO_SIDE_EFFECT&#x60; | [optional] 
 **time_in_force** | **str**| Order time in force | [optional] 
 **self_trade_prevention_mode** | **str**| The allowed enums is dependent on what is configured on the symbol. The possible supported values are EXPIRE_TAKER, EXPIRE_MAKER, EXPIRE_BOTH, NONE. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_pair_get**
> InlineResponse20022 sapi_v1_margin_pair_get(symbol)

Query Cross Margin Pair (MARKET_DATA)

Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT

try:
    # Query Cross Margin Pair (MARKET_DATA)
    api_response = api_instance.sapi_v1_margin_pair_get(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_pair_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_price_index_get**
> InlineResponse20025 sapi_v1_margin_price_index_get(symbol)

Query Margin PriceIndex (MARKET_DATA)

Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT

try:
    # Query Margin PriceIndex (MARKET_DATA)
    api_response = api_instance.sapi_v1_margin_price_index_get(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_price_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_rate_limit_order_get**
> list[InlineResponse20043] sapi_v1_margin_rate_limit_order_get(timestamp, signature, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)

Query Current Margin Order Count Usage (TRADE)

Displays the user's current margin order count usage for all intervals.  Weight(IP): 20

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
symbol = 'symbol_example' # str | isolated symbol, mandatory for isolated margin (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Current Margin Order Count Usage (TRADE)
    api_response = api_instance.sapi_v1_margin_rate_limit_order_get(timestamp, signature, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_rate_limit_order_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **symbol** | **str**| isolated symbol, mandatory for isolated margin | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20043]**](InlineResponse20043.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_repay_get**
> InlineResponse20020 sapi_v1_margin_repay_get(asset, timestamp, signature, isolated_symbol=isolated_symbol, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Query Repay Record (USER_DATA)

- `txId` or `startTime` must be sent. `txId` takes precedence. - Response in descending order - If `isolatedSymbol` is not sent, crossed margin data will be returned - Set `archived` to `true` to query data from 6 months ago  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
isolated_symbol = 'isolated_symbol_example' # str | Isolated symbol (optional)
tx_id = 789 # int | the tranId in  `POST /sapi/v1/margin/repay` (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
archived = 'archived_example' # str | Default: false. Set to true for archived data from 6 months ago (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Repay Record (USER_DATA)
    api_response = api_instance.sapi_v1_margin_repay_get(asset, timestamp, signature, isolated_symbol=isolated_symbol, tx_id=tx_id, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_repay_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **isolated_symbol** | **str**| Isolated symbol | [optional] 
 **tx_id** | **int**| the tranId in  &#x60;POST /sapi/v1/margin/repay&#x60; | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **archived** | **str**| Default: false. Set to true for archived data from 6 months ago | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_repay_post**
> Transaction sapi_v1_margin_repay_post(asset, amount, timestamp, signature, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)

Margin Account Repay (MARGIN)

Repay loan for margin account.  - If \"isIsolated\" = \"TRUE\", \"symbol\" must be sent - \"isIsolated\" = \"FALSE\" for crossed margin repay  Weight(IP): 3000

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
is_isolated = 'is_isolated_example' # str | * `TRUE` - For isolated margin * `FALSE` - Default, not for isolated margin (optional)
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Account Repay (MARGIN)
    api_response = api_instance.sapi_v1_margin_repay_post(asset, amount, timestamp, signature, is_isolated=is_isolated, symbol=symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_repay_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **is_isolated** | **str**| * &#x60;TRUE&#x60; - For isolated margin * &#x60;FALSE&#x60; - Default, not for isolated margin | [optional] 
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_trade_coeff_get**
> InlineResponse20035 sapi_v1_margin_trade_coeff_get(email, timestamp, signature, recv_window=recv_window)

Get Summary of Margin account (USER_DATA)

Get personal margin level information  Weight(IP): 10

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Email Address
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Summary of Margin account (USER_DATA)
    api_response = api_instance.sapi_v1_margin_trade_coeff_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_trade_coeff_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email Address | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_transfer_get**
> InlineResponse20018 sapi_v1_margin_transfer_get(timestamp, signature, asset=asset, type=type, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)

Get Cross Margin Transfer History (USER_DATA)

- Response in descending order - Returns data for last 7 days by default - Set `archived` to `true` to query data from 6 months ago  Weight(IP): 1

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
type = 'type_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
archived = 'archived_example' # str | Default: false. Set to true for archived data from 6 months ago (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Cross Margin Transfer History (USER_DATA)
    api_response = api_instance.sapi_v1_margin_transfer_get(timestamp, signature, asset=asset, type=type, start_time=start_time, end_time=end_time, current=current, size=size, archived=archived, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_transfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **archived** | **str**| Default: false. Set to true for archived data from 6 months ago | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_margin_transfer_post**
> Transaction sapi_v1_margin_transfer_post(asset, amount, type, timestamp, signature, recv_window=recv_window)

Cross Margin Account Transfer (MARGIN)

Execute transfer between spot account and cross margin account.  Weight(IP): 600

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
api_instance = binance_spot.MarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
amount = 1.2 # float | 
type = 56 # int | * `1` - transfer from main account to margin account * `2` - transfer from margin account to main account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Cross Margin Account Transfer (MARGIN)
    api_response = api_instance.sapi_v1_margin_transfer_post(asset, amount, type, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->sapi_v1_margin_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **type** | **int**| * &#x60;1&#x60; - transfer from main account to margin account * &#x60;2&#x60; - transfer from margin account to main account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

