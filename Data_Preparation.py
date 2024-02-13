# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2024-02-13 09:57:46
"""
import arcpy
from sys import argv

#For inline variable substitution, parameters passed as a String are evaluated using locals(), globals() and isinstance(). To override, substitute values directly.
def DataPreparation(Input_Refugee_Camp_Structure_Features="C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_SpatialJoi", Refugee_Tent_Selection_Expression="use_ = 'Refugee Tent'", Washroom_s_Selection_Expression="use_ = 'Wash Room(s)'"):  # Data Preparation

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    NetworkAnalysis_Package_gdb_2_ = "C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb"
    Field_Type = "TEXT"
    NetworkAnalysis_Package_gdb = "C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb"
    Field_Type_2_ = "TEXT"

    # Process: Feature To Point (Feature To Point) (management)
    Regularized_Tents_Point = "C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point"
    arcpy.management.FeatureToPoint(in_features=Input_Refugee_Camp_Structure_Features.__str__().format(**locals(),**globals())if isinstance(Input_Refugee_Camp_Structure_Features, str) else Input_Refugee_Camp_Structure_Features, out_feature_class=Regularized_Tents_Point)

    # Process: Feature Class To Feature Class (2) (Feature Class To Feature Class) (conversion)
    Tent_Centroids = arcpy.conversion.FeatureClassToFeatureClass(in_features=Regularized_Tents_Point, out_path=NetworkAnalysis_Package_gdb_2_, out_name="Tent_Centroids", where_clause=Refugee_Tent_Selection_Expression.__str__().format(**locals(),**globals())if isinstance(Refugee_Tent_Selection_Expression, str) else Refugee_Tent_Selection_Expression, field_mapping="Join_Count \"Join_Count\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Join_Count,-1,-1;TARGET_FID \"TARGET_FID\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,TARGET_FID,-1,-1;MEAN_Confidence \"MEAN_Confidence\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,MEAN_Confidence,-1,-1;ORIG_OID \"ORIG_OID\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,ORIG_OID,-1,-1;STATUS \"STATUS\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,STATUS,-1,-1;use_ \"Tent Use\" true true false 255 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,use_,0,254;District \"District\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,District,0,253;Upazila \"Upazila\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Upazila,0,253;Union_ \"Union\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Union_,0,253;Settlement \"Settlement\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Settlement,0,253;Camp_Name \"Camp Name\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Camp_Name,0,253;ISCG_Camp \"ISCG Camp\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,ISCG_Camp,0,253;Unique_ID \"Unique ID\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Unique_ID,0,253;Facility_C \"Facility C\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Facility_C,0,253;Facility \"Facility\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Facility,0,253;GPS_point_ \"GPS_point_\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,GPS_point_,-1,-1;GPS_poin_1 \"GPS_poin_1\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,GPS_poin_1,-1,-1;Flood_Risk \"Flood Risk\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Flood_Risk,0,253;Landslide \"Landslide\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Landslide,0,253;Date_Recor \"Date Recor\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Date_Recor,0,253;Sector \"Sector\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sector,0,253;Sanitation \"Sanitation\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitation,0,253;Sanitati_1 \"Sanitati_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_1,0,253;Sanitati_2 \"Sanitati_2\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_2,0,253;Sanitati_3 \"Sanitati_3\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_3,0,253;Sanitati_4 \"Sanitati_4\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_4,-1,-1;Sanitati_5 \"Sanitati_5\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_5,-1,-1;Sanitati_6 \"Sanitati_6\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_6,-1,-1;Sanitati_7 \"Sanitati_7\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_7,-1,-1;Sanitati_8 \"Sanitati_8\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_8,-1,-1;Sanitati_9 \"Sanitati_9\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_9,-1,-1;Sanitati10 \"Sanitati10\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati10,-1,-1;Sanitati11 \"Sanitati11\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati11,-1,-1;Sanitati12 \"Sanitati12\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati12,-1,-1;Sanitati13 \"Sanitati13\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati13,-1,-1;Sanitati14 \"Sanitati14\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati14,-1,-1;Water_stru \"Water-stru\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_stru,0,253;Water_wate \"Water-wate\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_wate,0,253;Water_st_1 \"Water-st_1\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_st_1,-1,-1;Water_num_ \"Water-num_\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_num_,-1,-1;Water_wa_1 \"Water-wa_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_wa_1,0,253;Other_stru \"Other-stru\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_stru,0,253;Other_st_1 \"Other-st_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_st_1,0,253;Other_site \"Other-site\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_site,0,253;Other_si_1 \"Other-si_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_si_1,0,253;Other_num_ \"Other-num_\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_num_,-1,-1;informatio \"informatio\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informatio,0,253;informat_1 \"informat_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_1,0,253;informat_2 \"informat_2\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_2,0,253;informat_3 \"informat_3\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_3,0,253;informat_4 \"informat_4\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_4,0,253;informat_5 \"informat_5\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_5,0,253;informat_6 \"informat_6\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_6,-1,-1;informat_7 \"informat_7\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_7,-1,-1;uuid \"uuid\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,uuid,0,253;Population \"Population\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Population,-1,-1;households \"Households\" true true false 2 Short 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,households,-1,-1;washroom_capacity \"Washroom Capacity\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,washroom_capacity,-1,-1;Shape_Length \"Shape_Length\" true true true 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Shape_Length,-1,-1;Shape_Area \"Shape_Area\" true true true 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Shape_Area,-1,-1;ORIG_FID \"ORIG_FID\" true true false 0 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,ORIG_FID,-1,-1")[0]

    # Process: Calculate Field (Calculate Field) (management)
    Tent_Centroids_2_ = arcpy.management.CalculateField(in_table=Tent_Centroids, field="TentID", expression="!ORIG_OID!", field_type=Field_Type)[0]

    # Process: Feature Class To Feature Class (Feature Class To Feature Class) (conversion)
    Washroom_Centroids = arcpy.conversion.FeatureClassToFeatureClass(in_features=Regularized_Tents_Point, out_path=NetworkAnalysis_Package_gdb, out_name="Washroom_Centroids", where_clause=Washroom_s_Selection_Expression.__str__().format(**locals(),**globals())if isinstance(Washroom_s_Selection_Expression, str) else Washroom_s_Selection_Expression, field_mapping="Join_Count \"Join_Count\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Join_Count,-1,-1;TARGET_FID \"TARGET_FID\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,TARGET_FID,-1,-1;MEAN_Confidence \"MEAN_Confidence\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,MEAN_Confidence,-1,-1;ORIG_OID \"ORIG_OID\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,ORIG_OID,-1,-1;STATUS \"STATUS\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,STATUS,-1,-1;use_ \"Tent Use\" true true false 255 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,use_,0,254;District \"District\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,District,0,253;Upazila \"Upazila\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Upazila,0,253;Union_ \"Union\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Union_,0,253;Settlement \"Settlement\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Settlement,0,253;Camp_Name \"Camp Name\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Camp_Name,0,253;ISCG_Camp \"ISCG Camp\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,ISCG_Camp,0,253;Unique_ID \"Unique ID\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Unique_ID,0,253;Facility_C \"Facility C\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Facility_C,0,253;Facility \"Facility\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Facility,0,253;GPS_point_ \"GPS_point_\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,GPS_point_,-1,-1;GPS_poin_1 \"GPS_poin_1\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,GPS_poin_1,-1,-1;Flood_Risk \"Flood Risk\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Flood_Risk,0,253;Landslide \"Landslide\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Landslide,0,253;Date_Recor \"Date Recor\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Date_Recor,0,253;Sector \"Sector\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sector,0,253;Sanitation \"Sanitation\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitation,0,253;Sanitati_1 \"Sanitati_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_1,0,253;Sanitati_2 \"Sanitati_2\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_2,0,253;Sanitati_3 \"Sanitati_3\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_3,0,253;Sanitati_4 \"Sanitati_4\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_4,-1,-1;Sanitati_5 \"Sanitati_5\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_5,-1,-1;Sanitati_6 \"Sanitati_6\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_6,-1,-1;Sanitati_7 \"Sanitati_7\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_7,-1,-1;Sanitati_8 \"Sanitati_8\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_8,-1,-1;Sanitati_9 \"Sanitati_9\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati_9,-1,-1;Sanitati10 \"Sanitati10\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati10,-1,-1;Sanitati11 \"Sanitati11\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati11,-1,-1;Sanitati12 \"Sanitati12\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati12,-1,-1;Sanitati13 \"Sanitati13\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati13,-1,-1;Sanitati14 \"Sanitati14\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Sanitati14,-1,-1;Water_stru \"Water-stru\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_stru,0,253;Water_wate \"Water-wate\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_wate,0,253;Water_st_1 \"Water-st_1\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_st_1,-1,-1;Water_num_ \"Water-num_\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_num_,-1,-1;Water_wa_1 \"Water-wa_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Water_wa_1,0,253;Other_stru \"Other-stru\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_stru,0,253;Other_st_1 \"Other-st_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_st_1,0,253;Other_site \"Other-site\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_site,0,253;Other_si_1 \"Other-si_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_si_1,0,253;Other_num_ \"Other-num_\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Other_num_,-1,-1;informatio \"informatio\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informatio,0,253;informat_1 \"informat_1\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_1,0,253;informat_2 \"informat_2\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_2,0,253;informat_3 \"informat_3\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_3,0,253;informat_4 \"informat_4\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_4,0,253;informat_5 \"informat_5\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_5,0,253;informat_6 \"informat_6\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_6,-1,-1;informat_7 \"informat_7\" true true false 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,informat_7,-1,-1;uuid \"uuid\" true true false 254 Text 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,uuid,0,253;Population \"Population\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Population,-1,-1;households \"Households\" true true false 2 Short 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,households,-1,-1;washroom_capacity \"Washroom Capacity\" true true false 4 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,washroom_capacity,-1,-1;Shape_Length \"Shape_Length\" true true true 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Shape_Length,-1,-1;Shape_Area \"Shape_Area\" true true true 8 Double 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,Shape_Area,-1,-1;ORIG_FID \"ORIG_FID\" true true false 0 Long 0 0,First,#,C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb\\Regularized_Tents_Point,ORIG_FID,-1,-1")[0]

    # Process: Calculate Field (2) (Calculate Field) (management)
    Washroom_Centroids_2_ = arcpy.management.CalculateField(in_table=Washroom_Centroids, field="WashID", expression="!ORIG_OID!", field_type=Field_Type_2_)[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb", workspace="C:\\Users\\and10749\\OneDrive - Esri\\Esri_Training\\SpatialAnalysis_Challenge\\Workflow\\NetworkAnalysis_Pro29_Build\\NetworkAnalysis_Package\\NetworkAnalysis_Package.gdb"):
        DataPreparation(*argv[1:])
