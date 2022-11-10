import os
import arcpy

# Set the input workspace, get the feature class name to copy
#  and the output location.
arcpy.env.workspace = "file/open"
arcpy.env.workspace = arcpy.GetParameterAsText(0)
in_featureclass = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)

out_featureclass = os.path.join(out_workspace,
                                os.path.basename(in_featureclass))
print arcpy.env.workspace, in_featureclass, out_featureclass, out_workspace
# Copy feature class to output location
arcpy.CopyFeatures_management(in_featureclass, out_featureclass)