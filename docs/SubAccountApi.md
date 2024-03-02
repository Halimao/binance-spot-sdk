# binance_spot.SubAccountApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_capital_deposit_sub_address_get**](SubAccountApi.md#sapi_v1_capital_deposit_sub_address_get) | **GET** /sapi/v1/capital/deposit/subAddress | Sub-account Spot Assets Summary (For Master Account)
[**sapi_v1_capital_deposit_sub_hisrec_get**](SubAccountApi.md#sapi_v1_capital_deposit_sub_hisrec_get) | **GET** /sapi/v1/capital/deposit/subHisrec | Sub-account Deposit History (For Master Account)
[**sapi_v1_managed_subaccount_account_snapshot_get**](SubAccountApi.md#sapi_v1_managed_subaccount_account_snapshot_get) | **GET** /sapi/v1/managed-subaccount/accountSnapshot | Managed sub-account snapshot (For Investor Master Account)
[**sapi_v1_managed_subaccount_asset_get**](SubAccountApi.md#sapi_v1_managed_subaccount_asset_get) | **GET** /sapi/v1/managed-subaccount/asset | Managed sub-account asset details(For Investor Master Account)
[**sapi_v1_managed_subaccount_deposit_address_get**](SubAccountApi.md#sapi_v1_managed_subaccount_deposit_address_get) | **GET** /sapi/v1/managed-subaccount/deposit/address | Get Managed Sub-account Deposit Address (For Investor Master Account)
[**sapi_v1_managed_subaccount_deposit_post**](SubAccountApi.md#sapi_v1_managed_subaccount_deposit_post) | **POST** /sapi/v1/managed-subaccount/deposit | Deposit assets into the managed sub-account(For Investor Master Account)
[**sapi_v1_managed_subaccount_fetch_future_asset_get**](SubAccountApi.md#sapi_v1_managed_subaccount_fetch_future_asset_get) | **GET** /sapi/v1/managed-subaccount/fetch-future-asset | Query Managed Sub-account Futures Asset Details (For Investor Master Account)
[**sapi_v1_managed_subaccount_info_get**](SubAccountApi.md#sapi_v1_managed_subaccount_info_get) | **GET** /sapi/v1/managed-subaccount/info | Query Managed Sub-account List (For Investor)
[**sapi_v1_managed_subaccount_margin_asset_get**](SubAccountApi.md#sapi_v1_managed_subaccount_margin_asset_get) | **GET** /sapi/v1/managed-subaccount/marginAsset | Query Managed Sub-account Margin Asset Details (For Investor Master Account)
[**sapi_v1_managed_subaccount_query_trans_log_for_investor_get**](SubAccountApi.md#sapi_v1_managed_subaccount_query_trans_log_for_investor_get) | **GET** /sapi/v1/managed-subaccount/queryTransLogForInvestor | Query Managed Sub Account Transfer Log (For Investor Master Account)
[**sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_get**](SubAccountApi.md#sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_get) | **GET** /sapi/v1/managed-subaccount/queryTransLogForTradeParent | Query Managed Sub Account Transfer Log (For Trading Team Master Account)
[**sapi_v1_managed_subaccount_query_trans_log_get**](SubAccountApi.md#sapi_v1_managed_subaccount_query_trans_log_get) | **GET** /sapi/v1/managed-subaccount/query-trans-log | Query Managed Sub Account Transfer Log (For Trading Team Sub Account)(USER_DATA)
[**sapi_v1_managed_subaccount_withdraw_post**](SubAccountApi.md#sapi_v1_managed_subaccount_withdraw_post) | **POST** /sapi/v1/managed-subaccount/withdraw | Withdrawl assets from the managed sub-account(For Investor Master Account)
[**sapi_v1_sub_account_blvt_enable_post**](SubAccountApi.md#sapi_v1_sub_account_blvt_enable_post) | **POST** /sapi/v1/sub-account/blvt/enable | Enable Leverage Token for Sub-account (For Master Account)
[**sapi_v1_sub_account_eoptions_enable_post**](SubAccountApi.md#sapi_v1_sub_account_eoptions_enable_post) | **POST** /sapi/v1/sub-account/eoptions/enable | Enable Options for Sub-account (For Master Account)(USER_DATA)
[**sapi_v1_sub_account_futures_account_get**](SubAccountApi.md#sapi_v1_sub_account_futures_account_get) | **GET** /sapi/v1/sub-account/futures/account | Detail on Sub-account&#x27;s Futures Account (For Master Account)
[**sapi_v1_sub_account_futures_account_summary_get**](SubAccountApi.md#sapi_v1_sub_account_futures_account_summary_get) | **GET** /sapi/v1/sub-account/futures/accountSummary | Summary of Sub-account&#x27;s Futures Account (For Master Account)
[**sapi_v1_sub_account_futures_enable_post**](SubAccountApi.md#sapi_v1_sub_account_futures_enable_post) | **POST** /sapi/v1/sub-account/futures/enable | Enable Futures for Sub-account (For Master Account)
[**sapi_v1_sub_account_futures_internal_transfer_get**](SubAccountApi.md#sapi_v1_sub_account_futures_internal_transfer_get) | **GET** /sapi/v1/sub-account/futures/internalTransfer | Sub-account Futures Asset Transfer History (For Master Account)
[**sapi_v1_sub_account_futures_internal_transfer_post**](SubAccountApi.md#sapi_v1_sub_account_futures_internal_transfer_post) | **POST** /sapi/v1/sub-account/futures/internalTransfer | Sub-account Futures Asset Transfer (For Master Account)
[**sapi_v1_sub_account_futures_position_risk_get**](SubAccountApi.md#sapi_v1_sub_account_futures_position_risk_get) | **GET** /sapi/v1/sub-account/futures/positionRisk | Futures Position-Risk of Sub-account (For Master Account)
[**sapi_v1_sub_account_futures_transfer_post**](SubAccountApi.md#sapi_v1_sub_account_futures_transfer_post) | **POST** /sapi/v1/sub-account/futures/transfer | Transfer for Sub-account (For Master Account)
[**sapi_v1_sub_account_list_get**](SubAccountApi.md#sapi_v1_sub_account_list_get) | **GET** /sapi/v1/sub-account/list | Query Sub-account List (For Master Account)
[**sapi_v1_sub_account_margin_account_get**](SubAccountApi.md#sapi_v1_sub_account_margin_account_get) | **GET** /sapi/v1/sub-account/margin/account | Detail on Sub-account&#x27;s Margin Account (For Master Account)
[**sapi_v1_sub_account_margin_account_summary_get**](SubAccountApi.md#sapi_v1_sub_account_margin_account_summary_get) | **GET** /sapi/v1/sub-account/margin/accountSummary | Summary of Sub-account&#x27;s Margin Account (For Master Account)
[**sapi_v1_sub_account_margin_enable_post**](SubAccountApi.md#sapi_v1_sub_account_margin_enable_post) | **POST** /sapi/v1/sub-account/margin/enable | Enable Margin for Sub-account (For Master Account)
[**sapi_v1_sub_account_margin_transfer_post**](SubAccountApi.md#sapi_v1_sub_account_margin_transfer_post) | **POST** /sapi/v1/sub-account/margin/transfer | Margin Transfer for Sub-account (For Master Account)
[**sapi_v1_sub_account_spot_summary_get**](SubAccountApi.md#sapi_v1_sub_account_spot_summary_get) | **GET** /sapi/v1/sub-account/spotSummary | Sub-account Spot Assets Summary (For Master Account)
[**sapi_v1_sub_account_status_get**](SubAccountApi.md#sapi_v1_sub_account_status_get) | **GET** /sapi/v1/sub-account/status | Sub-account&#x27;s Status on Margin/Futures (For Master Account)
[**sapi_v1_sub_account_sub_account_api_ip_restriction_get**](SubAccountApi.md#sapi_v1_sub_account_sub_account_api_ip_restriction_get) | **GET** /sapi/v1/sub-account/subAccountApi/ipRestriction | Get IP Restriction for a Sub-account API Key (For Master Account)
[**sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_delete**](SubAccountApi.md#sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_delete) | **DELETE** /sapi/v1/sub-account/subAccountApi/ipRestriction/ipList | Delete IP List for a Sub-account API Key (For Master Account)
[**sapi_v1_sub_account_sub_transfer_history_get**](SubAccountApi.md#sapi_v1_sub_account_sub_transfer_history_get) | **GET** /sapi/v1/sub-account/sub/transfer/history | Sub-account Spot Asset Transfer History (For Master Account)
[**sapi_v1_sub_account_transaction_statistics_get**](SubAccountApi.md#sapi_v1_sub_account_transaction_statistics_get) | **GET** /sapi/v1/sub-account/transaction-statistics | Query Sub-account Transaction Statistics (For Master Account)
[**sapi_v1_sub_account_transfer_sub_to_master_post**](SubAccountApi.md#sapi_v1_sub_account_transfer_sub_to_master_post) | **POST** /sapi/v1/sub-account/transfer/subToMaster | Transfer to Master (For Sub-account)
[**sapi_v1_sub_account_transfer_sub_to_sub_post**](SubAccountApi.md#sapi_v1_sub_account_transfer_sub_to_sub_post) | **POST** /sapi/v1/sub-account/transfer/subToSub | Transfer to Sub-account of Same Master (For Sub-account)
[**sapi_v1_sub_account_transfer_sub_user_history_get**](SubAccountApi.md#sapi_v1_sub_account_transfer_sub_user_history_get) | **GET** /sapi/v1/sub-account/transfer/subUserHistory | Sub-account Transfer History (For Sub-account)
[**sapi_v1_sub_account_universal_transfer_get**](SubAccountApi.md#sapi_v1_sub_account_universal_transfer_get) | **GET** /sapi/v1/sub-account/universalTransfer | Universal Transfer History (For Master Account)
[**sapi_v1_sub_account_universal_transfer_post**](SubAccountApi.md#sapi_v1_sub_account_universal_transfer_post) | **POST** /sapi/v1/sub-account/universalTransfer | Universal Transfer (For Master Account)
[**sapi_v1_sub_account_virtual_sub_account_post**](SubAccountApi.md#sapi_v1_sub_account_virtual_sub_account_post) | **POST** /sapi/v1/sub-account/virtualSubAccount | Create a Virtual Sub-account(For Master Account)
[**sapi_v2_sub_account_futures_account_get**](SubAccountApi.md#sapi_v2_sub_account_futures_account_get) | **GET** /sapi/v2/sub-account/futures/account | Detail on Sub-account&#x27;s Futures Account V2 (For Master Account)
[**sapi_v2_sub_account_futures_account_summary_get**](SubAccountApi.md#sapi_v2_sub_account_futures_account_summary_get) | **GET** /sapi/v2/sub-account/futures/accountSummary | Summary of Sub-account&#x27;s Futures Account V2 (For Master Account)
[**sapi_v2_sub_account_futures_position_risk_get**](SubAccountApi.md#sapi_v2_sub_account_futures_position_risk_get) | **GET** /sapi/v2/sub-account/futures/positionRisk | Futures Position-Risk of Sub-account V2 (For Master Account)
[**sapi_v2_sub_account_sub_account_api_ip_restriction_post**](SubAccountApi.md#sapi_v2_sub_account_sub_account_api_ip_restriction_post) | **POST** /sapi/v2/sub-account/subAccountApi/ipRestriction | Update IP Restriction for Sub-Account API key (For Master Account)
[**sapi_v3_sub_account_assets_get**](SubAccountApi.md#sapi_v3_sub_account_assets_get) | **GET** /sapi/v3/sub-account/assets | Sub-account Assets (For Master Account)
[**sapi_v4_sub_account_assets_get**](SubAccountApi.md#sapi_v4_sub_account_assets_get) | **GET** /sapi/v4/sub-account/assets | Query Sub-account Assets (For Master Account)

# **sapi_v1_capital_deposit_sub_address_get**
> InlineResponse20087 sapi_v1_capital_deposit_sub_address_get(email, coin, timestamp, signature, network=network, recv_window=recv_window)

Sub-account Spot Assets Summary (For Master Account)

Fetch sub-account deposit address  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
coin = 'coin_example' # str | Coin name
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
network = 'network_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account Spot Assets Summary (For Master Account)
    api_response = api_instance.sapi_v1_capital_deposit_sub_address_get(email, coin, timestamp, signature, network=network, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_capital_deposit_sub_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **coin** | **str**| Coin name | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **network** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20087**](InlineResponse20087.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_deposit_sub_hisrec_get**
> list[InlineResponse20088] sapi_v1_capital_deposit_sub_hisrec_get(email, timestamp, signature, coin=coin, status=status, start_time=start_time, end_time=end_time, limit=limit, offset=offset, recv_window=recv_window)

Sub-account Deposit History (For Master Account)

Fetch sub-account deposit history  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
coin = 'coin_example' # str | Coin name (optional)
status = 56 # int | 0(0:pending,6: credited but cannot withdraw, 1:success) (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 789 # int |  (optional)
offset = 56 # int |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account Deposit History (For Master Account)
    api_response = api_instance.sapi_v1_capital_deposit_sub_hisrec_get(email, timestamp, signature, coin=coin, status=status, start_time=start_time, end_time=end_time, limit=limit, offset=offset, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_capital_deposit_sub_hisrec_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **coin** | **str**| Coin name | [optional] 
 **status** | **int**| 0(0:pending,6: credited but cannot withdraw, 1:success) | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20088]**](InlineResponse20088.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_account_snapshot_get**
> InlineResponse200111 sapi_v1_managed_subaccount_account_snapshot_get(email, type, timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Managed sub-account snapshot (For Investor Master Account)

- The query time period must be less then 30 days - Support query within the last one month only - If `startTime` and `endTime` not sent, return records of the last 7 days by default  Weight(IP): 2400

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.SubAccountApi()
email = 'email_example' # str | Sub-account email
type = 'type_example' # str | \"SPOT\", \"MARGIN\"(cross), \"FUTURES\"(UM)
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | min 7, max 30, default 7 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Managed sub-account snapshot (For Investor Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_account_snapshot_get(email, type, timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_account_snapshot_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **type** | **str**| \&quot;SPOT\&quot;, \&quot;MARGIN\&quot;(cross), \&quot;FUTURES\&quot;(UM) | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| min 7, max 30, default 7 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200111**](InlineResponse200111.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_asset_get**
> list[InlineResponse200110] sapi_v1_managed_subaccount_asset_get(email, timestamp, signature, recv_window=recv_window)

Managed sub-account asset details(For Investor Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Managed sub-account asset details(For Investor Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_asset_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200110]**](InlineResponse200110.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_deposit_address_get**
> InlineResponse200116 sapi_v1_managed_subaccount_deposit_address_get(email, coin, timestamp, signature, network=network, recv_window=recv_window)

Get Managed Sub-account Deposit Address (For Investor Master Account)

Get investor's managed sub-account deposit address  Weight(UID): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
coin = 'coin_example' # str | Coin name
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
network = 'network_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Managed Sub-account Deposit Address (For Investor Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_deposit_address_get(email, coin, timestamp, signature, network=network, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_deposit_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **coin** | **str**| Coin name | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **network** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200116**](InlineResponse200116.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_deposit_post**
> InlineResponse200109 sapi_v1_managed_subaccount_deposit_post(to_email, asset, amount, timestamp, signature, recv_window=recv_window)

Deposit assets into the managed sub-account(For Investor Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
to_email = 'to_email_example' # str | Recipient email
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Deposit assets into the managed sub-account(For Investor Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_deposit_post(to_email, asset, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_deposit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_email** | **str**| Recipient email | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200109**](InlineResponse200109.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_fetch_future_asset_get**
> InlineResponse200113 sapi_v1_managed_subaccount_fetch_future_asset_get(email, timestamp, signature, recv_window=recv_window)

Query Managed Sub-account Futures Asset Details (For Investor Master Account)

Investor can use this api to query managed sub account futures asset details

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Managed Sub-account Futures Asset Details (For Investor Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_fetch_future_asset_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_fetch_future_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200113**](InlineResponse200113.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_info_get**
> InlineResponse200115 sapi_v1_managed_subaccount_info_get(email, timestamp, signature, page=page, limit=limit, recv_window=recv_window)

Query Managed Sub-account List (For Investor)

Get investor's managed sub-account list.  Weight(UID): 60

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Managed Sub-account List (For Investor)
    api_response = api_instance.sapi_v1_managed_subaccount_info_get(email, timestamp, signature, page=page, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200115**](InlineResponse200115.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_margin_asset_get**
> InlineResponse200114 sapi_v1_managed_subaccount_margin_asset_get(email, timestamp, signature, recv_window=recv_window)

Query Managed Sub-account Margin Asset Details (For Investor Master Account)

Investor can use this api to query managed sub account margin asset details

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Managed Sub-account Margin Asset Details (For Investor Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_margin_asset_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_margin_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200114**](InlineResponse200114.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_query_trans_log_for_investor_get**
> InlineResponse200112 sapi_v1_managed_subaccount_query_trans_log_for_investor_get(email, timestamp, signature, start_time=start_time, end_time=end_time, page=page, limit=limit, transfers=transfers, transfer_function_account_type=transfer_function_account_type, recv_window=recv_window)

Query Managed Sub Account Transfer Log (For Investor Master Account)

Investor can use this api to query managed sub account transfer log. This endpoint is available for investor of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset allocation and account application, while delegating trades to a professional trading team.  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
transfers = 'transfers_example' # str | Transfer Direction (FROM/TO) (optional)
transfer_function_account_type = 'transfer_function_account_type_example' # str | Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Managed Sub Account Transfer Log (For Investor Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_query_trans_log_for_investor_get(email, timestamp, signature, start_time=start_time, end_time=end_time, page=page, limit=limit, transfers=transfers, transfer_function_account_type=transfer_function_account_type, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_query_trans_log_for_investor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **transfers** | **str**| Transfer Direction (FROM/TO) | [optional] 
 **transfer_function_account_type** | **str**| Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200112**](InlineResponse200112.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_get**
> InlineResponse200112 sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_get(email, timestamp, signature, start_time=start_time, end_time=end_time, page=page, limit=limit, transfers=transfers, transfer_function_account_type=transfer_function_account_type, recv_window=recv_window)

Query Managed Sub Account Transfer Log (For Trading Team Master Account)

Trading team can use this api to query managed sub account transfer log. This endpoint is available for trading team of Managed Sub-Account. A Managed Sub-Account is an account type for investors who value flexibility in asset allocation and account application, while delegating trades to a professional trading team  Weight(IP): 60

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
transfers = 'transfers_example' # str | Transfer Direction (FROM/TO) (optional)
transfer_function_account_type = 'transfer_function_account_type_example' # str | Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Managed Sub Account Transfer Log (For Trading Team Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_get(email, timestamp, signature, start_time=start_time, end_time=end_time, page=page, limit=limit, transfers=transfers, transfer_function_account_type=transfer_function_account_type, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_query_trans_log_for_trade_parent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **transfers** | **str**| Transfer Direction (FROM/TO) | [optional] 
 **transfer_function_account_type** | **str**| Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE) | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200112**](InlineResponse200112.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_query_trans_log_get**
> InlineResponse200117 sapi_v1_managed_subaccount_query_trans_log_get(transfers, transfer_function_account_type, timestamp, signature, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Query Managed Sub Account Transfer Log (For Trading Team Sub Account)(USER_DATA)

Query Managed Sub Account Transfer Log (For Trading Team Sub Account)  Weight(UID): 60

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
transfers = 'transfers_example' # str | Transfer Direction
transfer_function_account_type = 'transfer_function_account_type_example' # str | Transfer function account type
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Managed Sub Account Transfer Log (For Trading Team Sub Account)(USER_DATA)
    api_response = api_instance.sapi_v1_managed_subaccount_query_trans_log_get(transfers, transfer_function_account_type, timestamp, signature, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_query_trans_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfers** | **str**| Transfer Direction | 
 **transfer_function_account_type** | **str**| Transfer function account type | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200117**](InlineResponse200117.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_managed_subaccount_withdraw_post**
> InlineResponse200109 sapi_v1_managed_subaccount_withdraw_post(from_email, asset, amount, timestamp, signature, transfer_date=transfer_date, recv_window=recv_window)

Withdrawl assets from the managed sub-account(For Investor Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
from_email = 'from_email_example' # str | Sender email
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
transfer_date = 789 # int | Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the withdrawal occurs right now (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Withdrawl assets from the managed sub-account(For Investor Master Account)
    api_response = api_instance.sapi_v1_managed_subaccount_withdraw_post(from_email, asset, amount, timestamp, signature, transfer_date=transfer_date, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_managed_subaccount_withdraw_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_email** | **str**| Sender email | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **transfer_date** | **int**| Withdrawals is automatically occur on the transfer date(UTC0). If a date is not selected, the withdrawal occurs right now | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200109**](InlineResponse200109.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_blvt_enable_post**
> InlineResponse200108 sapi_v1_sub_account_blvt_enable_post(email, enable_blvt, timestamp, signature, recv_window=recv_window)

Enable Leverage Token for Sub-account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
enable_blvt = true # bool | Only true for now
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Enable Leverage Token for Sub-account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_blvt_enable_post(email, enable_blvt, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_blvt_enable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **enable_blvt** | **bool**| Only true for now | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200108**](InlineResponse200108.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_eoptions_enable_post**
> InlineResponse200121 sapi_v1_sub_account_eoptions_enable_post(email, timestamp, signature, recv_window=recv_window)

Enable Options for Sub-account (For Master Account)(USER_DATA)

Enable Options for Sub-account (For Master Account).  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Enable Options for Sub-account (For Master Account)(USER_DATA)
    api_response = api_instance.sapi_v1_sub_account_eoptions_enable_post(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_eoptions_enable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200121**](InlineResponse200121.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_futures_account_get**
> InlineResponse20098 sapi_v1_sub_account_futures_account_get(email, timestamp, signature, recv_window=recv_window)

Detail on Sub-account's Futures Account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Detail on Sub-account's Futures Account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_futures_account_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_futures_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20098**](InlineResponse20098.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_futures_account_summary_get**
> InlineResponse20099 sapi_v1_sub_account_futures_account_summary_get(timestamp, signature, recv_window=recv_window)

Summary of Sub-account's Futures Account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Summary of Sub-account's Futures Account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_futures_account_summary_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_futures_account_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20099**](InlineResponse20099.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_futures_enable_post**
> InlineResponse20097 sapi_v1_sub_account_futures_enable_post(email, timestamp, signature, recv_window=recv_window)

Enable Futures for Sub-account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Enable Futures for Sub-account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_futures_enable_post(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_futures_enable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20097**](InlineResponse20097.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_futures_internal_transfer_get**
> InlineResponse20083 sapi_v1_sub_account_futures_internal_transfer_get(email, futures_type, timestamp, signature, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Sub-account Futures Asset Transfer History (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
futures_type = 56 # int | 1:USDT-margined Futures, 2: Coin-margined Futures
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default value: 50, Max value: 500 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account Futures Asset Transfer History (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_futures_internal_transfer_get(email, futures_type, timestamp, signature, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_futures_internal_transfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **futures_type** | **int**| 1:USDT-margined Futures, 2: Coin-margined Futures | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default value: 50, Max value: 500 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20083**](InlineResponse20083.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_futures_internal_transfer_post**
> InlineResponse20084 sapi_v1_sub_account_futures_internal_transfer_post(from_email, to_email, futures_type, asset, amount, timestamp, signature, recv_window=recv_window)

Sub-account Futures Asset Transfer (For Master Account)

- Master account can transfer max 2000 times a minute  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
from_email = 'from_email_example' # str | Sender email
to_email = 'to_email_example' # str | Recipient email
futures_type = 56 # int | 1:USDT-margined Futures,2: Coin-margined Futures
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account Futures Asset Transfer (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_futures_internal_transfer_post(from_email, to_email, futures_type, asset, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_futures_internal_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_email** | **str**| Sender email | 
 **to_email** | **str**| Recipient email | 
 **futures_type** | **int**| 1:USDT-margined Futures,2: Coin-margined Futures | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20084**](InlineResponse20084.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_futures_position_risk_get**
> list[InlineResponse200100] sapi_v1_sub_account_futures_position_risk_get(email, timestamp, signature, recv_window=recv_window)

Futures Position-Risk of Sub-account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Futures Position-Risk of Sub-account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_futures_position_risk_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_futures_position_risk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200100]**](InlineResponse200100.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_futures_transfer_post**
> InlineResponse200101 sapi_v1_sub_account_futures_transfer_post(email, asset, amount, type, timestamp, signature, recv_window=recv_window)

Transfer for Sub-account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
asset = 'asset_example' # str | 
amount = 1.2 # float | 
type = 56 # int | * `1` - transfer from subaccount's spot account to its USDT-margined futures account * `2` - transfer from subaccount's USDT-margined futures account to its spot account * `3` - transfer from subaccount's spot account to its COIN-margined futures account * `4` - transfer from subaccount's COIN-margined futures account to its spot account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Transfer for Sub-account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_futures_transfer_post(email, asset, amount, type, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_futures_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **type** | **int**| * &#x60;1&#x60; - transfer from subaccount&#x27;s spot account to its USDT-margined futures account * &#x60;2&#x60; - transfer from subaccount&#x27;s USDT-margined futures account to its spot account * &#x60;3&#x60; - transfer from subaccount&#x27;s spot account to its COIN-margined futures account * &#x60;4&#x60; - transfer from subaccount&#x27;s COIN-margined futures account to its spot account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_list_get**
> InlineResponse20081 sapi_v1_sub_account_list_get(timestamp, signature, email=email, is_freeze=is_freeze, page=page, limit=limit, recv_window=recv_window)

Query Sub-account List (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
email = 'email_example' # str | Sub-account email (optional)
is_freeze = 'is_freeze_example' # str |  (optional)
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default 1; max 200 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Sub-account List (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_list_get(timestamp, signature, email=email, is_freeze=is_freeze, page=page, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **email** | **str**| Sub-account email | [optional] 
 **is_freeze** | **str**|  | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default 1; max 200 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20081**](InlineResponse20081.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_margin_account_get**
> InlineResponse20095 sapi_v1_sub_account_margin_account_get(email, timestamp, signature, recv_window=recv_window)

Detail on Sub-account's Margin Account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Detail on Sub-account's Margin Account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_margin_account_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_margin_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20095**](InlineResponse20095.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_margin_account_summary_get**
> InlineResponse20096 sapi_v1_sub_account_margin_account_summary_get(timestamp, signature, recv_window=recv_window)

Summary of Sub-account's Margin Account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Summary of Sub-account's Margin Account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_margin_account_summary_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_margin_account_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20096**](InlineResponse20096.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_margin_enable_post**
> InlineResponse20094 sapi_v1_sub_account_margin_enable_post(email, timestamp, signature, recv_window=recv_window)

Enable Margin for Sub-account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Enable Margin for Sub-account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_margin_enable_post(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_margin_enable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20094**](InlineResponse20094.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_margin_transfer_post**
> InlineResponse200101 sapi_v1_sub_account_margin_transfer_post(email, asset, amount, type, timestamp, signature, recv_window=recv_window)

Margin Transfer for Sub-account (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
asset = 'asset_example' # str | 
amount = 1.2 # float | 
type = 56 # int | * `1` - transfer from subaccount's spot account to margin account * `2` - transfer from subaccount's margin account to its spot account
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Margin Transfer for Sub-account (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_margin_transfer_post(email, asset, amount, type, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_margin_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **type** | **int**| * &#x60;1&#x60; - transfer from subaccount&#x27;s spot account to margin account * &#x60;2&#x60; - transfer from subaccount&#x27;s margin account to its spot account | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_spot_summary_get**
> InlineResponse20086 sapi_v1_sub_account_spot_summary_get(timestamp, signature, email=email, page=page, size=size, recv_window=recv_window)

Sub-account Spot Assets Summary (For Master Account)

Get BTC valued asset summary of subaccounts.  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
email = 'email_example' # str | Sub-account email (optional)
page = 56 # int | Default 1 (optional)
size = 56 # int | Default:10 Max:20 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account Spot Assets Summary (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_spot_summary_get(timestamp, signature, email=email, page=page, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_spot_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **email** | **str**| Sub-account email | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **size** | **int**| Default:10 Max:20 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20086**](InlineResponse20086.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_status_get**
> list[InlineResponse20093] sapi_v1_sub_account_status_get(timestamp, signature, email=email, recv_window=recv_window)

Sub-account's Status on Margin/Futures (For Master Account)

- If no `email` sent, all sub-accounts' information will be returned.  Weight(IP): 10

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
email = 'email_example' # str | Sub-account email (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account's Status on Margin/Futures (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_status_get(timestamp, signature, email=email, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **email** | **str**| Sub-account email | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20093]**](InlineResponse20093.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_sub_account_api_ip_restriction_get**
> InlineResponse200118 sapi_v1_sub_account_sub_account_api_ip_restriction_get(email, sub_account_api_key, timestamp, signature, recv_window=recv_window)

Get IP Restriction for a Sub-account API Key (For Master Account)

Weight(UID): 3000

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
sub_account_api_key = 'sub_account_api_key_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get IP Restriction for a Sub-account API Key (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_sub_account_api_ip_restriction_get(email, sub_account_api_key, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_sub_account_api_ip_restriction_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **sub_account_api_key** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200118**](InlineResponse200118.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_delete**
> InlineResponse200119 sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_delete(email, sub_account_api_key, timestamp, signature, ip_address=ip_address, third_party_name=third_party_name, recv_window=recv_window)

Delete IP List for a Sub-account API Key (For Master Account)

Weight(UID): 3000

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
sub_account_api_key = 'sub_account_api_key_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
ip_address = 'ip_address_example' # str | Can be added in batches, separated by commas (optional)
third_party_name = 'third_party_name_example' # str | third party IP list name (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Delete IP List for a Sub-account API Key (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_delete(email, sub_account_api_key, timestamp, signature, ip_address=ip_address, third_party_name=third_party_name, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_sub_account_api_ip_restriction_ip_list_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **sub_account_api_key** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **ip_address** | **str**| Can be added in batches, separated by commas | [optional] 
 **third_party_name** | **str**| third party IP list name | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200119**](InlineResponse200119.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_sub_transfer_history_get**
> list[InlineResponse20082] sapi_v1_sub_account_sub_transfer_history_get(timestamp, signature, from_email=from_email, to_email=to_email, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Sub-account Spot Asset Transfer History (For Master Account)

- fromEmail and toEmail cannot be sent at the same time. - Return fromEmail equal master account email by default.  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
from_email = 'from_email_example' # str | Sub-account email (optional)
to_email = 'to_email_example' # str | Sub-account email (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default 1 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account Spot Asset Transfer History (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_sub_transfer_history_get(timestamp, signature, from_email=from_email, to_email=to_email, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_sub_transfer_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **from_email** | **str**| Sub-account email | [optional] 
 **to_email** | **str**| Sub-account email | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default 1 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20082]**](InlineResponse20082.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_transaction_statistics_get**
> InlineResponse200120 sapi_v1_sub_account_transaction_statistics_get(email, timestamp, signature, recv_window=recv_window)

Query Sub-account Transaction Statistics (For Master Account)

Query Sub-account Transaction statistics (For Master Account).  Weight(UID): 60

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Sub-account Transaction Statistics (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_transaction_statistics_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_transaction_statistics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200120**](InlineResponse200120.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_transfer_sub_to_master_post**
> InlineResponse200101 sapi_v1_sub_account_transfer_sub_to_master_post(asset, amount, timestamp, signature, recv_window=recv_window)

Transfer to Master (For Sub-account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Transfer to Master (For Sub-account)
    api_response = api_instance.sapi_v1_sub_account_transfer_sub_to_master_post(asset, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_transfer_sub_to_master_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_transfer_sub_to_sub_post**
> InlineResponse200101 sapi_v1_sub_account_transfer_sub_to_sub_post(to_email, asset, amount, timestamp, signature, recv_window=recv_window)

Transfer to Sub-account of Same Master (For Sub-account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
to_email = 'to_email_example' # str | Recipient email
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Transfer to Sub-account of Same Master (For Sub-account)
    api_response = api_instance.sapi_v1_sub_account_transfer_sub_to_sub_post(to_email, asset, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_transfer_sub_to_sub_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_email** | **str**| Recipient email | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200101**](InlineResponse200101.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_transfer_sub_user_history_get**
> list[InlineResponse200102] sapi_v1_sub_account_transfer_sub_user_history_get(timestamp, signature, asset=asset, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Sub-account Transfer History (For Sub-account)

- If `type` is not sent, the records of type 2: transfer out will be returned by default. - If `startTime` and `endTime` are not sent, the recent 30-day data will be returned.  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
type = 56 # int | * `1` - transfer in * `2` - transfer out (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account Transfer History (For Sub-account)
    api_response = api_instance.sapi_v1_sub_account_transfer_sub_user_history_get(timestamp, signature, asset=asset, type=type, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_transfer_sub_user_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **type** | **int**| * &#x60;1&#x60; - transfer in * &#x60;2&#x60; - transfer out | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200102]**](InlineResponse200102.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_universal_transfer_get**
> list[InlineResponse200103] sapi_v1_sub_account_universal_transfer_get(timestamp, signature, from_email=from_email, to_email=to_email, client_tran_id=client_tran_id, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)

Universal Transfer History (For Master Account)

- `fromEmail` and `toEmail` cannot be sent at the same time. - Return `fromEmail` equal master account email by default. - The query time period must be less then 30 days. - If startTime and endTime not sent, return records of the last 30 days by default.  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
from_email = 'from_email_example' # str | Sub-account email (optional)
to_email = 'to_email_example' # str | Sub-account email (optional)
client_tran_id = 'client_tran_id_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default 500, Max 500 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Universal Transfer History (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_universal_transfer_get(timestamp, signature, from_email=from_email, to_email=to_email, client_tran_id=client_tran_id, start_time=start_time, end_time=end_time, page=page, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_universal_transfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **from_email** | **str**| Sub-account email | [optional] 
 **to_email** | **str**| Sub-account email | [optional] 
 **client_tran_id** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default 500, Max 500 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200103]**](InlineResponse200103.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_universal_transfer_post**
> InlineResponse200104 sapi_v1_sub_account_universal_transfer_post(from_account_type, to_account_type, asset, amount, timestamp, signature, from_email=from_email, to_email=to_email, client_tran_id=client_tran_id, symbol=symbol, recv_window=recv_window)

Universal Transfer (For Master Account)

- You need to enable \"internal transfer\" option for the api key which requests this endpoint. - Transfer from master account by default if fromEmail is not sent. - Transfer to master account by default if toEmail is not sent. - Supported transfer scenarios:   - Master account SPOT transfer to sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN   - Sub-account SPOT,USDT_FUTURE,COIN_FUTURE,MARGIN(Cross),ISOLATED_MARGIN transfer to master account SPOT   - Transfer between two sub-account SPOT accounts  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
from_account_type = 'from_account_type_example' # str | 
to_account_type = 'to_account_type_example' # str | 
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
from_email = 'from_email_example' # str | Sub-account email (optional)
to_email = 'to_email_example' # str | Sub-account email (optional)
client_tran_id = 'client_tran_id_example' # str |  (optional)
symbol = 'symbol_example' # str | Only supported under ISOLATED_MARGIN type (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Universal Transfer (For Master Account)
    api_response = api_instance.sapi_v1_sub_account_universal_transfer_post(from_account_type, to_account_type, asset, amount, timestamp, signature, from_email=from_email, to_email=to_email, client_tran_id=client_tran_id, symbol=symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_universal_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_account_type** | **str**|  | 
 **to_account_type** | **str**|  | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **from_email** | **str**| Sub-account email | [optional] 
 **to_email** | **str**| Sub-account email | [optional] 
 **client_tran_id** | **str**|  | [optional] 
 **symbol** | **str**| Only supported under ISOLATED_MARGIN type | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200104**](InlineResponse200104.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_sub_account_virtual_sub_account_post**
> InlineResponse20080 sapi_v1_sub_account_virtual_sub_account_post(sub_account_string, timestamp, signature, recv_window=recv_window)

Create a Virtual Sub-account(For Master Account)

- This request will generate a virtual sub account under your master account. - You need to enable \"trade\" option for the api key which requests this endpoint.  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
sub_account_string = 'sub_account_string_example' # str | Please input a string. We will create a virtual email using that string for you to register
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Create a Virtual Sub-account(For Master Account)
    api_response = api_instance.sapi_v1_sub_account_virtual_sub_account_post(sub_account_string, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v1_sub_account_virtual_sub_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_string** | **str**| Please input a string. We will create a virtual email using that string for you to register | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20080**](InlineResponse20080.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v2_sub_account_futures_account_get**
> InlineResponse200105 sapi_v2_sub_account_futures_account_get(email, futures_type, timestamp, signature, recv_window=recv_window)

Detail on Sub-account's Futures Account V2 (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
futures_type = 56 # int | * `1` - USDT Margined Futures * `2` - COIN Margined Futures
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Detail on Sub-account's Futures Account V2 (For Master Account)
    api_response = api_instance.sapi_v2_sub_account_futures_account_get(email, futures_type, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v2_sub_account_futures_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **futures_type** | **int**| * &#x60;1&#x60; - USDT Margined Futures * &#x60;2&#x60; - COIN Margined Futures | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200105**](InlineResponse200105.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v2_sub_account_futures_account_summary_get**
> InlineResponse200106 sapi_v2_sub_account_futures_account_summary_get(futures_type, timestamp, signature, page=page, limit=limit, recv_window=recv_window)

Summary of Sub-account's Futures Account V2 (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
futures_type = 56 # int | * `1` - USDT Margined Futures * `2` - COIN Margined Futures
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
page = 56 # int | Default 1 (optional)
limit = 56 # int | Default 10, Max 20 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Summary of Sub-account's Futures Account V2 (For Master Account)
    api_response = api_instance.sapi_v2_sub_account_futures_account_summary_get(futures_type, timestamp, signature, page=page, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v2_sub_account_futures_account_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_type** | **int**| * &#x60;1&#x60; - USDT Margined Futures * &#x60;2&#x60; - COIN Margined Futures | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **page** | **int**| Default 1 | [optional] 
 **limit** | **int**| Default 10, Max 20 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200106**](InlineResponse200106.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v2_sub_account_futures_position_risk_get**
> InlineResponse200107 sapi_v2_sub_account_futures_position_risk_get(email, futures_type, timestamp, signature, recv_window=recv_window)

Futures Position-Risk of Sub-account V2 (For Master Account)

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
futures_type = 56 # int | * `1` - USDT Margined Futures * `2` - COIN Margined Futures
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Futures Position-Risk of Sub-account V2 (For Master Account)
    api_response = api_instance.sapi_v2_sub_account_futures_position_risk_get(email, futures_type, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v2_sub_account_futures_position_risk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **futures_type** | **int**| * &#x60;1&#x60; - USDT Margined Futures * &#x60;2&#x60; - COIN Margined Futures | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200107**](InlineResponse200107.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v2_sub_account_sub_account_api_ip_restriction_post**
> InlineResponse200122 sapi_v2_sub_account_sub_account_api_ip_restriction_post(email, sub_account_api_key, status, timestamp, signature, third_party_name=third_party_name, recv_window=recv_window)

Update IP Restriction for Sub-Account API key (For Master Account)

Update IP Restriction for Sub-Account API key  Weight(UID): 3000

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
sub_account_api_key = 'sub_account_api_key_example' # str | 
status = 'status_example' # str | IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only. 3 = Restrict access to users' trusted third party IPs only
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
third_party_name = 'third_party_name_example' # str | third party IP list name (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Update IP Restriction for Sub-Account API key (For Master Account)
    api_response = api_instance.sapi_v2_sub_account_sub_account_api_ip_restriction_post(email, sub_account_api_key, status, timestamp, signature, third_party_name=third_party_name, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v2_sub_account_sub_account_api_ip_restriction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **sub_account_api_key** | **str**|  | 
 **status** | **str**| IP Restriction status. 1 &#x3D; IP Unrestricted. 2 &#x3D; Restrict access to trusted IPs only. 3 &#x3D; Restrict access to users&#x27; trusted third party IPs only | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **third_party_name** | **str**| third party IP list name | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200122**](InlineResponse200122.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v3_sub_account_assets_get**
> InlineResponse20085 sapi_v3_sub_account_assets_get(email, timestamp, signature, recv_window=recv_window)

Sub-account Assets (For Master Account)

Fetch sub-account assets  Weight(IP): 1

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | Sub-account email
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Sub-account Assets (For Master Account)
    api_response = api_instance.sapi_v3_sub_account_assets_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v3_sub_account_assets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Sub-account email | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20085**](InlineResponse20085.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v4_sub_account_assets_get**
> InlineResponse200123 sapi_v4_sub_account_assets_get(email, timestamp, signature, recv_window=recv_window)

Query Sub-account Assets (For Master Account)

Fetch sub-account assets  Weight(UID): 60

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
api_instance = binance_spot.SubAccountApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Sub-account Assets (For Master Account)
    api_response = api_instance.sapi_v4_sub_account_assets_get(email, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubAccountApi->sapi_v4_sub_account_assets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200123**](InlineResponse200123.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

