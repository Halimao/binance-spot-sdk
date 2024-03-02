# binance_spot.VIPLoansApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_loan_vip_borrow_post**](VIPLoansApi.md#sapi_v1_loan_vip_borrow_post) | **POST** /sapi/v1/loan/vip/borrow | VIP Loan Borrow
[**sapi_v1_loan_vip_collateral_account_get**](VIPLoansApi.md#sapi_v1_loan_vip_collateral_account_get) | **GET** /sapi/v1/loan/vip/collateral/account | Check Locked Value of VIP Collateral Account (USER_DATA)
[**sapi_v1_loan_vip_collateral_data_get**](VIPLoansApi.md#sapi_v1_loan_vip_collateral_data_get) | **GET** /sapi/v1/loan/vip/collateral/data | Get Collateral Asset Data (USER_DATA)
[**sapi_v1_loan_vip_loanable_data_get**](VIPLoansApi.md#sapi_v1_loan_vip_loanable_data_get) | **GET** /sapi/v1/loan/vip/loanable/data | Get Loanable Assets Data
[**sapi_v1_loan_vip_ongoing_orders_get**](VIPLoansApi.md#sapi_v1_loan_vip_ongoing_orders_get) | **GET** /sapi/v1/loan/vip/ongoing/orders | Get VIP Loan Ongoing Orders (USER_DATA)
[**sapi_v1_loan_vip_renew_post**](VIPLoansApi.md#sapi_v1_loan_vip_renew_post) | **POST** /sapi/v1/loan/vip/renew | VIP Loan Renew
[**sapi_v1_loan_vip_repay_history_get**](VIPLoansApi.md#sapi_v1_loan_vip_repay_history_get) | **GET** /sapi/v1/loan/vip/repay/history | Get VIP Loan Repayment History (USER_DATA)
[**sapi_v1_loan_vip_repay_post**](VIPLoansApi.md#sapi_v1_loan_vip_repay_post) | **POST** /sapi/v1/loan/vip/repay | VIP Loan Repay (TRADE)
[**sapi_v1_loan_vip_request_data_get**](VIPLoansApi.md#sapi_v1_loan_vip_request_data_get) | **GET** /sapi/v1/loan/vip/request/data | Query Application Status (USER_DATA)
[**sapi_v1_loan_vip_request_interest_rate_get**](VIPLoansApi.md#sapi_v1_loan_vip_request_interest_rate_get) | **GET** /sapi/v1/loan/vip/request/interestRate | Get Borrow Interest Rate (USER_DATA)

# **sapi_v1_loan_vip_borrow_post**
> InlineResponse200196 sapi_v1_loan_vip_borrow_post(loan_account_id, loan_amount, collateral_account_id, collateral_coin, is_flexible_rate, timestamp, signature, loan_coin=loan_coin, loan_term=loan_term, recv_window=recv_window)

VIP Loan Borrow

VIP loan is available for VIP users only.  Weight(UID): 6000

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
loan_account_id = 789 # int | 
loan_amount = 3.4 # float | 
collateral_account_id = 'collateral_account_id_example' # str | 
collateral_coin = 'collateral_coin_example' # str | 
is_flexible_rate = 'is_flexible_rate_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
loan_term = 56 # int |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # VIP Loan Borrow
    api_response = api_instance.sapi_v1_loan_vip_borrow_post(loan_account_id, loan_amount, collateral_account_id, collateral_coin, is_flexible_rate, timestamp, signature, loan_coin=loan_coin, loan_term=loan_term, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_borrow_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_account_id** | **int**|  | 
 **loan_amount** | **float**|  | 
 **collateral_account_id** | **str**|  | 
 **collateral_coin** | **str**|  | 
 **is_flexible_rate** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **loan_term** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200196**](InlineResponse200196.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_collateral_account_get**
> InlineResponse200195 sapi_v1_loan_vip_collateral_account_get(timestamp, signature, order_id=order_id, collateral_account_id=collateral_account_id, recv_window=recv_window)

Check Locked Value of VIP Collateral Account (USER_DATA)

VIP loan is available for VIP users only.  Weight(IP): 6000

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order id (optional)
collateral_account_id = 789 # int |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Check Locked Value of VIP Collateral Account (USER_DATA)
    api_response = api_instance.sapi_v1_loan_vip_collateral_account_get(timestamp, signature, order_id=order_id, collateral_account_id=collateral_account_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_collateral_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order id | [optional] 
 **collateral_account_id** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200195**](InlineResponse200195.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_collateral_data_get**
> InlineResponse200198 sapi_v1_loan_vip_collateral_data_get(timestamp, signature, collateral_coin=collateral_coin, recv_window=recv_window)

Get Collateral Asset Data (USER_DATA)

Get collateral asset data.  Weight(IP): 400

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Collateral Asset Data (USER_DATA)
    api_response = api_instance.sapi_v1_loan_vip_collateral_data_get(timestamp, signature, collateral_coin=collateral_coin, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_collateral_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200198**](InlineResponse200198.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_loanable_data_get**
> InlineResponse200197 sapi_v1_loan_vip_loanable_data_get(timestamp, signature, loan_coin=loan_coin, vip_level=vip_level, recv_window=recv_window)

Get Loanable Assets Data

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
vip_level = 56 # int | Defaults to user's vip level (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Loanable Assets Data
    api_response = api_instance.sapi_v1_loan_vip_loanable_data_get(timestamp, signature, loan_coin=loan_coin, vip_level=vip_level, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_loanable_data_get: %s\n" % e)
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

[**InlineResponse200197**](InlineResponse200197.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_ongoing_orders_get**
> InlineResponse200192 sapi_v1_loan_vip_ongoing_orders_get(timestamp, signature, order_id=order_id, collateral_account_id=collateral_account_id, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)

Get VIP Loan Ongoing Orders (USER_DATA)

VIP loan is available for VIP users only.  Weight(IP): 400

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order id (optional)
collateral_account_id = 789 # int |  (optional)
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
collateral_coin = 'collateral_coin_example' # str | Coin used as collateral (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 56 # int | Default 10; max 100. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get VIP Loan Ongoing Orders (USER_DATA)
    api_response = api_instance.sapi_v1_loan_vip_ongoing_orders_get(timestamp, signature, order_id=order_id, collateral_account_id=collateral_account_id, loan_coin=loan_coin, collateral_coin=collateral_coin, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_ongoing_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order id | [optional] 
 **collateral_account_id** | **int**|  | [optional] 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **collateral_coin** | **str**| Coin used as collateral | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| Default 10; max 100. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200192**](InlineResponse200192.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_renew_post**
> InlineResponse200201 sapi_v1_loan_vip_renew_post(timestamp, signature, order_id=order_id, loan_term=loan_term, recv_window=recv_window)

VIP Loan Renew

VIP loan is available for VIP users only.  Weight(UID): 6000

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order id (optional)
loan_term = 56 # int |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # VIP Loan Renew
    api_response = api_instance.sapi_v1_loan_vip_renew_post(timestamp, signature, order_id=order_id, loan_term=loan_term, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_renew_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order id | [optional] 
 **loan_term** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200201**](InlineResponse200201.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_repay_history_get**
> InlineResponse200194 sapi_v1_loan_vip_repay_history_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)

Get VIP Loan Repayment History (USER_DATA)

VIP loan is available for VIP users only.  Weight(IP): 400

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order id (optional)
loan_coin = 'loan_coin_example' # str | Coin loaned (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 56 # int | Default 10; max 100. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get VIP Loan Repayment History (USER_DATA)
    api_response = api_instance.sapi_v1_loan_vip_repay_history_get(timestamp, signature, order_id=order_id, loan_coin=loan_coin, start_time=start_time, end_time=end_time, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_repay_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order id | [optional] 
 **loan_coin** | **str**| Coin loaned | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| Default 10; max 100. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200194**](InlineResponse200194.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_repay_post**
> InlineResponse200193 sapi_v1_loan_vip_repay_post(amount, timestamp, signature, order_id=order_id, recv_window=recv_window)

VIP Loan Repay (TRADE)

VIP loan is available for VIP users only.  Weight(UID): 6000

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
order_id = 789 # int | Order id (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # VIP Loan Repay (TRADE)
    api_response = api_instance.sapi_v1_loan_vip_repay_post(amount, timestamp, signature, order_id=order_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_repay_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **order_id** | **int**| Order id | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200193**](InlineResponse200193.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_request_data_get**
> InlineResponse200199 sapi_v1_loan_vip_request_data_get(timestamp, signature, current=current, limit=limit, recv_window=recv_window)

Query Application Status (USER_DATA)

Get Application Status  Weight(UID): 400

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Application Status (USER_DATA)
    api_response = api_instance.sapi_v1_loan_vip_request_data_get(timestamp, signature, current=current, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_request_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200199**](InlineResponse200199.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_loan_vip_request_interest_rate_get**
> list[InlineResponse200200] sapi_v1_loan_vip_request_interest_rate_get(timestamp, signature, loan_coin=loan_coin, recv_window=recv_window)

Get Borrow Interest Rate (USER_DATA)

Get borrow interest rate.  Weight(UID): 400

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
api_instance = binance_spot.VIPLoansApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
loan_coin = 'loan_coin_example' # str | Max 10 assets, Multiple split by \",\" (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Borrow Interest Rate (USER_DATA)
    api_response = api_instance.sapi_v1_loan_vip_request_interest_rate_get(timestamp, signature, loan_coin=loan_coin, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VIPLoansApi->sapi_v1_loan_vip_request_interest_rate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **loan_coin** | **str**| Max 10 assets, Multiple split by \&quot;,\&quot; | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200200]**](InlineResponse200200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

