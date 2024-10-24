# GDB-to-CSV

This is a python toolbox (PYT) that should be Added to an ESRI ArcGIS Pro project.
The purpose is to export all featureclass atrribute tables from a geodatabase to a CSV file.  This tool works whether featureclasses are stored in a featuredataset or not.  This version was intially created to only export certain fields from each feature class.  If a field is not found in a featureclass the value of "" is given to that field for that featureclass.  Future versions may include all fields , and may have a different default value to avoid confusion.  


