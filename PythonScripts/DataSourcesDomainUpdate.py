import arcpy, shutil
from arcpy import env

# Set the workspace environment
#
#env.workspace = "C:\\Documents\\ncgmp\\mixed\\"

# List all file geodatabases in the current workspace 
# 
workspaces = arcpy.ListWorkspaces("*", "")
for workspace in workspaces:
#name = arcpy.Describe(workspace).name

# Set local variables
#
    in_table = workspace + "\\DataSources"
    code_field = "DataSources_ID"
    description_field = "Source"
    in_workspace = workspace
    domain_name = "d_DataSources"
    domain_description = "Data Sources"
    update_option = "APPEND"    

    try:
        print "Updating " + domain_name +". . ."
        # Process: Append the feature classes into the empty feature class
        arcpy.TableToDomain_management (in_table,
                                    code_field,
                                    description_field,
                                    in_workspace,
                                    domain_name,
                                    domain_description,
                                    update_option)

    except:
        # If an error occurred while running a tool print the messages
        print arcpy.GetMessages()

    print "d_DataSources domain update completed. . ."

