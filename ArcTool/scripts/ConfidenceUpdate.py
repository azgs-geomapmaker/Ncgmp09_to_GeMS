import arcpy, shutil
from arcpy import env

# Set the workspace environment
#
#env.workspace = "C:\\Documents\\ncgmp\\mixed\\"

confidenceitems = ["ExistenceConfidence",
         "IdentityConfidence",
                   "GeneralLithologyConfidence"]
# List all  geodatabases in the current workspace 
# 
workspaces = arcpy.ListWorkspaces("*", "")    
for workspace in workspaces:
    env.workspace = workspace
    datasetList = arcpy.ListDatasets("*", "Feature")
    for dataset in datasetList:
        print dataset
        fcList = arcpy.ListFeatureClasses("*","",dataset)
        fcList.sort()
        for fc in fcList:
            name = arcpy.Describe(fc).name
            print name
            fieldList = arcpy.ListFields(fc)
            for field in fieldList:
                name = field.name
                print name
                if name in confidenceitems:
                    print "Calculating " + name + " confidence items, copy to"
                    arcpy.CalculateField_management (fc, name, '"certain"', "PYTHON")
    tables = arcpy.ListTables()
    for table in tables:
        print(table)
        fieldList = arcpy.ListFields(table)
        for field in fieldList:
            name = field.name
            print name
            if name in confidenceitems:
                print "Calculating " + name + " not in confidence items, copy to"
                arcpy.CalculateField_management (table, name, '"certain"', "PYTHON")

    print "updating Identity Confidence and Existence Confidence fields completed. . ."

