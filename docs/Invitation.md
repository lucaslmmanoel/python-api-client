# Invitation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**client_id** | **str** |  | [optional] 
**redirect_uri** | **str** | User will be redirected to this uri when they accept the invitation | 
**cloud_name** | **str** |  | 
**cloud_role** | **int** | Role the user will have when they accept the invitation | 
**project_name** | **str** |  | [optional] 
**project_role** | **int** | Role the user will have when they accept the invitation | [optional] 
**email** | **str** | email of the user to invite | 
**status** | **str** |          A: Accepted         D: Denied         P: Pending         W: Accepted but waiting for user first login to finish the process          | [optional] 
**sender_provider_sub** | **str** | OIDC sub of the sender. The original sub from the provider is used instead of the broker sub | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

