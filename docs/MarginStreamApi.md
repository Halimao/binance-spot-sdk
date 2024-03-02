# binance_spot.MarginStreamApi

All URIs are relative to *https://api.binance.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sapi_v1_user_data_stream_delete**](MarginStreamApi.md#sapi_v1_user_data_stream_delete) | **DELETE** /sapi/v1/userDataStream | Close a ListenKey (USER_STREAM)
[**sapi_v1_user_data_stream_post**](MarginStreamApi.md#sapi_v1_user_data_stream_post) | **POST** /sapi/v1/userDataStream | Create a ListenKey (USER_STREAM)
[**sapi_v1_user_data_stream_put**](MarginStreamApi.md#sapi_v1_user_data_stream_put) | **PUT** /sapi/v1/userDataStream | Ping/Keep-alive a ListenKey (USER_STREAM)

# **sapi_v1_user_data_stream_delete**
> object sapi_v1_user_data_stream_delete(listen_key=listen_key)

Close a ListenKey (USER_STREAM)

Close out a user data stream.  Weight: 1

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
api_instance = binance_spot.MarginStreamApi(binance_spot.ApiClient(configuration))
listen_key = 'listen_key_example' # str | User websocket listen key (optional)

try:
    # Close a ListenKey (USER_STREAM)
    api_response = api_instance.sapi_v1_user_data_stream_delete(listen_key=listen_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginStreamApi->sapi_v1_user_data_stream_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listen_key** | **str**| User websocket listen key | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_user_data_stream_post**
> InlineResponse200124 sapi_v1_user_data_stream_post()

Create a ListenKey (USER_STREAM)

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active `listenKey`, that `listenKey` will be returned and its validity will be extended for 60 minutes.  Weight: 1

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
api_instance = binance_spot.MarginStreamApi(binance_spot.ApiClient(configuration))

try:
    # Create a ListenKey (USER_STREAM)
    api_response = api_instance.sapi_v1_user_data_stream_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginStreamApi->sapi_v1_user_data_stream_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200124**](InlineResponse200124.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sapi_v1_user_data_stream_put**
> object sapi_v1_user_data_stream_put(listen_key=listen_key)

Ping/Keep-alive a ListenKey (USER_STREAM)

Keepalive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.  Weight: 1

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
api_instance = binance_spot.MarginStreamApi(binance_spot.ApiClient(configuration))
listen_key = 'listen_key_example' # str | User websocket listen key (optional)

try:
    # Ping/Keep-alive a ListenKey (USER_STREAM)
    api_response = api_instance.sapi_v1_user_data_stream_put(listen_key=listen_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarginStreamApi->sapi_v1_user_data_stream_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listen_key** | **str**| User websocket listen key | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

