# SelfUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**email** | **str** |  | 
**company** | **str** |  | [optional] 
**firstname** | **str** |  | 
**lastname** | **str** |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**clouds** | [**list[CloudRole]**](CloudRole.md) |  | [optional] [readonly] 
**projects** | [**list[ProjectRole]**](ProjectRole.md) |  | [optional] [readonly] 
**provider** | **str** |  | [optional] [readonly] 
**provider_sub** | **str** | sub from original identity provider | [optional] 
**sub** | **str** | sub from Keycloak | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


