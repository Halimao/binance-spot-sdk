# binance_spot.CryptoLoansApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_loan_adjust_ltv_post**](CryptoLoansApi.md#sapi_v1_loan_adjust_ltv_post) | **POST** /sapi/v1/loan/adjust/ltv | Crypto Loan Adjust LTV (TRADE)
[**sapi_v1_loan_borrow_history_get**](CryptoLoansApi.md#sapi_v1_loan_borrow_history_get) | **GET** /sapi/v1/loan/borrow/history | Get Crypto Loans Borrow History (USER_DATA)
[**sapi_v1_loan_borrow_post**](CryptoLoansApi.md#sapi_v1_loan_borrow_post) | **POST** /sapi/v1/loan/borrow | Crypto Loan Borrow (TRADE)
[**sapi_v1_loan_collateral_data_get**](CryptoLoansApi.md#sapi_v1_loan_collateral_data_get) | **GET** /sapi/v1/loan/collateral/data | Get Collateral Assets Data (USER_DATA)
[**sapi_v1_loan_customize_margin_call_post**](CryptoLoansApi.md#sapi_v1_loan_customize_margin_call_post) | **POST** /sapi/v1/loan/customize/margin_call | Crypto Loan Customize Margin Call (TRADE)
[**sapi_v1_loan_flexible_adjust_ltv_post**](CryptoLoansApi.md#sapi_v1_loan_flexible_adjust_ltv_post) | **POST** /sapi/v1/loan/flexible/adjust/ltv | Adjust LTV - Flexible Loan Adjust LTV (TRADE)
[**sapi_v1_loan_flexible_borrow_history_get**](CryptoLoansApi.md#sapi_v1_loan_flexible_borrow_history_get) | **GET** /sapi/v1/loan/flexible/borrow/history | Borrow - Get Flexible Loan Borrow History (USER_DATA)
[**sapi_v1_loan_flexible_borrow_post**](CryptoLoansApi.md#sapi_v1_loan_flexible_borrow_post) | **POST** /sapi/v1/loan/flexible/borrow | Borrow - Flexible Loan Borrow (TRADE)
[**sapi_v1_loan_flexible_collateral_data_get**](CryptoLoansApi.md#sapi_v1_loan_flexible_collateral_data_get) | **GET** /sapi/v1/loan/flexible/collateral/data | Get Flexible Loan Collateral Assets Data (USER_DATA)
[**sapi_v1_loan_flexible_loanable_data_get**](CryptoLoansApi.md#sapi_v1_loan_flexible_loanable_data_get) | **GET** /sapi/v1/loan/flexible/loanable/data | Get Flexible Loan Assets Data (USER_DATA)
[**sapi_v1_loan_flexible_ltv_adjustment_history_get**](CryptoLoansApi.md#sapi_v1_loan_flexible_ltv_adjustment_history_get) | **GET** /sapi/v1/loan/flexible/ltv/adjustment/history | Adjust LTV - Get Flexible Loan LTV Adjustment History (USER_DATA)
[**sapi_v1_loan_flexible_ongoing_orders_get**](CryptoLoansApi.md#sapi_v1_loan_flexible_ongoing_orders_get) | **GET** /sapi/v1/loan/flexible/ongoing/orders | Borrow - Get Flexible Loan Ongoing Orders (USER_DATA)
[**sapi_v1_loan_flexible_repay_history_get**](CryptoLoansApi.md#sapi_v1_loan_flexible_repay_history_get) | **GET** /sapi/v1/loan/flexible/repay/history | Repay - Get Flexible Loan Repayment History (USER_DATA)
[**sapi_v1_loan_flexible_repay_post**](CryptoLoansApi.md#sapi_v1_loan_flexible_repay_post) | **POST** /sapi/v1/loan/flexible/repay | Repay - Flexible Loan Repay (TRADE)
[**sapi_v1_loan_income_get**](CryptoLoansApi.md#sapi_v1_loan_income_get) | **GET** /sapi/v1/loan/income | Get Crypto Loans Income History (USER_DATA)
[**sapi_v1_loan_loanable_data_get**](CryptoLoansApi.md#sapi_v1_loan_loanable_data_get) | **GET** /sapi/v1/loan/loanable/data | Get Loanable Assets Data (USER_DATA)
[**sapi_v1_loan_ltv_adjustment_history_get**](CryptoLoansApi.md#sapi_v1_loan_ltv_adjustment_history_get) | **GET** /sapi/v1/loan/ltv/adjustment/history | Get Loan LTV Adjustment History (USER_DATA)
[**sapi_v1_loan_ongoing_orders_get**](CryptoLoansApi.md#sapi_v1_loan_ongoing_orders_get) | **GET** /sapi/v1/loan/ongoing/orders | Get Loan Ongoing Orders (USER_DATA)
[**sapi_v1_loan_repay_collateral_rate_get**](CryptoLoansApi.md#sapi_v1_loan_repay_collateral_rate_get) | **GET** /sapi/v1/loan/repay/collateral/rate | Check Collateral Repay Rate (USER_DATA)
[**sapi_v1_loan_repay_history_get**](CryptoLoansApi.md#sapi_v1_loan_repay_history_get) | **GET** /sapi/v1/loan/repay/history | Get Loan Repayment History (USER_DATA)
[**sapi_v1_loan_repay_post**](CryptoLoansApi.md#sapi_v1_loan_repay_post) | **POST** /sapi/v1/loan/repay | Crypto Loan Repay (TRADE)

# **sapi_v1_loan_adjust_ltv_post**
> InlineResponse200208 sapi_v1_loan_adjust_ltv_post(order_id, amount, direction, timestamp, signature, recv_window=recv_window)

Crypto Loan Adjust LTV (TRADE)

Weight(UID): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
order_id = 789 # int | Order ID
amount = 1.2 # float | Amount
direction = 'direction_example' # str | 'ADDITIONAL', 'REDUCED'
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Crypto Loan Adjust LTV (TRADE)
    api_response = api_instance.sapi_v1_loan_adjust_ltv_post(order_id, amount, direction, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_adjust_ltv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID | 
 **amount** | **float**| Amount | 
 **direction** | **str**| &#x27;ADDITIONAL&#x27;, &#x27;REDUCED&#x27; | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200208**](InlineResponse200208.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_borrow_history_get**
> InlineResponse200204 sapi_v1_loan_borrow_history_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Crypto Loans Borrow History (USER_DATA)

- If startTime and endTime are not sent, the recent 90-day data will be returned. - The max interval between startTime and endTime is 180 days.  Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | orderId in POST /sapi/v1/loan/borrow (optional)
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 789 # int | default 10, max 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Crypto Loans Borrow History (USER_DATA)
    api_response = api_instance.sapi_v1_loan_borrow_history_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_borrow_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| orderId in POST /sapi/v1/loan/borrow | [optional] 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| default 10, max 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200204**](InlineResponse200204.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_borrow_post**
> InlineResponse200203 sapi_v1_loan_borrow_post(loan_coin, collateral_coin, loan_term, timestamp, signature, loan_amount=loan_amount, collateral_amount=collateral_amount, recv_window=recv_window)

Crypto Loan Borrow (TRADE)

Weight(UID): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
loan_coin = 'loan_coin_example' # str | Coin loaned
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral
loan_term = 56 # int | 7/14/30/90/180 days
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_amount = 3.4 # float | Loan amount (optional)
collateral_amount = 3.4 # float |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Crypto Loan Borrow (TRADE)
    api_response = api_instance.sapi_v1_loan_borrow_post(loan_coin, collateral_coin, loan_term, timestamp, signature, loan_amount=loan_amount, collateral_amount=collateral_amount, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_borrow_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_coin** | **str**| Coin loaned | 
 **collateral_coin** | **str**| Coin used as collateral | 
 **loan_term** | **int**| 7/14/30/90/180 days | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_amount** | **float**| Loan amount | [optional] 
 **collateral_amount** | **float**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200203**](InlineResponse200203.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_collateral_data_get**
> InlineResponse200211 sapi_v1_loan_collateral_data_get(timestamp, signature, collateral_coin=collateral_coin, vip_level=vip_level, recv_window=recv_window)

Get Collateral Assets Data (USER_DATA)

Get LTV information and collateral limit of collateral assets. The collateral limit is shown in USD value.  Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
vip_level = 56 # int | Defaults to user's vip level (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Collateral Assets Data (USER_DATA)
    api_response = api_instance.sapi_v1_loan_collateral_data_get(timestamp, signature, collateral_coin=collateral_coin, vip_level=vip_level, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_collateral_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **vip_level** | **int**| Defaults to user&#x27;s vip level | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200211**](InlineResponse200211.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_customize_margin_call_post**
> InlineResponse200213 sapi_v1_loan_customize_margin_call_post(margin_call, timestamp, signature, order_id=order_id, collateral_coin=collateral_coin, recv_window=recv_window)

Crypto Loan Customize Margin Call (TRADE)

Customize margin call for ongoing orders only.  Weight(UID): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
margin_call = 3.4 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Mandatory when collateralCoin is empty. Send either orderId or collateralCoin, if both parameters are sent, take orderId only. (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Crypto Loan Customize Margin Call (TRADE)
    api_response = api_instance.sapi_v1_loan_customize_margin_call_post(margin_call, timestamp, signature, order_id=order_id, collateral_coin=collateral_coin, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_customize_margin_call_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **margin_call** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Mandatory when collateralCoin is empty. Send either orderId or collateralCoin, if both parameters are sent, take orderId only. | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200213**](InlineResponse200213.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_adjust_ltv_post**
> InlineResponse200219 sapi_v1_loan_flexible_adjust_ltv_post(adjustment_amount, direction, timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, recv_window=recv_window)

Adjust LTV - Flexible Loan Adjust LTV (TRADE)

 Weight(UID): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
adjustment_amount = 3.4 # float | 
direction = 'direction_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Adjust LTV - Flexible Loan Adjust LTV (TRADE)
    api_response = api_instance.sapi_v1_loan_flexible_adjust_ltv_post(adjustment_amount, direction, timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_adjust_ltv_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adjustment_amount** | **float**|  | 
 **direction** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200219**](InlineResponse200219.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_borrow_history_get**
> InlineResponse200216 sapi_v1_loan_flexible_borrow_history_get(timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Borrow - Get Flexible Loan Borrow History (USER_DATA)

 Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Borrow - Get Flexible Loan Borrow History (USER_DATA)
    api_response = api_instance.sapi_v1_loan_flexible_borrow_history_get(timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_borrow_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200216**](InlineResponse200216.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_borrow_post**
> InlineResponse200214 sapi_v1_loan_flexible_borrow_post(timestamp, signature, loan_coin=loan_coin, loan_amount=loan_amount, collateral_coin=collateral_coin, collateral_amount=collateral_amount, recv_window=recv_window)

Borrow - Flexible Loan Borrow (TRADE)

 Weight(UID): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
loan_amount = 3.4 # float | Loan amount (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
collateral_amount = 3.4 # float |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Borrow - Flexible Loan Borrow (TRADE)
    api_response = api_instance.sapi_v1_loan_flexible_borrow_post(timestamp, signature, loan_coin=loan_coin, loan_amount=loan_amount, collateral_coin=collateral_coin, collateral_amount=collateral_amount, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_borrow_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **loan_amount** | **float**| Loan amount | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **collateral_amount** | **float**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200214**](InlineResponse200214.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_collateral_data_get**
> InlineResponse200222 sapi_v1_loan_flexible_collateral_data_get(timestamp, signature, collateral_coin=collateral_coin, recv_window=recv_window)

Get Flexible Loan Collateral Assets Data (USER_DATA)

Get LTV information and collateral limit of flexible loan's collateral assets. The collateral limit is shown in USD value.  Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Flexible Loan Collateral Assets Data (USER_DATA)
    api_response = api_instance.sapi_v1_loan_flexible_collateral_data_get(timestamp, signature, collateral_coin=collateral_coin, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_collateral_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200222**](InlineResponse200222.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_loanable_data_get**
> InlineResponse200221 sapi_v1_loan_flexible_loanable_data_get(timestamp, signature, loan_coin=loan_coin, recv_window=recv_window)

Get Flexible Loan Assets Data (USER_DATA)

Get interest rate and borrow limit of flexible loanable assets. The borrow limit is shown in USD value.  Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Flexible Loan Assets Data (USER_DATA)
    api_response = api_instance.sapi_v1_loan_flexible_loanable_data_get(timestamp, signature, loan_coin=loan_coin, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_loanable_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200221**](InlineResponse200221.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_ltv_adjustment_history_get**
> InlineResponse200220 sapi_v1_loan_flexible_ltv_adjustment_history_get(timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Adjust LTV - Get Flexible Loan LTV Adjustment History (USER_DATA)

 Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Adjust LTV - Get Flexible Loan LTV Adjustment History (USER_DATA)
    api_response = api_instance.sapi_v1_loan_flexible_ltv_adjustment_history_get(timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_ltv_adjustment_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200220**](InlineResponse200220.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_ongoing_orders_get**
> InlineResponse200215 sapi_v1_loan_flexible_ongoing_orders_get(timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)

Borrow - Get Flexible Loan Ongoing Orders (USER_DATA)

 Weight(IP): 300

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Borrow - Get Flexible Loan Ongoing Orders (USER_DATA)
    api_response = api_instance.sapi_v1_loan_flexible_ongoing_orders_get(timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_ongoing_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200215**](InlineResponse200215.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_repay_history_get**
> InlineResponse200218 sapi_v1_loan_flexible_repay_history_get(timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Repay - Get Flexible Loan Repayment History (USER_DATA)

 Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Repay - Get Flexible Loan Repayment History (USER_DATA)
    api_response = api_instance.sapi_v1_loan_flexible_repay_history_get(timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_repay_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200218**](InlineResponse200218.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_flexible_repay_post**
> InlineResponse200217 sapi_v1_loan_flexible_repay_post(repay_amount, timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, collateral_return=collateral_return, full_repayment=full_repayment, recv_window=recv_window)

Repay - Flexible Loan Repay (TRADE)

 Weight(IP): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
repay_amount = 3.4 # float | repay amount of loanCoin
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
collateral_return = true # bool |  (optional)
full_repayment = true # bool |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Repay - Flexible Loan Repay (TRADE)
    api_response = api_instance.sapi_v1_loan_flexible_repay_post(repay_amount, timestamp, signature, loan_coin=loan_coin, collateral_coin=collateral_coin, collateral_return=collateral_return, full_repayment=full_repayment, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_flexible_repay_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repay_amount** | **float**| repay amount of loanCoin | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **collateral_return** | **bool**|  | [optional] 
 **full_repayment** | **bool**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200217**](InlineResponse200217.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_income_get**
> list[InlineResponse200202] sapi_v1_loan_income_get(timestamp, signature, asset=asset, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Get Crypto Loans Income History (USER_DATA)

- If startTime and endTime are not sent, the recent 7-day data will be returned. - The max interval between startTime and endTime is 30 days.  Weight(UID): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
type = 'type_example' # str | All types will be returned by default.   * `borrowIn`   * `collateralSpent`   * `repayAmount`   * `collateralReturn` - Collateral return after repayment   * `addCollateral`   * `removeCollateral`   * `collateralReturnAfterLiquidation` (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | default 20, max 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Crypto Loans Income History (USER_DATA)
    api_response = api_instance.sapi_v1_loan_income_get(timestamp, signature, asset=asset, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_income_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **type** | **str**| All types will be returned by default.   * &#x60;borrowIn&#x60;   * &#x60;collateralSpent&#x60;   * &#x60;repayAmount&#x60;   * &#x60;collateralReturn&#x60; - Collateral return after repayment   * &#x60;addCollateral&#x60;   * &#x60;removeCollateral&#x60;   * &#x60;collateralReturnAfterLiquidation&#x60; | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| default 20, max 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200202]**](InlineResponse200202.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_loanable_data_get**
> InlineResponse200210 sapi_v1_loan_loanable_data_get(timestamp, signature, loan_coin=loan_coin, vip_level=vip_level, recv_window=recv_window)

Get Loanable Assets Data (USER_DATA)

Get interest rate and borrow limit of loanable assets. The borrow limit is shown in USD value.  Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
vip_level = 56 # int | Defaults to user's vip level (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Loanable Assets Data (USER_DATA)
    api_response = api_instance.sapi_v1_loan_loanable_data_get(timestamp, signature, loan_coin=loan_coin, vip_level=vip_level, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_loanable_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **vip_level** | **int**| Defaults to user&#x27;s vip level | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200210**](InlineResponse200210.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_ltv_adjustment_history_get**
> InlineResponse200209 sapi_v1_loan_ltv_adjustment_history_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Loan LTV Adjustment History (USER_DATA)

If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between startTime and endTime is 180 days.  Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order ID (optional)
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 789 # int | default 10, max 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Loan LTV Adjustment History (USER_DATA)
    api_response = api_instance.sapi_v1_loan_ltv_adjustment_history_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_ltv_adjustment_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order ID | [optional] 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| default 10, max 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200209**](InlineResponse200209.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_ongoing_orders_get**
> InlineResponse200205 sapi_v1_loan_ongoing_orders_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)

Get Loan Ongoing Orders (USER_DATA)

Weight(IP): 300

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | orderId in POST /sapi/v1/loan/borrow (optional)
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
current = 56 # int | Current querying page. Start from 1; default:1, max:1000 (optional)
limit = 789 # int | default 10, max 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Loan Ongoing Orders (USER_DATA)
    api_response = api_instance.sapi_v1_loan_ongoing_orders_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_ongoing_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| orderId in POST /sapi/v1/loan/borrow | [optional] 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **current** | **int**| Current querying page. Start from 1; default:1, max:1000 | [optional] 
 **limit** | **int**| default 10, max 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200205**](InlineResponse200205.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_repay_collateral_rate_get**
> InlineResponse200212 sapi_v1_loan_repay_collateral_rate_get(loan_coin, collateral_coin, repay_amount, timestamp, signature, recv_window=recv_window)

Check Collateral Repay Rate (USER_DATA)

Get the the rate of collateral coin / loan coin when using collateral repay, the rate will be valid within 8 second.  Weight(IP): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
loan_coin = 'loan_coin_example' # str | Coin loaned
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral
repay_amount = 3.4 # float | repay amount of loanCoin
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Check Collateral Repay Rate (USER_DATA)
    api_response = api_instance.sapi_v1_loan_repay_collateral_rate_get(loan_coin, collateral_coin, repay_amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_repay_collateral_rate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_coin** | **str**| Coin loaned | 
 **collateral_coin** | **str**| Coin used as collateral | 
 **repay_amount** | **float**| repay amount of loanCoin | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200212**](InlineResponse200212.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_repay_history_get**
> InlineResponse200207 sapi_v1_loan_repay_history_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get Loan Repayment History (USER_DATA)

If startTime and endTime are not sent, the recent 90-day data will be returned. The max interval between startTime and endTime is 180 days.  Weight(IP): 400

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order ID (optional)
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 789 # int | default 10, max 100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Loan Repayment History (USER_DATA)
    api_response = api_instance.sapi_v1_loan_repay_history_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, collateral_coin=collateral_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_repay_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order ID | [optional] 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| default 10, max 100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200207**](InlineResponse200207.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_repay_post**
> InlineResponse200206 sapi_v1_loan_repay_post(order_id, amount, timestamp, signature, type=type, collateral_return=collateral_return, recv_window=recv_window)

Crypto Loan Repay (TRADE)

Weight(UID): 6000

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
api_instance = binance_spot.CryptoLoansApi(binance_spot.ApiClient(configuration))
order_id = 789 # int | Order ID
amount = 1.2 # float | Repayment Amount
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
type = 56 # int | Default: 1. 1 for 'repay with borrowed coin'; 2 for 'repay with collateral'. (optional)
collateral_return = true # bool | Default: TRUE. TRUE: Return extra collateral to spot account; FALSE: Keep extra collateral in the order. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Crypto Loan Repay (TRADE)
    api_response = api_instance.sapi_v1_loan_repay_post(order_id, amount, timestamp, signature, type=type, collateral_return=collateral_return, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoLoansApi->sapi_v1_loan_repay_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID | 
 **amount** | **float**| Repayment Amount | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **type** | **int**| Default: 1. 1 for &#x27;repay with borrowed coin&#x27;; 2 for &#x27;repay with collateral&#x27;. | [optional] 
 **collateral_return** | **bool**| Default: TRUE. TRUE: Return extra collateral to spot account; FALSE: Keep extra collateral in the order. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200206**](InlineResponse200206.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

