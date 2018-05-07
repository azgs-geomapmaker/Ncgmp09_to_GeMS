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
    featureclassin = "Glossary"
    featureclassout = "Glossary"
    inFC = "C:\\Users\\lbookman\\Documents\\ncgmp\\" + name + "\\" + featureclassin
    outFC = "C:\\Users\\lbookman\\Documents\\GeMS\\"+newname+".gdb\\" + featureclassout
    schemaType = "NO_TEST"
    subtype = ""

    # Set input field variables
    #
    infield1 = "Glossary_ID"
    infield2 = "Term"
    infield3 = "Definition"
    infield4 = "DefinitionSourceID"

    # Set output field variables
    #
    outfield1 = "Glossary_ID"
    outfield2 = "Term"
    outfield3 = "Definition"
    outfield4 = "DefinitionSourceID"
   
    print "Adding " + featureclassin + " field map to. . ." + workspace
    # Create a fieldmappings object and two fieldmap objects
    #
    input1 = arcpy.FieldMap()
    input2 = arcpy.FieldMap()
    input3 = arcpy.FieldMap()
    input4 = arcpy.FieldMap()

    fieldmappings = arcpy.FieldMappings()

    # Add input fields
    #   to fieldmap object.
    #
    input1.addInputField(inFC,infield1)
    input2.addInputField(inFC,infield2)
    input3.addInputField(inFC,infield3)
    input4.addInputField(inFC,infield4)    

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
    # Set the Name of the Field output from this field map.
    #
    output4 = input4.outputField
    output4.name = (outfield4)
    input4.outputField = output4
   
    # Add the custom fieldmaps into the fieldmappings object.
    #
    fieldmappings.addFieldMap(input1)
    fieldmappings.addFieldMap(input2)
    fieldmappings.addFieldMap(input3)
    fieldmappings.addFieldMap(input4)

    try:
        print "Appending data. . ."
        # Process: Append the feature classes into the empty feature class
        arcpy.Append_management(inFC, outFC, schemaType, fieldmappings, subtype)

    except:
        # If an error occurred while running a tool print the messages
        print arcpy.GetMessages()

    print "Append data to " + featureclassout + " " + newname + " complete. . ."

