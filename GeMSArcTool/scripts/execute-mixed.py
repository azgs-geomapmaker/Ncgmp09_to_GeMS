import arcpy, os
from arcpy import env

executefile = ["execute-mixed.py"]

pathname = os.path.realpath(__file__)
pathname = pathname.split('\\')
pathname.pop()
pathname = '\\'.join(pathname)
arcpy.AddMessage("Path {0} ".format(pathname))

scripts = os.listdir(pathname)
            
            
arcpy.env.ncgmp09 = arcpy.GetParameterAsText(0)
arcpy.AddMessage("Msg {0} ".format(arcpy.env.ncgmp09))
arcpy.env.gems = arcpy.GetParameterAsText(1)
arcpy.AddMessage("Msg123 {0} ".format(arcpy.env.gems))

for script in scripts:
    if script.endswith(".py"):
		if script not in executefile:
			arcpy.AddMessage("Msg {0} ".format(script))
			arcpy.AddMessage("Msg {0} ".format(env.workspace))
			execfile(pathname + "\\" +script, {"env.workspace": env.workspace})