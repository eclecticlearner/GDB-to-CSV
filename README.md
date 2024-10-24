# GDB-to-CSV

This is a python toolbox (PYT) that should be added to an ESRI ArcGIS Pro project.
The purpose is to export all feature class attribute tables from a geodatabase to a CSV file.  This tool works whether feature classes are stored in a feature dataset or not.  This version was initially created to only export certain fields from each feature class.  If a field is not found in a feature class the value of "" is given to that field for that feature class.  

The end user will need to open the pyt file in a code or text editor (such as the built in python window in ESRI ArcGIS Pro) and change the values of the “output_fields” variable to be a specific list of desired fields to be exported.

Future versions may include all fields, and may have a different default value to avoid confusion.  
Future versions may have an input text box for the user to specify the field names they wish to export from all feature classes.

