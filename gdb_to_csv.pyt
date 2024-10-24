class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "GIS to GDB Tools"
        self.alias = "GIS to GDB Tools"
        self.tools = [GDBtoCSV]

class GDBtoCSV(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "2. Export GDB To CSV"
        self.alias = "GDB To CSV"
        self.description = "Converts GDB Layer attributes to CSV"
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        
        inputGDB = arcpy.Parameter(
        displayName="Input GDB",
        name="inputGDB",
        datatype="Workspace",
        parameterType="Required",
        direction="Input")

        
        outputCSV = arcpy.Parameter(
        displayName="Output CSV",
        name="outputCSV",
        datatype="file",
        parameterType="Required",
        direction="Output")
        outputCSV.filter.list = ['csv']

        parameters = [inputGDB, outputCSV]
        return parameters

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.env.workspace = parameters[0].valueAsText
        newCSV = parameters[1].ValueAsText            
        datasetList = arcpy.ListDatasets("*", "Feature")
        
        # Change this variable to list of fields to be exported
        output_fields = [field1, field2, field3, etc]

       # Function if featureclasses are not in a feature dataset
        def nofds():
                fcList = arcpy.ListFeatureClasses("*")
                for fc in fcList:
                    with arcpy.da.SearchCursor(fc, '*') as cursor:
                        for row in cursor:
                            record = dict(zip(cursor.fields, row))
                            values = [record.get(key, None) for key in output_fields]
                            writer.writerow(values)
        
      # Function if featureclasses are in a feature dataset
        def fds():
                for dataset in datasetList:
                    fcList = arcpy.ListFeatureClasses("*","",dataset)
                    for fc in fcList:
                        with arcpy.da.SearchCursor(fc, '*') as cursor:
                            for row in cursor:
                                record = dict(zip(cursor.fields, row))
                                values = [record.get(key, None) for key in csvList]
                                writer.writerow(values)

        with open(newCSV, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csvList)
            nofds()
            fds()
