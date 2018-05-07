import arcpy, os
from arcpy import env

env.workspace = "C:\\Users\\lbookman\\Documents\\ncgmp"
executefile = ["execute-mixed.py"]
scripts = os.listdir("C:\\Users\\lbookman\\Documents\\transfer-data-to-ncgmp09-master_LB")
for script in scripts:
    if script.endswith(".py"):
        if script not in executefile:
            print (script)
            execfile(script, {"env.workspace": env.workspace})
            