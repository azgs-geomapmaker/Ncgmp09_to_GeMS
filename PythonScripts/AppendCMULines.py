import arcpy, shutil
from arcpy import env

# Set the workspace environment
#
#env.workspace = "C:\\Documents\\azgs\\mixed"

# List all file geodatabases in the current workspace 
# 
workspaces = arcpy.ListWorkspaces("*", "")
for workspace in workspaces:
    name = arcpy.Describe(workspace).name
    namepart = name.split(".")
    newname = namepart[0]
    # Set local variables
    #
    featureclassin = "CMULines"
    featureclassout = "CMULines"
    inFC = "C:\\Users\\lbookman\\Documents\\ncgmp\\" + name + "\\CorrelationOfMapUnits\\" + featureclassin
    outFC = "C:\\Users\\lbookman\\Documents\\GeMS\\"+newname+".gdb\\CorrelationOfMapUnits\\" + featureclassout
    schemaType = "NO_TEST"
    subtype = ""

    # Set input field variables
    #
    infield1 = "CMULines_ID"
    infield2 = "Type"
    infield3 = "Symbol"
    

    # Set output field variables
    #
    outfield1 = "CMULines_ID"
    outfield2 = "Type"
    outfield3 = "Symbol"
    
   
    print "Adding " + featureclassin + "field map to. . ." + workspace
    # Create a fieldmappings object and two fieldmap objects
    #
    input1 = arcpy.FieldMap()
    input2 = arcpy.FieldMap()
    input3 = arcpy.FieldMap()
    

    fieldmappings = arcpy.FieldMappings()

    # Add input fields
    #   to fieldmap object.
    #
    input1.addInputField(inFC,infield1)
    input2.addInputField(inFC,infield2)
    input3.addInputField(inFC,infield3)
   

    # Set the Name of the Field output from this field map.
    #
    output1 = input1.outputField
    output1.name = (outfield1)
    input1.outputField = output1
    # Set the Name of the Field output from this field map.
    #
    output2 = input2.outputField
    output2.name = (outfield2)
    input2.outputField = output2
    # Set the Name of the Field output from this field map.
    #
    output3 = input3.outputField
    output3.name = (outfield3)
    input3.outputField = output3

    
    # Add the custom fieldmaps into the fieldmappings object.
    #
    fieldmappings.addFieldMap(input1)
    fieldmappings.addFieldMap(input2)
    fieldmappings.addFieldMap(input3)

    try:
        print "Appending data. . ."
        # Process: Append the feature classes into the empty feature class
        arcpy.Append_management(inFC, outFC, schemaType, fieldmappings, subtype)

    except:
        # If an error occurred while running a tool print the messages
        print arcpy.GetMessages()

    print "Append data to " + featureclassout + " " + newname + " complete. . ."

