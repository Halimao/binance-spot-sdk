# binance_spot.SavingsApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_lending_customized_fixed_purchase_post**](SavingsApi.md#sapi_v1_lending_customized_fixed_purchase_post) | **POST** /sapi/v1/lending/customizedFixed/purchase | Purchase Fixed/Activity Project (USER_DATA)
[**sapi_v1_lending_position_changed_post**](SavingsApi.md#sapi_v1_lending_position_changed_post) | **POST** /sapi/v1/lending/positionChanged | Change Fixed/Activity Position to Daily Position (USER_DATA)
[**sapi_v1_lending_project_list_get**](SavingsApi.md#sapi_v1_lending_project_list_get) | **GET** /sapi/v1/lending/project/list | Get Fixed/Activity Project List(USER_DATA)
[**sapi_v1_lending_project_position_list_get**](SavingsApi.md#sapi_v1_lending_project_position_list_get) | **GET** /sapi/v1/lending/project/position/list | Get Fixed/Activity Project Position (USER_DATA)

# **sapi_v1_lending_customized_fixed_purchase_post**
> InlineResponse200129 sapi_v1_lending_customized_fixed_purchase_post(project_id, lot, timestamp, signature, recv_window=recv_window)

Purchase Fixed/Activity Project (USER_DATA)

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
api_instance = binance_spot.SavingsApi(binance_spot.ApiClient(configuration))
project_id = 'project_id_example' # str | 
lot = 'lot_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Purchase Fixed/Activity Project (USER_DATA)
    api_response = api_instance.sapi_v1_lending_customized_fixed_purchase_post(project_id, lot, timestamp, signature, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsApi->sapi_v1_lending_customized_fixed_purchase_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **lot** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200129**](InlineResponse200129.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_position_changed_post**
> InlineResponse200131 sapi_v1_lending_position_changed_post(project_id, lot, timestamp, signature, position_id=position_id, recv_window=recv_window)

Change Fixed/Activity Position to Daily Position (USER_DATA)

- PositionId is mandatory parameter for fixed position.  Weight(IP): 1

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
api_instance = binance_spot.SavingsApi(binance_spot.ApiClient(configuration))
project_id = 'project_id_example' # str | 
lot = 'lot_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
position_id = 'position_id_example' # str |  (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Change Fixed/Activity Position to Daily Position (USER_DATA)
    api_response = api_instance.sapi_v1_lending_position_changed_post(project_id, lot, timestamp, signature, position_id=position_id, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsApi->sapi_v1_lending_position_changed_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **lot** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **position_id** | **str**|  | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**InlineResponse200131**](InlineResponse200131.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_project_list_get**
> list[InlineResponse200128] sapi_v1_lending_project_list_get(type, timestamp, signature, asset=asset, status=status, is_sort_asc=is_sort_asc, sort_by=sort_by, current=current, size=size, recv_window=recv_window)

Get Fixed/Activity Project List(USER_DATA)

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
api_instance = binance_spot.SavingsApi(binance_spot.ApiClient(configuration))
type = 'type_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
asset = 'asset_example' # str |  (optional)
status = 'status_example' # str | Default `ALL` (optional)
is_sort_asc = true # bool | default \"true\" (optional)
sort_by = 'sort_by_example' # str | Default `START_TIME` (optional)
current = 56 # int | Current querying page. Start from 1. Default:1 (optional)
size = 56 # int | Default:10 Max:100 (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Fixed/Activity Project List(USER_DATA)
    api_response = api_instance.sapi_v1_lending_project_list_get(type, timestamp, signature, asset=asset, status=status, is_sort_asc=is_sort_asc, sort_by=sort_by, current=current, size=size, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsApi->sapi_v1_lending_project_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **asset** | **str**|  | [optional] 
 **status** | **str**| Default &#x60;ALL&#x60; | [optional] 
 **is_sort_asc** | **bool**| default \&quot;true\&quot; | [optional] 
 **sort_by** | **str**| Default &#x60;START_TIME&#x60; | [optional] 
 **current** | **int**| Current querying page. Start from 1. Default:1 | [optional] 
 **size** | **int**| Default:10 Max:100 | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200128]**](InlineResponse200128.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_lending_project_position_list_get**
> list[InlineResponse200130] sapi_v1_lending_project_position_list_get(asset, timestamp, signature, project_id=project_id, status=status, recv_window=recv_window)

Get Fixed/Activity Project Position (USER_DATA)

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
api_instance = binance_spot.SavingsApi(binance_spot.ApiClient(configuration))
asset = 'asset_example' # str | 
timestamp = 789 # int | UTC timestamp in ms
signature = 'signature_example' # str | Signature
project_id = 'project_id_example' # str |  (optional)
status = 'status_example' # str | Default `ALL` (optional)
recv_window = 789 # int | The value cannot be greater than 60000 (optional)

try:
    # Get Fixed/Activity Project Position (USER_DATA)
    api_response = api_instance.sapi_v1_lending_project_position_list_get(asset, timestamp, signature, project_id=project_id, status=status, recv_window=recv_window)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavingsApi->sapi_v1_lending_project_position_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**|  | 
 **timestamp** | **int**| UTC timestamp in ms | 
 **signature** | **str**| Signature | 
 **project_id** | **str**|  | [optional] 
 **status** | **str**| Default &#x60;ALL&#x60; | [optional] 
 **recv_window** | **int**| The value cannot be greater than 60000 | [optional] 

### Return type

[**list[InlineResponse200130]**](InlineResponse200130.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

