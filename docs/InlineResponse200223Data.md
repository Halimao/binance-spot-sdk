# InlineResponse200223Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_type** | **str** | Enum：PAY(C2B Merchant Acquiring Payment), PAY_REFUND(C2B Merchant Acquiring Payment,refund), C2C(C2C Transfer Payment),CRYPTO_BOX(Crypto box), CRYPTO_BOX_RF(Crypto Box, refund), C2C_HOLDING(Transfer to new Binance user), C2C_HOLDING_RF(Transfer to new Binance user,refund), PAYOUT(B2C Disbursement Payment) | 
**transaction_id** | **str** |  | 
**transaction_time** | **int** |  | 
**amount** | **str** | order amount(up to 8 decimal places), positive is income, negative is expenditure | 
**currency** | **str** |  | 
**wallet_type** | **int** |  | 
**wallet_types** | **list[int]** |  | 
**funds_detail** | [**list[InlineResponse200223FundsDetail]**](InlineResponse200223FundsDetail.md) |  | 
**payer_info** | [**InlineResponse200223PayerInfo**](InlineResponse200223PayerInfo.md) |  | 
**receiver_info** | [**InlineResponse200223ReceiverInfo**](InlineResponse200223ReceiverInfo.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

