import pandas as pd
from guide.api.model.Connection import Connections
import pickle
import json

class  DataSource(Connections):
    def __init__(self,source_absolute_path_details,sourceType):
        super().__init__()
        self.source_absolute_path_details=source_absolute_path_details
        self.sourceType=sourceType
        self.metadata={}
    def getMetaData(self):
        if self.sourceType == 'excel':
            xls=pd.ExcelFile(self.source_absolute_path_details)
            self.metadata['sheet_names']=xls.sheet_names
            self.metadata['parameters']=pd.read_excel.__doc__.split("\n")
            return self.metadata
    def processRequest(self,operation,request_params):
        if operation not in ('showConnections','showConnectionData'):
            self.operation_status=0
            Connection_name=request_params['Connection_name']
            Connection_type=request_params['Connection_type']
            Connection_parameters=request_params['Connection_parameters']

            if operation == 'INSERT':
                self.insert(Connection_type,Connection_name,Connection_parameters)
            elif operation == 'UPDATE':
                self.update(Connection_name,Connection_parameters)
            elif operation == 'DELETE':
                self.delete(Connection_name)

            if self.operation_status == 0:
                staus_code=200
                message="connection created successfully"
            else:
                staus_code=400
                message="connection creation failed"
            self.processResponse(staus_code,message)
        else:
            self.operation_status=0
            if operation ==  'showConnectionData':
               self.showConnectionData(request_params['Connection_name'])
            else:
                self.showConnections(self)
                
            if self.operation_status == 0:
                staus_code=200
                message="selection operation successfully"
            else:
                staus_code=400
                message="selection operation failed"
            self.processResponse(staus_code,message,'YES')

    def processResponse(self,staus_code,message,showresult=None):
        if showresult:
            return json.dumps({'status_code':staus_code,'message':message,'result':self.result})
        return json.dumps({'status_code':staus_code,'message':message})