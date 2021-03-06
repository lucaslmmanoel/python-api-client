# Ifc

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**creator** | [**User**](User.md) |  | [optional] 
**status** | **str** |  | [optional] [readonly] 
**source** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**document_id** | **str** |  | [optional] [readonly] 
**document** | [**Document**](Document.md) |  | [optional] 
**structure_file** | **str** |  | [optional] [readonly] 
**systems_file** | **str** |  | [optional] [readonly] 
**map_file** | **str** |  | [optional] [readonly] 
**gltf_file** | **str** |  | [optional] [readonly] 
**bvh_tree_file** | **str** |  | [optional] [readonly] 
**viewer_360_file** | **str** |  | [optional] [readonly] 
**xkt_file** | **str** |  | [optional] [readonly] 
**project_id** | **str** |  | [optional] [readonly] 
**world_position** | **list[float]** | [x,y,z] array of the position of the local_placement in world coordinates | [optional] 
**errors** | **list[str]** | List of errors that happened during IFC processing | [optional] [readonly] 
**warnings** | **list[str]** | List of warnings that happened during IFC processing | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


