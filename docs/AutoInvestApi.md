# binance_spot.AutoInvestApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_lending_auto_invest_all_asset_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_all_asset_get) | **GET** /sapi/v1/lending/auto-invest/all/asset | Query all source asset and target asset (USER_DATA)
[**sapi_v1_lending_auto_invest_history_list_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_history_list_get) | **GET** /sapi/v1/lending/auto-invest/history/list | Query subscription transaction history
[**sapi_v1_lending_auto_invest_index_info_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_index_info_get) | **GET** /sapi/v1/lending/auto-invest/index/info | Query Index Details(USER_DATA)
[**sapi_v1_lending_auto_invest_index_user_summary_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_index_user_summary_get) | **GET** /sapi/v1/lending/auto-invest/index/user-summary | Query Index Linked Plan Position Details(USER_DATA)
[**sapi_v1_lending_auto_invest_one_off_post**](AutoInvestApi.md#sapi_v1_lending_auto_invest_one_off_post) | **POST** /sapi/v1/lending/auto-invest/one-off | One Time Transaction(TRADE)
[**sapi_v1_lending_auto_invest_one_off_status_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_one_off_status_get) | **GET** /sapi/v1/lending/auto-invest/one-off/status | Query One-Time Transaction Status (USER_DATA)
[**sapi_v1_lending_auto_invest_plan_add_post**](AutoInvestApi.md#sapi_v1_lending_auto_invest_plan_add_post) | **POST** /sapi/v1/lending/auto-invest/plan/add | Investment plan creation (USER_DATA)
[**sapi_v1_lending_auto_invest_plan_edit_post**](AutoInvestApi.md#sapi_v1_lending_auto_invest_plan_edit_post) | **POST** /sapi/v1/lending/auto-invest/plan/edit | Investment plan adjustment
[**sapi_v1_lending_auto_invest_plan_edit_status_post**](AutoInvestApi.md#sapi_v1_lending_auto_invest_plan_edit_status_post) | **POST** /sapi/v1/lending/auto-invest/plan/edit-status | Change Plan Status
[**sapi_v1_lending_auto_invest_plan_id_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_plan_id_get) | **GET** /sapi/v1/lending/auto-invest/plan/id | Query holding details of the plan
[**sapi_v1_lending_auto_invest_plan_list_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_plan_list_get) | **GET** /sapi/v1/lending/auto-invest/plan/list | Get list of plans
[**sapi_v1_lending_auto_invest_rebalance_history_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_rebalance_history_get) | **GET** /sapi/v1/lending/auto-invest/rebalance/history | Index Linked Plan Rebalance Details (USER_DATA)
[**sapi_v1_lending_auto_invest_redeem_history_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_redeem_history_get) | **GET** /sapi/v1/lending/auto-invest/redeem/history | Index Linked Plan Redemption History (USER_DATA)
[**sapi_v1_lending_auto_invest_redeem_post**](AutoInvestApi.md#sapi_v1_lending_auto_invest_redeem_post) | **POST** /sapi/v1/lending/auto-invest/redeem | Index Linked Plan Redemption (TRADE)
[**sapi_v1_lending_auto_invest_source_asset_list_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_source_asset_list_get) | **GET** /sapi/v1/lending/auto-invest/source-asset/list | Query source asset list (USER_DATA)
[**sapi_v1_lending_auto_invest_target_asset_list_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_target_asset_list_get) | **GET** /sapi/v1/lending/auto-invest/target-asset/list | Get target asset list (USER_DATA)
[**sapi_v1_lending_auto_invest_target_asset_roi_list_get**](AutoInvestApi.md#sapi_v1_lending_auto_invest_target_asset_roi_list_get) | **GET** /sapi/v1/lending/auto-invest/target-asset/roi/list | Get target asset ROI data (USER_DATA)

# **sapi_v1_lending_auto_invest_all_asset_get**
> InlineResponse200242 sapi_v1_lending_auto_invest_all_asset_get(timestamp, signature, recv_window=recv_window)

Query all source asset and target asset (USER_DATA)

Query all source assets and target assets  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query all source asset and target asset (USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_all_asset_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_all_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200242**](InlineResponse200242.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_history_list_get**
> list[InlineResponse200248] sapi_v1_lending_auto_invest_history_list_get(timestamp, signature, plan_id=plan_id, start_time=start_time, end_time=end_time, target_asset=target_asset, plan_type=plan_type, size=size, current=current, recv_window=recv_window)

Query subscription transaction history

Query subscription transaction history of a plan  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
plan_id = 789 # int |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
target_asset = 1.2 # float |  (optional)
plan_type = 'plan_type_example' # str |  (optional)
size = 56 # int | Default:10 Max:100 (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query subscription transaction history
    api_response = api_instance.sapi_v1_lending_auto_invest_history_list_get(timestamp, signature, plan_id=plan_id, start_time=start_time, end_time=end_time, target_asset=target_asset, plan_type=plan_type, size=size, current=current, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_history_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **plan_id** | **int**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **target_asset** | **float**|  | [optional] 
 **plan_type** | **str**|  | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200248]**](InlineResponse200248.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_index_info_get**
> InlineResponse200249 sapi_v1_lending_auto_invest_index_info_get(index_id, timestamp, signature, recv_window=recv_window)

Query Index Details(USER_DATA)

Query index details  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
index_id = 789 # int | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Index Details(USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_index_info_get(index_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_index_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_id** | **int**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200249**](InlineResponse200249.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_index_user_summary_get**
> InlineResponse200250 sapi_v1_lending_auto_invest_index_user_summary_get(index_id, timestamp, signature, recv_window=recv_window)

Query Index Linked Plan Position Details(USER_DATA)

Details on users Index-Linked plan position details  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
index_id = 789 # int | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Index Linked Plan Position Details(USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_index_user_summary_get(index_id, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_index_user_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_id** | **int**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200250**](InlineResponse200250.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_one_off_post**
> InlineResponse200251 sapi_v1_lending_auto_invest_one_off_post(source_type, subscription_amount, source_asset, timestamp, signature, request_id=request_id, flexible_allowed_to_use=flexible_allowed_to_use, plan_id=plan_id, index_id=index_id, details=details, recv_window=recv_window)

One Time Transaction(TRADE)

One time transaction  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
source_type = 'source_type_example' # str | 
subscription_amount = 3.4 # float | 
source_asset = 'source_asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
request_id = 'request_id_example' # str |  (optional)
flexible_allowed_to_use = true # bool |  (optional)
plan_id = 789 # int |  (optional)
index_id = 789 # int |  (optional)
details = [binance_spot.Details2()] # list[Details2] |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # One Time Transaction(TRADE)
    api_response = api_instance.sapi_v1_lending_auto_invest_one_off_post(source_type, subscription_amount, source_asset, timestamp, signature, request_id=request_id, flexible_allowed_to_use=flexible_allowed_to_use, plan_id=plan_id, index_id=index_id, details=details, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_one_off_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_type** | **str**|  | 
 **subscription_amount** | **float**|  | 
 **source_asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **request_id** | **str**|  | [optional] 
 **flexible_allowed_to_use** | **bool**|  | [optional] 
 **plan_id** | **int**|  | [optional] 
 **index_id** | **int**|  | [optional] 
 **details** | [**list[Details2]**](Details2.md)|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200251**](InlineResponse200251.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_one_off_status_get**
> InlineResponse200252 sapi_v1_lending_auto_invest_one_off_status_get(transaction_id, timestamp, signature, request_id=request_id, recv_window=recv_window)

Query One-Time Transaction Status (USER_DATA)

Transaction status for one-time transaction  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
transaction_id = 789 # int | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
request_id = 'request_id_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query One-Time Transaction Status (USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_one_off_status_get(transaction_id, timestamp, signature, request_id=request_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_one_off_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **request_id** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200252**](InlineResponse200252.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_plan_add_post**
> InlineResponse200244 sapi_v1_lending_auto_invest_plan_add_post(source_type, plan_type, subscription_amount, subscription_cycle, subscription_start_time, source_asset, details, timestamp, signature, request_id=request_id, index_id=index_id, subscription_start_day=subscription_start_day, subscription_start_weekday=subscription_start_weekday, flexible_allowed_to_use=flexible_allowed_to_use, recv_window=recv_window)

Investment plan creation (USER_DATA)

Post an investment plan creation  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
source_type = 'source_type_example' # str | 
plan_type = 'plan_type_example' # str | 
subscription_amount = 3.4 # float | 
subscription_cycle = 'subscription_cycle_example' # str | 
subscription_start_time = 56 # int | 
source_asset = 'source_asset_example' # str | 
details = [binance_spot.Details()] # list[Details] | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
request_id = 'request_id_example' # str |  (optional)
index_id = 789 # int |  (optional)
subscription_start_day = 56 # int |  (optional)
subscription_start_weekday = 'subscription_start_weekday_example' # str |  (optional)
flexible_allowed_to_use = true # bool |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Investment plan creation (USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_plan_add_post(source_type, plan_type, subscription_amount, subscription_cycle, subscription_start_time, source_asset, details, timestamp, signature, request_id=request_id, index_id=index_id, subscription_start_day=subscription_start_day, subscription_start_weekday=subscription_start_weekday, flexible_allowed_to_use=flexible_allowed_to_use, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_plan_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_type** | **str**|  | 
 **plan_type** | **str**|  | 
 **subscription_amount** | **float**|  | 
 **subscription_cycle** | **str**|  | 
 **subscription_start_time** | **int**|  | 
 **source_asset** | **str**|  | 
 **details** | [**list[Details]**](Details.md)|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **request_id** | **str**|  | [optional] 
 **index_id** | **int**|  | [optional] 
 **subscription_start_day** | **int**|  | [optional] 
 **subscription_start_weekday** | **str**|  | [optional] 
 **flexible_allowed_to_use** | **bool**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200244**](InlineResponse200244.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_plan_edit_post**
> InlineResponse200244 sapi_v1_lending_auto_invest_plan_edit_post(plan_id, subscription_amount, subscription_cycle, subscription_start_time, source_asset, timestamp, signature, subscription_start_day=subscription_start_day, subscription_start_weekday=subscription_start_weekday, flexible_allowed_to_use=flexible_allowed_to_use, details=details, recv_window=recv_window)

Investment plan adjustment

Query Source Asset to be used for investment  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
plan_id = 56 # int | 
subscription_amount = 3.4 # float | 
subscription_cycle = 'subscription_cycle_example' # str | 
subscription_start_time = 56 # int | 
source_asset = 'source_asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
subscription_start_day = 56 # int |  (optional)
subscription_start_weekday = 'subscription_start_weekday_example' # str |  (optional)
flexible_allowed_to_use = true # bool |  (optional)
details = [binance_spot.Details1()] # list[Details1] |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Investment plan adjustment
    api_response = api_instance.sapi_v1_lending_auto_invest_plan_edit_post(plan_id, subscription_amount, subscription_cycle, subscription_start_time, source_asset, timestamp, signature, subscription_start_day=subscription_start_day, subscription_start_weekday=subscription_start_weekday, flexible_allowed_to_use=flexible_allowed_to_use, details=details, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_plan_edit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **int**|  | 
 **subscription_amount** | **float**|  | 
 **subscription_cycle** | **str**|  | 
 **subscription_start_time** | **int**|  | 
 **source_asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **subscription_start_day** | **int**|  | [optional] 
 **subscription_start_weekday** | **str**|  | [optional] 
 **flexible_allowed_to_use** | **bool**|  | [optional] 
 **details** | [**list[Details1]**](Details1.md)|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200244**](InlineResponse200244.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_plan_edit_status_post**
> InlineResponse200245 sapi_v1_lending_auto_invest_plan_edit_status_post(plan_id, status, timestamp, signature, recv_window=recv_window)

Change Plan Status

Change Plan Status  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
plan_id = 56 # int | 
status = 'status_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Change Plan Status
    api_response = api_instance.sapi_v1_lending_auto_invest_plan_edit_status_post(plan_id, status, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_plan_edit_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **int**|  | 
 **status** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200245**](InlineResponse200245.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_plan_id_get**
> InlineResponse200247 sapi_v1_lending_auto_invest_plan_id_get(timestamp, signature, plan_id=plan_id, request_id=request_id, recv_window=recv_window)

Query holding details of the plan

Query holding details of the plan  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
plan_id = 789 # int |  (optional)
request_id = 'request_id_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query holding details of the plan
    api_response = api_instance.sapi_v1_lending_auto_invest_plan_id_get(timestamp, signature, plan_id=plan_id, request_id=request_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_plan_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **plan_id** | **int**|  | [optional] 
 **request_id** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200247**](InlineResponse200247.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_plan_list_get**
> InlineResponse200246 sapi_v1_lending_auto_invest_plan_list_get(plan_type, timestamp, signature, recv_window=recv_window)

Get list of plans

Query plan lists  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
plan_type = 'plan_type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get list of plans
    api_response = api_instance.sapi_v1_lending_auto_invest_plan_list_get(plan_type, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_plan_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200246**](InlineResponse200246.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_rebalance_history_get**
> list[InlineResponse200255] sapi_v1_lending_auto_invest_rebalance_history_get(timestamp, signature, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)

Index Linked Plan Rebalance Details (USER_DATA)

Get the history of Index Linked Plan Redemption transactions  Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day records  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Index Linked Plan Rebalance Details (USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_rebalance_history_get(timestamp, signature, start_time=start_time, end_time=end_time, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_rebalance_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200255]**](InlineResponse200255.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_redeem_history_get**
> list[InlineResponse200254] sapi_v1_lending_auto_invest_redeem_history_get(request_id, timestamp, signature, start_time=start_time, end_time=end_time, current=current, asset=asset, size=size, recv_window=recv_window)

Index Linked Plan Redemption History (USER_DATA)

Get the history of Index Linked Plan Redemption transactions  Max 30 day difference between startTime and endTime If no startTime and endTime, default to show past 30 day records  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
request_id = 789 # int | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
asset = 'asset_example' # str |  (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Index Linked Plan Redemption History (USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_redeem_history_get(request_id, timestamp, signature, start_time=start_time, end_time=end_time, current=current, asset=asset, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_redeem_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **asset** | **str**|  | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200254]**](InlineResponse200254.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_redeem_post**
> InlineResponse200253 sapi_v1_lending_auto_invest_redeem_post(index_id, redemption_percentage, timestamp, signature, request_id=request_id, recv_window=recv_window)

Index Linked Plan Redemption (TRADE)

To redeem index-Linked plan holdings  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
index_id = 789 # int | PORTFOLIO plan's Id
redemption_percentage = 56 # int | user redeem percentage,10/20/100.
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
request_id = 'request_id_example' # str | sourceType + unique, transactionId and requestId cannot be empty at the same time (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Index Linked Plan Redemption (TRADE)
    api_response = api_instance.sapi_v1_lending_auto_invest_redeem_post(index_id, redemption_percentage, timestamp, signature, request_id=request_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_redeem_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_id** | **int**| PORTFOLIO plan&#x27;s Id | 
 **redemption_percentage** | **int**| user redeem percentage,10/20/100. | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **request_id** | **str**| sourceType + unique, transactionId and requestId cannot be empty at the same time | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200253**](InlineResponse200253.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_source_asset_list_get**
> InlineResponse200243 sapi_v1_lending_auto_invest_source_asset_list_get(usage_type, timestamp, signature, target_asset=target_asset, index_id=index_id, flexible_allowed_to_use=flexible_allowed_to_use, recv_window=recv_window)

Query source asset list (USER_DATA)

Query Source Asset to be used for investment  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
usage_type = 'usage_type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
target_asset = 'target_asset_example' # str |  (optional)
index_id = 789 # int |  (optional)
flexible_allowed_to_use = true # bool |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query source asset list (USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_source_asset_list_get(usage_type, timestamp, signature, target_asset=target_asset, index_id=index_id, flexible_allowed_to_use=flexible_allowed_to_use, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_source_asset_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **target_asset** | **str**|  | [optional] 
 **index_id** | **int**|  | [optional] 
 **flexible_allowed_to_use** | **bool**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200243**](InlineResponse200243.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_target_asset_list_get**
> InlineResponse200240 sapi_v1_lending_auto_invest_target_asset_list_get(timestamp, signature, target_asset=target_asset, size=size, current=current, recv_window=recv_window)

Get target asset list (USER_DATA)

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
target_asset = 'target_asset_example' # str |  (optional)
size = 56 # int | Default:10 Max:100 (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get target asset list (USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_target_asset_list_get(timestamp, signature, target_asset=target_asset, size=size, current=current, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_target_asset_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **target_asset** | **str**|  | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200240**](InlineResponse200240.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_auto_invest_target_asset_roi_list_get**
> list[InlineResponse200241] sapi_v1_lending_auto_invest_target_asset_roi_list_get(target_asset, his_roi_type, timestamp, signature, recv_window=recv_window)

Get target asset ROI data (USER_DATA)

ROI return list for target asset  Weight(IP): 1

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
api_instance = binance_spot.AutoInvestApi(binance_spot.ApiClient(configuration))
target_asset = 'target_asset_example' # str | 
his_roi_type = 'his_roi_type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get target asset ROI data (USER_DATA)
    api_response = api_instance.sapi_v1_lending_auto_invest_target_asset_roi_list_get(target_asset, his_roi_type, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutoInvestApi->sapi_v1_lending_auto_invest_target_asset_roi_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_asset** | **str**|  | 
 **his_roi_type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200241]**](InlineResponse200241.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

