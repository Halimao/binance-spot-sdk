# binance_spot.WalletApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_account_api_restrictions_get**](WalletApi.md#sapi_v1_account_api_restrictions_get) | **GET** /sapi/v1/account/apiRestrictions | Get API Key Permission (USER_DATA)
[**sapi_v1_account_api_trading_status_get**](WalletApi.md#sapi_v1_account_api_trading_status_get) | **GET** /sapi/v1/account/apiTradingStatus | Account API Trading Status (USER_DATA)
[**sapi_v1_account_disable_fast_withdraw_switch_post**](WalletApi.md#sapi_v1_account_disable_fast_withdraw_switch_post) | **POST** /sapi/v1/account/disableFastWithdrawSwitch | Disable Fast Withdraw Switch (USER_DATA)
[**sapi_v1_account_enable_fast_withdraw_switch_post**](WalletApi.md#sapi_v1_account_enable_fast_withdraw_switch_post) | **POST** /sapi/v1/account/enableFastWithdrawSwitch | Enable Fast Withdraw Switch (USER_DATA)
[**sapi_v1_account_snapshot_get**](WalletApi.md#sapi_v1_account_snapshot_get) | **GET** /sapi/v1/accountSnapshot | Daily Account Snapshot (USER_DATA)
[**sapi_v1_account_status_get**](WalletApi.md#sapi_v1_account_status_get) | **GET** /sapi/v1/account/status | Account Status (USER_DATA)
[**sapi_v1_asset_asset_detail_get**](WalletApi.md#sapi_v1_asset_asset_detail_get) | **GET** /sapi/v1/asset/assetDetail | Asset Detail (USER_DATA)
[**sapi_v1_asset_asset_dividend_get**](WalletApi.md#sapi_v1_asset_asset_dividend_get) | **GET** /sapi/v1/asset/assetDividend | Asset Dividend Record (USER_DATA)
[**sapi_v1_asset_convert_transfer_post**](WalletApi.md#sapi_v1_asset_convert_transfer_post) | **POST** /sapi/v1/asset/convert-transfer | Convert Transfer (USER_DATA)
[**sapi_v1_asset_convert_transfer_query_by_page_get**](WalletApi.md#sapi_v1_asset_convert_transfer_query_by_page_get) | **GET** /sapi/v1/asset/convert-transfer/queryByPage | Query Convert Transfer (USER_DATA)
[**sapi_v1_asset_custody_transfer_history_get**](WalletApi.md#sapi_v1_asset_custody_transfer_history_get) | **GET** /sapi/v1/asset/custody/transfer-history | Query User Delegation History(For Master Account) (USER_DATA)
[**sapi_v1_asset_dribblet_get**](WalletApi.md#sapi_v1_asset_dribblet_get) | **GET** /sapi/v1/asset/dribblet | DustLog(USER_DATA)
[**sapi_v1_asset_dust_btc_post**](WalletApi.md#sapi_v1_asset_dust_btc_post) | **POST** /sapi/v1/asset/dust-btc | Get Assets That Can Be Converted Into BNB (USER_DATA)
[**sapi_v1_asset_dust_post**](WalletApi.md#sapi_v1_asset_dust_post) | **POST** /sapi/v1/asset/dust | Dust Transfer (USER_DATA)
[**sapi_v1_asset_get_funding_asset_post**](WalletApi.md#sapi_v1_asset_get_funding_asset_post) | **POST** /sapi/v1/asset/get-funding-asset | Funding Wallet (USER_DATA)
[**sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_get**](WalletApi.md#sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_get) | **GET** /sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage | Get Cloud-Mining payment and refund history (USER_DATA)
[**sapi_v1_asset_trade_fee_get**](WalletApi.md#sapi_v1_asset_trade_fee_get) | **GET** /sapi/v1/asset/tradeFee | Trade Fee (USER_DATA)
[**sapi_v1_asset_transfer_get**](WalletApi.md#sapi_v1_asset_transfer_get) | **GET** /sapi/v1/asset/transfer | Query User Universal Transfer History (USER_DATA)
[**sapi_v1_asset_transfer_post**](WalletApi.md#sapi_v1_asset_transfer_post) | **POST** /sapi/v1/asset/transfer | User Universal Transfer (USER_DATA)
[**sapi_v1_asset_wallet_balance_get**](WalletApi.md#sapi_v1_asset_wallet_balance_get) | **GET** /sapi/v1/asset/wallet/balance | Query User Wallet Balance (USER_DATA)
[**sapi_v1_capital_config_getall_get**](WalletApi.md#sapi_v1_capital_config_getall_get) | **GET** /sapi/v1/capital/config/getall | All Coins&#x27; Information (USER_DATA)
[**sapi_v1_capital_contract_convertible_coins_get**](WalletApi.md#sapi_v1_capital_contract_convertible_coins_get) | **GET** /sapi/v1/capital/contract/convertible-coins | Query auto-converting stable coins (USER_DATA)
[**sapi_v1_capital_contract_convertible_coins_post**](WalletApi.md#sapi_v1_capital_contract_convertible_coins_post) | **POST** /sapi/v1/capital/contract/convertible-coins | Switch on/off BUSD and stable coins conversion (USER_DATA) (USER_DATA)
[**sapi_v1_capital_deposit_address_get**](WalletApi.md#sapi_v1_capital_deposit_address_get) | **GET** /sapi/v1/capital/deposit/address | Deposit Address (supporting network) (USER_DATA)
[**sapi_v1_capital_deposit_address_list_get**](WalletApi.md#sapi_v1_capital_deposit_address_list_get) | **GET** /sapi/v1/capital/deposit/address/list | Fetch deposit address list with network (USER_DATA)
[**sapi_v1_capital_deposit_credit_apply_post**](WalletApi.md#sapi_v1_capital_deposit_credit_apply_post) | **POST** /sapi/v1/capital/deposit/credit-apply | One click arrival deposit apply (USER_DATA)
[**sapi_v1_capital_deposit_hisrec_get**](WalletApi.md#sapi_v1_capital_deposit_hisrec_get) | **GET** /sapi/v1/capital/deposit/hisrec | Deposit History(supporting network) (USER_DATA)
[**sapi_v1_capital_withdraw_apply_post**](WalletApi.md#sapi_v1_capital_withdraw_apply_post) | **POST** /sapi/v1/capital/withdraw/apply | Withdraw (USER_DATA)
[**sapi_v1_capital_withdraw_history_get**](WalletApi.md#sapi_v1_capital_withdraw_history_get) | **GET** /sapi/v1/capital/withdraw/history | Withdraw History (supporting network) (USER_DATA)
[**sapi_v1_system_status_get**](WalletApi.md#sapi_v1_system_status_get) | **GET** /sapi/v1/system/status | System Status (System)
[**sapi_v3_asset_get_user_asset_post**](WalletApi.md#sapi_v3_asset_get_user_asset_post) | **POST** /sapi/v3/asset/getUserAsset | User Asset (USER_DATA)

# **sapi_v1_account_api_restrictions_get**
> InlineResponse20078 sapi_v1_account_api_restrictions_get(timestamp, signature, recv_window=recv_window)

Get API Key Permission (USER_DATA)

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get API Key Permission (USER_DATA)
    api_response = api_instance.sapi_v1_account_api_restrictions_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_account_api_restrictions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20078**](InlineResponse20078.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_account_api_trading_status_get**
> InlineResponse20064 sapi_v1_account_api_trading_status_get(timestamp, signature, recv_window=recv_window)

Account API Trading Status (USER_DATA)

Fetch account API trading status with details.  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Account API Trading Status (USER_DATA)
    api_response = api_instance.sapi_v1_account_api_trading_status_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_account_api_trading_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_account_disable_fast_withdraw_switch_post**
> object sapi_v1_account_disable_fast_withdraw_switch_post(timestamp, signature, recv_window=recv_window)

Disable Fast Withdraw Switch (USER_DATA)

- This request will disable fastwithdraw switch under your account. - You need to enable \"trade\" option for the api key which requests this endpoint.  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Disable Fast Withdraw Switch (USER_DATA)
    api_response = api_instance.sapi_v1_account_disable_fast_withdraw_switch_post(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_account_disable_fast_withdraw_switch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **sapi_v1_account_enable_fast_withdraw_switch_post**
> object sapi_v1_account_enable_fast_withdraw_switch_post(timestamp, signature, recv_window=recv_window)

Enable Fast Withdraw Switch (USER_DATA)

- This request will enable fastwithdraw switch under your account. You need to enable \"trade\" option for the api key which requests this endpoint. - When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no on-chain transaction, no transaction ID and no withdrawal fee.  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Enable Fast Withdraw Switch (USER_DATA)
    api_response = api_instance.sapi_v1_account_enable_fast_withdraw_switch_post(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_account_enable_fast_withdraw_switch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **sapi_v1_account_snapshot_get**
> InlineResponse20058 sapi_v1_account_snapshot_get(type, timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Daily Account Snapshot (USER_DATA)

- The query time period must be less than 30 days - Support query within the last one month only - If startTimeand endTime not sent, return records of the last 7 days by default  Weight(IP): 2400

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
type = 'type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 7 # int |  (optional) (default to 7)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Daily Account Snapshot (USER_DATA)
    api_response = api_instance.sapi_v1_account_snapshot_get(type, timestamp, signature, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_account_snapshot_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**|  | [optional] [default to 7]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_account_status_get**
> InlineResponse20063 sapi_v1_account_status_get(timestamp, signature, recv_window=recv_window)

Account Status (USER_DATA)

Fetch account status detail.  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Account Status (USER_DATA)
    api_response = api_instance.sapi_v1_account_status_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_account_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_asset_detail_get**
> InlineResponse20069 sapi_v1_asset_asset_detail_get(timestamp, signature, asset=asset, recv_window=recv_window)

Asset Detail (USER_DATA)

Fetch details of assets supported on Binance.  - Please get network and other deposit or withdraw details from `GET /sapi/v1/capital/config/getall`.  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Asset Detail (USER_DATA)
    api_response = api_instance.sapi_v1_asset_asset_detail_get(timestamp, signature, asset=asset, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_asset_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_asset_dividend_get**
> InlineResponse20068 sapi_v1_asset_asset_dividend_get(timestamp, signature, asset=asset, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)

Asset Dividend Record (USER_DATA)

Query asset Dividend Record  Weight(IP): 10

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
limit = 20 # int |  (optional) (default to 20)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Asset Dividend Record (USER_DATA)
    api_response = api_instance.sapi_v1_asset_asset_dividend_get(timestamp, signature, asset=asset, start_time=start_time, end_time=end_time, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_asset_dividend_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_convert_transfer_post**
> InlineResponse20075 sapi_v1_asset_convert_transfer_post(client_tran_id, asset, amount, target_asset, timestamp, signature, recv_window=recv_window)

Convert Transfer (USER_DATA)

Convert transfer, convert between BUSD and stablecoins. If the clientId has been used before, will not do the convert transfer, the original transfer will be returned.  Weight(UID): 5

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
client_tran_id = 'client_tran_id_example' # str | The unique flag, the min length is 20
asset = 'asset_example' # str | 
amount = 1.2 # float | 
target_asset = 'target_asset_example' # str | Target asset you want to convert
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Convert Transfer (USER_DATA)
    api_response = api_instance.sapi_v1_asset_convert_transfer_post(client_tran_id, asset, amount, target_asset, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_convert_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_tran_id** | **str**| The unique flag, the min length is 20 | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **target_asset** | **str**| Target asset you want to convert | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20075**](InlineResponse20075.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_convert_transfer_query_by_page_get**
> InlineResponse20076 sapi_v1_asset_convert_transfer_query_by_page_get(start_time, end_time, timestamp, signature, tran_id=tran_id, asset=asset, account_type=account_type, current=current, size=size, recv_window=recv_window)

Query Convert Transfer (USER_DATA)

Weight(UID): 5

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
start_time = 789 # int | UTC timestamp in ms
end_time = 789 # int | UTC timestamp in ms
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
tran_id = 789 # int | The transaction id (optional)
asset = 'asset_example' # str | If it is blank, we will match deducted asset and target asset. (optional)
account_type = 'account_type_example' # str | MAIN: main account. CARD: funding account. If it is blank, we will query spot and card wallet, otherwise, we just query the corresponding wallet (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Convert Transfer (USER_DATA)
    api_response = api_instance.sapi_v1_asset_convert_transfer_query_by_page_get(start_time, end_time, timestamp, signature, tran_id=tran_id, asset=asset, account_type=account_type, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_convert_transfer_query_by_page_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| UTC timestamp in ms | 
 **end_time** | **int**| UTC timestamp in ms | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **tran_id** | **int**| The transaction id | [optional] 
 **asset** | **str**| If it is blank, we will match deducted asset and target asset. | [optional] 
 **account_type** | **str**| MAIN: main account. CARD: funding account. If it is blank, we will query spot and card wallet, otherwise, we just query the corresponding wallet | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20076**](InlineResponse20076.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_custody_transfer_history_get**
> InlineResponse20091 sapi_v1_asset_custody_transfer_history_get(email, start_time, end_time, asset, timestamp, signature, type=type, current=current, size=size, recv_window=recv_window)

Query User Delegation History(For Master Account) (USER_DATA)

Query User Delegation History  Weight(IP): 60

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
email = 'email_example' # str | 
start_time = 789 # int | 
end_time = 789 # int | 
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
type = 'type_example' # str |  (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query User Delegation History(For Master Account) (USER_DATA)
    api_response = api_instance.sapi_v1_asset_custody_transfer_history_get(email, start_time, end_time, asset, timestamp, signature, type=type, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_custody_transfer_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **type** | **str**|  | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20091**](InlineResponse20091.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_dribblet_get**
> InlineResponse20065 sapi_v1_asset_dribblet_get(timestamp, signature, start_time=start_time, end_time=end_time, recv_window=recv_window)

DustLog(USER_DATA)

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # DustLog(USER_DATA)
    api_response = api_instance.sapi_v1_asset_dribblet_get(timestamp, signature, start_time=start_time, end_time=end_time, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_dribblet_get: %s\n" % e)
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

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_dust_btc_post**
> InlineResponse20066 sapi_v1_asset_dust_btc_post(timestamp, signature, recv_window=recv_window)

Get Assets That Can Be Converted Into BNB (USER_DATA)

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Assets That Can Be Converted Into BNB (USER_DATA)
    api_response = api_instance.sapi_v1_asset_dust_btc_post(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_dust_btc_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20066**](InlineResponse20066.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_dust_post**
> InlineResponse20067 sapi_v1_asset_dust_post(asset, timestamp, signature, recv_window=recv_window)

Dust Transfer (USER_DATA)

Convert dust assets to BNB.  Weight(UID): 10

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
asset = ['asset_example'] # list[str] | The asset being converted. For example, asset=BTC&asset=USDT
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Dust Transfer (USER_DATA)
    api_response = api_instance.sapi_v1_asset_dust_post(asset, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_dust_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**list[str]**](str.md)| The asset being converted. For example, asset&#x3D;BTC&amp;asset&#x3D;USDT | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_get_funding_asset_post**
> list[InlineResponse20073] sapi_v1_asset_get_funding_asset_post(timestamp, signature, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)

Funding Wallet (USER_DATA)

- Currently supports querying the following business assets：Binance Pay, Binance Card, Binance Gift Card, Stock Token  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
need_btc_valuation = 'need_btc_valuation_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Funding Wallet (USER_DATA)
    api_response = api_instance.sapi_v1_asset_get_funding_asset_post(timestamp, signature, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_get_funding_asset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **need_btc_valuation** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20073]**](InlineResponse20073.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_get**
> InlineResponse20077 sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_get(start_time, end_time, timestamp, signature, tran_id=tran_id, client_tran_id=client_tran_id, asset=asset, current=current, size=size, recv_window=recv_window)

Get Cloud-Mining payment and refund history (USER_DATA)

The query of Cloud-Mining payment and refund history  Weight(UID): 600

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
start_time = 789 # int | UTC timestamp in ms
end_time = 789 # int | UTC timestamp in ms
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
tran_id = 789 # int | The transaction id (optional)
client_tran_id = 'client_tran_id_example' # str | The unique flag (optional)
asset = 'asset_example' # str | If it is blank, we will query all assets (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Cloud-Mining payment and refund history (USER_DATA)
    api_response = api_instance.sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_get(start_time, end_time, timestamp, signature, tran_id=tran_id, client_tran_id=client_tran_id, asset=asset, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_ledger_transfer_cloud_mining_query_by_page_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| UTC timestamp in ms | 
 **end_time** | **int**| UTC timestamp in ms | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **tran_id** | **int**| The transaction id | [optional] 
 **client_tran_id** | **str**| The unique flag | [optional] 
 **asset** | **str**| If it is blank, we will query all assets | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20077**](InlineResponse20077.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_trade_fee_get**
> list[InlineResponse20070] sapi_v1_asset_trade_fee_get(timestamp, signature, symbol=symbol, recv_window=recv_window)

Trade Fee (USER_DATA)

Fetch trade fee  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
symbol = 'symbol_example' # str | Trading symbol, e.g. BNBUSDT (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Trade Fee (USER_DATA)
    api_response = api_instance.sapi_v1_asset_trade_fee_get(timestamp, signature, symbol=symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_trade_fee_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **symbol** | **str**| Trading symbol, e.g. BNBUSDT | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20070]**](InlineResponse20070.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_transfer_get**
> InlineResponse20071 sapi_v1_asset_transfer_get(type, timestamp, signature, start_time=start_time, end_time=end_time, current=current, size=size, from_symbol=from_symbol, to_symbol=to_symbol, recv_window=recv_window)

Query User Universal Transfer History (USER_DATA)

- `fromSymbol` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN - `toSymbol` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN - Support query within the last 6 months only - If `startTime` and `endTime` not sent, return records of the last 7 days by default  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
type = 'type_example' # str | Universal transfer type
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
from_symbol = 'from_symbol_example' # str | Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN (optional)
to_symbol = 'to_symbol_example' # str | Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query User Universal Transfer History (USER_DATA)
    api_response = api_instance.sapi_v1_asset_transfer_get(type, timestamp, signature, start_time=start_time, end_time=end_time, current=current, size=size, from_symbol=from_symbol, to_symbol=to_symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_transfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Universal transfer type | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **from_symbol** | **str**| Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN | [optional] 
 **to_symbol** | **str**| Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20071**](InlineResponse20071.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_transfer_post**
> InlineResponse20072 sapi_v1_asset_transfer_post(type, asset, amount, timestamp, signature, from_symbol=from_symbol, to_symbol=to_symbol, recv_window=recv_window)

User Universal Transfer (USER_DATA)

You need to enable `Permits Universal Transfer` option for the api key which requests this endpoint.  - `fromSymbol` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN - `toSymbol` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN  ENUM of transfer types:   - MAIN_UMFUTURE Spot account transfer to USDⓈ-M Futures account   - MAIN_CMFUTURE Spot account transfer to COIN-M Futures account   - MAIN_MARGIN Spot account transfer to Margin(cross)account   - UMFUTURE_MAIN USDⓈ-M Futures account transfer to Spot account   - UMFUTURE_MARGIN USDⓈ-M Futures account transfer to Margin(cross)account   - CMFUTURE_MAIN COIN-M Futures account transfer to Spot account   - CMFUTURE_MARGIN COIN-M Futures account transfer to Margin(cross) account   - MARGIN_MAIN Margin(cross)account transfer to Spot account   - MARGIN_UMFUTURE Margin(cross)account transfer to USDⓈ-M Futures   - MARGIN_CMFUTURE Margin(cross)account transfer to COIN-M Futures   - ISOLATEDMARGIN_MARGIN Isolated margin account transfer to Margin(cross) account   - MARGIN_ISOLATEDMARGIN Margin(cross) account transfer to Isolated margin account   - ISOLATEDMARGIN_ISOLATEDMARGIN Isolated margin account transfer to Isolated margin account   - MAIN_FUNDING Spot account transfer to Funding account   - FUNDING_MAIN Funding account transfer to Spot account   - FUNDING_UMFUTURE Funding account transfer to UMFUTURE account   - UMFUTURE_FUNDING UMFUTURE account transfer to Funding account   - MARGIN_FUNDING MARGIN account transfer to Funding account   - FUNDING_MARGIN Funding account transfer to Margin account   - FUNDING_CMFUTURE Funding account transfer to CMFUTURE account   - CMFUTURE_FUNDING CMFUTURE account transfer to Funding account   - MAIN_OPTION Spot account transfer to Options account   - OPTION_MAIN Options account transfer to Spot account   - UMFUTURE_OPTION USDⓈ-M Futures account transfer to Options account   - OPTION_UMFUTURE Options account transfer to USDⓈ-M Futures account   - MARGIN_OPTION Margin(cross)account transfer to Options account   - OPTION_MARGIN Options account transfer to Margin(cross)account   - FUNDING_OPTION Funding account transfer to Options account   - OPTION_FUNDING Options account transfer to Funding account   - MAIN_PORTFOLIO_MARGIN Spot account transfer to Portfolio Margin account   - PORTFOLIO_MARGIN_MAIN Portfolio Margin account transfer to Spot account   - MAIN_ISOLATED_MARGIN Spot account transfer to Isolated margin account   - ISOLATED_MARGIN_MAIN Isolated margin account transfer to Spot account  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
type = 'type_example' # str | Universal transfer type
asset = 'asset_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
from_symbol = 'from_symbol_example' # str | Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN (optional)
to_symbol = 'to_symbol_example' # str | Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # User Universal Transfer (USER_DATA)
    api_response = api_instance.sapi_v1_asset_transfer_post(type, asset, amount, timestamp, signature, from_symbol=from_symbol, to_symbol=to_symbol, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Universal transfer type | 
 **asset** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **from_symbol** | **str**| Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN | [optional] 
 **to_symbol** | **str**| Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20072**](InlineResponse20072.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_asset_wallet_balance_get**
> list[InlineResponse20090] sapi_v1_asset_wallet_balance_get(timestamp, signature, recv_window=recv_window)

Query User Wallet Balance (USER_DATA)

Query User Wallet Balance  Weight(IP): 60

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query User Wallet Balance (USER_DATA)
    api_response = api_instance.sapi_v1_asset_wallet_balance_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_asset_wallet_balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20090]**](InlineResponse20090.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_config_getall_get**
> list[InlineResponse20057] sapi_v1_capital_config_getall_get(timestamp, signature, recv_window=recv_window)

All Coins' Information (USER_DATA)

Get information of coins (available for deposit and withdraw) for user.  Weight(IP): 10

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # All Coins' Information (USER_DATA)
    api_response = api_instance.sapi_v1_capital_config_getall_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_config_getall_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20057]**](InlineResponse20057.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_contract_convertible_coins_get**
> InlineResponse20079 sapi_v1_capital_contract_convertible_coins_get()

Query auto-converting stable coins (USER_DATA)

Get a user's auto-conversion settings in deposit/withdrawal  Weight(UID): 600'

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))

try:
    # Query auto-converting stable coins (USER_DATA)
    api_response = api_instance.sapi_v1_capital_contract_convertible_coins_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_contract_convertible_coins_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20079**](InlineResponse20079.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_contract_convertible_coins_post**
> object sapi_v1_capital_contract_convertible_coins_post(coin, enable)

Switch on/off BUSD and stable coins conversion (USER_DATA) (USER_DATA)

User can use it to turn on or turn off the BUSD auto-conversion from/to a specific stable coin.  Weight(UID): 600'

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
coin = 'coin_example' # str | Must be USDC, USDP or TUSD
enable = true # bool | true: turn on the auto-conversion. false: turn off the auto-conversion

try:
    # Switch on/off BUSD and stable coins conversion (USER_DATA) (USER_DATA)
    api_response = api_instance.sapi_v1_capital_contract_convertible_coins_post(coin, enable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_contract_convertible_coins_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Must be USDC, USDP or TUSD | 
 **enable** | **bool**| true: turn on the auto-conversion. false: turn off the auto-conversion | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_deposit_address_get**
> InlineResponse20062 sapi_v1_capital_deposit_address_get(coin, timestamp, signature, network=network, recv_window=recv_window)

Deposit Address (supporting network) (USER_DATA)

Fetch deposit address with network.  - If network is not send, return with default network of the coin. - You can get network and isDefault in networkList in the response of Get /sapi/v1/capital/config/getall (HMAC SHA256).  Weight(IP): 10

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
coin = 'coin_example' # str | Coin name
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
network = 'network_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Deposit Address (supporting network) (USER_DATA)
    api_response = api_instance.sapi_v1_capital_deposit_address_get(coin, timestamp, signature, network=network, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_deposit_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Coin name | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **network** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_deposit_address_list_get**
> list[InlineResponse20092] sapi_v1_capital_deposit_address_list_get(coin, timestamp, signature, network=network, recv_window=recv_window)

Fetch deposit address list with network (USER_DATA)

Fetch deposit address list with network.  Weight(IP): 10

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
coin = 'coin_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
network = 'network_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Fetch deposit address list with network (USER_DATA)
    api_response = api_instance.sapi_v1_capital_deposit_address_list_get(coin, timestamp, signature, network=network, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_deposit_address_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **network** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20092]**](InlineResponse20092.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_deposit_credit_apply_post**
> InlineResponse20089 sapi_v1_capital_deposit_credit_apply_post(timestamp, signature, deposit_id=deposit_id, tx_id=tx_id, sub_account_id=sub_account_id, sub_user_id=sub_user_id, recv_window=recv_window)

One click arrival deposit apply (USER_DATA)

Apply deposit credit for expired address (One click arrival)  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
deposit_id = 789 # int | Deposit record Id, priority use (optional)
tx_id = 'tx_id_example' # str | Deposit txId, used when depositId is not specified (optional)
sub_account_id = 789 # int |  (optional)
sub_user_id = 789 # int |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # One click arrival deposit apply (USER_DATA)
    api_response = api_instance.sapi_v1_capital_deposit_credit_apply_post(timestamp, signature, deposit_id=deposit_id, tx_id=tx_id, sub_account_id=sub_account_id, sub_user_id=sub_user_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_deposit_credit_apply_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **deposit_id** | **int**| Deposit record Id, priority use | [optional] 
 **tx_id** | **str**| Deposit txId, used when depositId is not specified | [optional] 
 **sub_account_id** | **int**|  | [optional] 
 **sub_user_id** | **int**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20089**](InlineResponse20089.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_deposit_hisrec_get**
> list[InlineResponse20060] sapi_v1_capital_deposit_hisrec_get(timestamp, signature, coin=coin, status=status, start_time=start_time, end_time=end_time, offset=offset, limit=limit, recv_window=recv_window)

Deposit History(supporting network) (USER_DATA)

Fetch deposit history.  - Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days. - If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days.  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
coin = 'coin_example' # str | Coin name (optional)
status = 56 # int | * `0` - pending * `6` - credited but cannot withdraw * `1` - success (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
offset = 56 # int |  (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Deposit History(supporting network) (USER_DATA)
    api_response = api_instance.sapi_v1_capital_deposit_hisrec_get(timestamp, signature, coin=coin, status=status, start_time=start_time, end_time=end_time, offset=offset, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_deposit_hisrec_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **coin** | **str**| Coin name | [optional] 
 **status** | **int**| * &#x60;0&#x60; - pending * &#x60;6&#x60; - credited but cannot withdraw * &#x60;1&#x60; - success | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20060]**](InlineResponse20060.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_withdraw_apply_post**
> InlineResponse20059 sapi_v1_capital_withdraw_apply_post(coin, address, amount, timestamp, signature, withdraw_order_id=withdraw_order_id, network=network, address_tag=address_tag, transaction_fee_flag=transaction_fee_flag, name=name, wallet_type=wallet_type, recv_window=recv_window)

Withdraw (USER_DATA)

Submit a withdraw request.  - If `network` not send, return with default network of the coin. - You can get `network` and `isDefault` in `networkList` of a coin in the response of `Get /sapi/v1/capital/config/getall (HMAC SHA256)`.  Weight(IP): 1

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
coin = 'coin_example' # str | Coin name
address = 'address_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
withdraw_order_id = 'withdraw_order_id_example' # str | Client id for withdraw (optional)
network = 'network_example' # str |  (optional)
address_tag = 'address_tag_example' # str | Secondary address identifier for coins like XRP,XMR etc. (optional)
transaction_fee_flag = false # bool | When making internal transfer - `true` ->  returning the fee to the destination account; - `false` -> returning the fee back to the departure account. (optional) (default to false)
name = 'name_example' # str |  (optional)
wallet_type = 56 # int | The wallet type for withdraw，0-Spot wallet, 1- Funding wallet. Default is Spot wallet (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Withdraw (USER_DATA)
    api_response = api_instance.sapi_v1_capital_withdraw_apply_post(coin, address, amount, timestamp, signature, withdraw_order_id=withdraw_order_id, network=network, address_tag=address_tag, transaction_fee_flag=transaction_fee_flag, name=name, wallet_type=wallet_type, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_withdraw_apply_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Coin name | 
 **address** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **withdraw_order_id** | **str**| Client id for withdraw | [optional] 
 **network** | **str**|  | [optional] 
 **address_tag** | **str**| Secondary address identifier for coins like XRP,XMR etc. | [optional] 
 **transaction_fee_flag** | **bool**| When making internal transfer - &#x60;true&#x60; -&gt;  returning the fee to the destination account; - &#x60;false&#x60; -&gt; returning the fee back to the departure account. | [optional] [default to false]
 **name** | **str**|  | [optional] 
 **wallet_type** | **int**| The wallet type for withdraw，0-Spot wallet, 1- Funding wallet. Default is Spot wallet | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_capital_withdraw_history_get**
> list[InlineResponse20061] sapi_v1_capital_withdraw_history_get(timestamp, signature, coin=coin, withdraw_order_id=withdraw_order_id, status=status, start_time=start_time, end_time=end_time, offset=offset, limit=limit, recv_window=recv_window)

Withdraw History (supporting network) (USER_DATA)

Fetch withdraw history.  This endpoint specifically uses per second UID rate limit, user's total second level IP rate limit is 180000/second. Response from the endpoint contains header key X-SAPI-USED-UID-WEIGHT-1S, which defines weight used by the current IP.  - `network` may not be in the response for old withdraw. - Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days. - If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days - If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days. - If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.  Weight(UID): 18000 Request Limit: 10 requests per second

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
coin = 'coin_example' # str | Coin name (optional)
withdraw_order_id = 'withdraw_order_id_example' # str |  (optional)
status = 56 # int | * `0` - Email Sent * `1` - Cancelled * `2` - Awaiting Approval * `3` - Rejected * `4` - Processing * `5` - Failure * `6` - Completed (optional)
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
offset = 56 # int |  (optional)
limit = 56 # int | Default 500; max 1000. (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Withdraw History (supporting network) (USER_DATA)
    api_response = api_instance.sapi_v1_capital_withdraw_history_get(timestamp, signature, coin=coin, withdraw_order_id=withdraw_order_id, status=status, start_time=start_time, end_time=end_time, offset=offset, limit=limit, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_capital_withdraw_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **coin** | **str**| Coin name | [optional] 
 **withdraw_order_id** | **str**|  | [optional] 
 **status** | **int**| * &#x60;0&#x60; - Email Sent * &#x60;1&#x60; - Cancelled * &#x60;2&#x60; - Awaiting Approval * &#x60;3&#x60; - Rejected * &#x60;4&#x60; - Processing * &#x60;5&#x60; - Failure * &#x60;6&#x60; - Completed | [optional] 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **offset** | **int**|  | [optional] 
 **limit** | **int**| Default 500; max 1000. | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20061]**](InlineResponse20061.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_system_status_get**
> InlineResponse20056 sapi_v1_system_status_get()

System Status (System)

Fetch system status.  Weight(IP): 1

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.WalletApi()

try:
    # System Status (System)
    api_response = api_instance.sapi_v1_system_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v1_system_status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v3_asset_get_user_asset_post**
> list[InlineResponse20074] sapi_v3_asset_get_user_asset_post(timestamp, signature, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)

User Asset (USER_DATA)

Get user assets, just for positive data.  Weight(IP): 5

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
api_instance = binance_spot.WalletApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
need_btc_valuation = 'need_btc_valuation_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # User Asset (USER_DATA)
    api_response = api_instance.sapi_v3_asset_get_user_asset_post(timestamp, signature, asset=asset, need_btc_valuation=need_btc_valuation, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->sapi_v3_asset_get_user_asset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **need_btc_valuation** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse20074]**](InlineResponse20074.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

