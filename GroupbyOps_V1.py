import pandas as pd
import numpy as np
class GroupBy():

    def __init__ (self):
        
        self.dataframe = pd.read_excel('emp.xlsx')
        self.df = self.dataframe.copy()
        self.group_clause = list(self.df.columns)
    def Listagg(self,GroupIndx,ListaggIndx):
            return self.df.groupby( self.group_clause[GroupIndx])[ self.group_clause[ListaggIndx]].apply(lambda tags: ','.join(tags))
             
    def Group(self,GroupIndx,ValueIndx):
            return self.df.groupby( self.group_clause[GroupIndx])[ self.group_clause[ValueIndx]].sum().to_frame().reset_index()
             
    def Aggregate(self,GroupIndx,ValueIndx):
            self.Aggdf = self.df.groupby( self.group_clause[GroupIndx]).agg({ self.group_clause[ValueIndx]:['min','max','mean']})
            self.Aggdf.columns = ['_'.join(col).strip() for col in self.Aggdf.columns.values]
            return self.Aggdf.reset_index()
            
    def getGroupbyKey(self,GroupIndx,GroupbyKey):
            self.groupby = self.df.groupby( self.group_clause[GroupIndx])
            return self.groupby.get_group( GroupbyKey )
            
    def ListaggList(self,GroupIndx,ListaggIndx):
            return self.df.groupby( self.group_clause[GroupIndx])[ self.group_clause[ListaggIndx]].apply(lambda group_series: group_series.tolist()).reset_index()
             
    def GroupBySample(self,GroupIndx):
    
            return self.df.groupby( self.group_clause[GroupIndx]).apply(lambda group_df: group_df.sample(2)).reset_index(drop=True)
             
    def Group_Rank(self,GroupIndx,ValueIndx,col):
	       self.df[col]=df.groupby(self.group_clause[GroupIndx])[self.group_clause[ListaggIndx]].rank(method='dense')#method=first,min
		   return self.df