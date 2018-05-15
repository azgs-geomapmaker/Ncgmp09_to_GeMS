import arcpy, shutil
from arcpy import env

# Set the workspace environment
#
#env.workspace = "C:\\Documents\\azgs\\mixed"

datasetitems = ["OrientationDataPoints",
         "SamplePoints",
         "StationPoints",
                "ContactsAndFaults",
         "MapUnitPolys",
         "OtherLines",
         "OverlayPolys"]
tableitems = ["DataSources",
         "DescriptionOfMapUnits",
         "ExtendedAttributes",
         "GeologicEvents",
         "Glossary",
         "Notes",
         "StandardLithology",
         "SysInfo"]
standaloneitems = ["CartographicLines",
         "DataSourcePolys"]
# List all  geodatabases in the current workspace 
# 
workspaces = arcpy.ListWorkspaces("*", "")    
for workspace in workspaces:
    env.workspace = workspace
    dsname = arcpy.Describe(workspace).name
    namepart = dsname.split(".")
    newname = namepart[0]
    datasetList = arcpy.ListDatasets("*", "Feature")
    for dataset in datasetList:
        print dataset
        fcList = arcpy.ListFeatureClasses("*","",dataset)
        fcList.sort()
        for fc in fcList:
            name = arcpy.Describe(fc).name
            print name
            if name not in datasetitems:
                ws2 = "C:\\Users\\lbookman.AZGS\\Documents\\ncgmp\\mixed\\" +  newname + ".gdb"
                print name + " not in dataset items, copying to ncgmp"
                arcpy.FeatureClassToFeatureClass_conversion(fc, ws2 + "\\GeologicMap", 
                                            name)    
    tables = arcpy.ListTables()
    for table in tables:
        print(table)
        tablename = arcpy.Describe(table).name
        if tablename not in tableitems:
            ws2 = "C:\\Users\\lbookman.AZGS\\Documents\\ncgmp\\mixed\\" +  newname + ".gdb"
            print tablename + " not in dataset items, copying to ncgmp"
            arcpy.TableToGeodatabase_conversion(table, ws2)
    featureClassList = arcpy.ListFeatureClasses("*","")
    featureClassList.sort()
    for featureclass in featureClassList:
        featureclassname = arcpy.Describe(featureclass).name
        print featureclassname
        if featureclassname not in standaloneitems:
            ws2 = "C:\\Users\\lbookman.AZGS\\Documents\\ncgmp\\mixed\\" +  newname + ".gdb"
            print featureclassname + " not in dataset items, copying to ncgmp"
            arcpy.FeatureClassToFeatureClass_conversion(featureclass, ws2 + "\\GeologicMap", featureclassname)
    print "copying additional data completed. . ."

