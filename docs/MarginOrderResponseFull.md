# MarginOrderResponseFull

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | 
**order_id** | **int** |  | 
**client_order_id** | **str** |  | 
**transact_time** | **int** |  | 
**price** | **str** |  | 
**orig_qty** | **str** |  | 
**executed_qty** | **str** |  | 
**cummulative_quote_qty** | **str** |  | 
**status** | **str** |  | 
**time_in_force** | **str** |  | 
**type** | **str** |  | 
**side** | **str** |  | 
**margin_buy_borrow_amount** | **float** | will not return if no margin trade happens | 
**margin_buy_borrow_asset** | **str** | will not return if no margin trade happens | 
**is_isolated** | **bool** |  | 
**fills** | [**list[OrderResponseFullFills]**](OrderResponseFullFills.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

