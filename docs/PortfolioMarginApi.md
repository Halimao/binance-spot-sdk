# binance_spot.PortfolioMarginApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_portfolio_account_get**](PortfolioMarginApi.md#sapi_v1_portfolio_account_get) | **GET** /sapi/v1/portfolio/account | Portfolio Margin Account (USER_DATA)
[**sapi_v1_portfolio_asset_collection_post**](PortfolioMarginApi.md#sapi_v1_portfolio_asset_collection_post) | **POST** /sapi/v1/portfolio/asset-collection | Fund Collection by Asset (USER_DATA)
[**sapi_v1_portfolio_asset_index_price_get**](PortfolioMarginApi.md#sapi_v1_portfolio_asset_index_price_get) | **GET** /sapi/v1/portfolio/asset-index-price | Query Portfolio Margin Asset Index Price (MARKET_DATA)
[**sapi_v1_portfolio_auto_collection_post**](PortfolioMarginApi.md#sapi_v1_portfolio_auto_collection_post) | **POST** /sapi/v1/portfolio/auto-collection | Fund Auto-collection (USER_DATA)
[**sapi_v1_portfolio_bnb_transfer_post**](PortfolioMarginApi.md#sapi_v1_portfolio_bnb_transfer_post) | **POST** /sapi/v1/portfolio/bnb-transfer | BNB Transfer (USER_DATA)
[**sapi_v1_portfolio_collateral_rate_get**](PortfolioMarginApi.md#sapi_v1_portfolio_collateral_rate_get) | **GET** /sapi/v1/portfolio/collateralRate | Portfolio Margin Collateral Rate (MARKET_DATA)
[**sapi_v1_portfolio_interest_history_get**](PortfolioMarginApi.md#sapi_v1_portfolio_interest_history_get) | **GET** /sapi/v1/portfolio/interest-history | Query Classic Portfolio Margin Negative Balance Interest History (USER_DATA)
[**sapi_v1_portfolio_margin_asset_leverage_get**](PortfolioMarginApi.md#sapi_v1_portfolio_margin_asset_leverage_get) | **GET** /sapi/v1/portfolio/margin-asset-leverage | Get Portfolio Margin Asset Leverage (USER_DATA)
[**sapi_v1_portfolio_pm_loan_get**](PortfolioMarginApi.md#sapi_v1_portfolio_pm_loan_get) | **GET** /sapi/v1/portfolio/pmLoan | Portfolio Margin Bankruptcy Loan Amount (USER_DATA)
[**sapi_v1_portfolio_repay_futures_negative_balance_post**](PortfolioMarginApi.md#sapi_v1_portfolio_repay_futures_negative_balance_post) | **POST** /sapi/v1/portfolio/repay-futures-negative-balance | Repay futures Negative Balance (USER_DATA)
[**sapi_v1_portfolio_repay_futures_switch_get**](PortfolioMarginApi.md#sapi_v1_portfolio_repay_futures_switch_get) | **GET** /sapi/v1/portfolio/repay-futures-switch | Get Auto-repay-futures Status (USER_DATA)
[**sapi_v1_portfolio_repay_futures_switch_post**](PortfolioMarginApi.md#sapi_v1_portfolio_repay_futures_switch_post) | **POST** /sapi/v1/portfolio/repay-futures-switch | Change Auto-repay-futures Status (USER_DATA)
[**sapi_v1_portfolio_repay_post**](PortfolioMarginApi.md#sapi_v1_portfolio_repay_post) | **POST** /sapi/v1/portfolio/repay | Portfolio Margin Bankruptcy Loan Repay (USER_DATA)

# **sapi_v1_portfolio_account_get**
> InlineResponse200163 sapi_v1_portfolio_account_get(timestamp, signature, recv_window=recv_window)

Portfolio Margin Account (USER_DATA)

Get the account info  'Weight(IP): 1'

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Portfolio Margin Account (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_account_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200163**](InlineResponse200163.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_asset_collection_post**
> InlineResponse200169 sapi_v1_portfolio_asset_collection_post(asset, timestamp, signature, recv_window=recv_window)

Fund Collection by Asset (USER_DATA)

Transfers specific asset from Futures Account to Margin account  Weight(IP): 60

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Fund Collection by Asset (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_asset_collection_post(asset, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_asset_collection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200169**](InlineResponse200169.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_asset_index_price_get**
> list[InlineResponse200168] sapi_v1_portfolio_asset_index_price_get(asset=asset)

Query Portfolio Margin Asset Index Price (MARKET_DATA)

Query Portfolio Margin Asset Index Price  Weight(IP): - 1 if send asset - 50 if not send asset

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str |  (optional)

try:
    # Query Portfolio Margin Asset Index Price (MARKET_DATA)
    api_response = api_instance.sapi_v1_portfolio_asset_index_price_get(asset=asset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_asset_index_price_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | [optional] 

### Return type

[**list[InlineResponse200168]**](InlineResponse200168.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_auto_collection_post**
> InlineResponse200169 sapi_v1_portfolio_auto_collection_post(timestamp, signature, recv_window=recv_window)

Fund Auto-collection (USER_DATA)

Transfers all assets from Futures Account to Margin account  Weight(IP): 1500

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Fund Auto-collection (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_auto_collection_post(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_auto_collection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200169**](InlineResponse200169.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_bnb_transfer_post**
> InlineResponse200151 sapi_v1_portfolio_bnb_transfer_post(transfer_side, amount, timestamp, signature, recv_window=recv_window)

BNB Transfer (USER_DATA)

BNB transfer can be between Margin Account and USDM Account  Weight(IP): 1500

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
transfer_side = 'transfer_side_example' # str | 
amount = 1.2 # float | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # BNB Transfer (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_bnb_transfer_post(transfer_side, amount, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_bnb_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_side** | **str**|  | 
 **amount** | **float**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200151**](InlineResponse200151.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_collateral_rate_get**
> list[InlineResponse200164] sapi_v1_portfolio_collateral_rate_get()

Portfolio Margin Collateral Rate (MARKET_DATA)

Portfolio Margin Collateral Rate.  Weight(IP): 50

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))

try:
    # Portfolio Margin Collateral Rate (MARKET_DATA)
    api_response = api_instance.sapi_v1_portfolio_collateral_rate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_collateral_rate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200164]**](InlineResponse200164.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_interest_history_get**
> list[InlineResponse200167] sapi_v1_portfolio_interest_history_get(asset, timestamp, signature, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)

Query Classic Portfolio Margin Negative Balance Interest History (USER_DATA)

Query interest history of negative balance for portfolio margin.  Weight(IP): 50

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
start_time = 789 # int | UTC timestamp in ms (optional)
end_time = 789 # int | UTC timestamp in ms (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Query Classic Portfolio Margin Negative Balance Interest History (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_interest_history_get(asset, timestamp, signature, start_time=start_time, end_time=end_time, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_interest_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **start_time** | **int**| UTC timestamp in ms | [optional] 
 **end_time** | **int**| UTC timestamp in ms | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200167]**](InlineResponse200167.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_margin_asset_leverage_get**
> list[InlineResponse200171] sapi_v1_portfolio_margin_asset_leverage_get()

Get Portfolio Margin Asset Leverage (USER_DATA)

Weight(IP): 50

### Example
```python
from __future__ import print_function
import time
import binance_spot
from binance_spot.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = binance_spot.PortfolioMarginApi()

try:
    # Get Portfolio Margin Asset Leverage (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_margin_asset_leverage_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_margin_asset_leverage_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200171]**](InlineResponse200171.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_pm_loan_get**
> InlineResponse200165 sapi_v1_portfolio_pm_loan_get(timestamp, signature, recv_window=recv_window)

Portfolio Margin Bankruptcy Loan Amount (USER_DATA)

Query Portfolio Margin Bankruptcy Loan Amount.  Weight(UID): 500

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Portfolio Margin Bankruptcy Loan Amount (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_pm_loan_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_pm_loan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200165**](InlineResponse200165.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_repay_futures_negative_balance_post**
> InlineResponse200169 sapi_v1_portfolio_repay_futures_negative_balance_post(timestamp, signature, recv_window=recv_window)

Repay futures Negative Balance (USER_DATA)

Repay futures Negative Balance  Weight(IP): 1500

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Repay futures Negative Balance (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_repay_futures_negative_balance_post(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_repay_futures_negative_balance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200169**](InlineResponse200169.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_repay_futures_switch_get**
> InlineResponse200170 sapi_v1_portfolio_repay_futures_switch_get(timestamp, signature, recv_window=recv_window)

Get Auto-repay-futures Status (USER_DATA)

Query Auto-repay-futures Status  Weight(IP): 30

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Auto-repay-futures Status (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_repay_futures_switch_get(timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_repay_futures_switch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200170**](InlineResponse200170.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_repay_futures_switch_post**
> InlineResponse200169 sapi_v1_portfolio_repay_futures_switch_post(auto_repay, timestamp, signature, recv_window=recv_window)

Change Auto-repay-futures Status (USER_DATA)

Change Auto-repay-futures Status  Weight(IP): 1500

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
auto_repay = true # bool | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Change Auto-repay-futures Status (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_repay_futures_switch_post(auto_repay, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_repay_futures_switch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_repay** | **bool**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200169**](InlineResponse200169.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_portfolio_repay_post**
> InlineResponse200166 sapi_v1_portfolio_repay_post(timestamp, signature, _from=_from, recv_window=recv_window)

Portfolio Margin Bankruptcy Loan Repay (USER_DATA)

Repay Portfolio Margin Bankruptcy Loan.  Weight(UID): 3000

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
api_instance = binance_spot.PortfolioMarginApi(binance_spot.ApiClient(configuration))
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
_from = '_from_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Portfolio Margin Bankruptcy Loan Repay (USER_DATA)
    api_response = api_instance.sapi_v1_portfolio_repay_post(timestamp, signature, _from=_from, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMarginApi->sapi_v1_portfolio_repay_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **_from** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200166**](InlineResponse200166.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

