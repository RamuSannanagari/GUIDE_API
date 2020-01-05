import pandas as pd
import numpy as np
class DataShow():

    def __init__ (self):
        
        self.dataframe = pd.read_excel('emp.xlsx')
        self.df = self.dataframe.copy()

        self.Select_clause = {'vcol':[[k,v] for k, v in dict(self.df.dtypes).items()],'alias' :list(self.df.columns)}
        self.Immutable_columns = [[k,v] for k, v in dict(self.df.dtypes).items()]
        self.Immutable_columns =[tuple(element) for element in self.Immutable_columns]
        self.Immutable_columns = tuple(self.Immutable_columns)
    def Remove(self,Deleteindx):
        
        del self.Select_clause['vcol'][Deleteindx] 
        del self.Select_clause['alias'][Deleteindx] 
        #self.Select_clause['vcol'] = [v for i, v in enumerate(self.Select_clause['vcol']) if i not in Deleteindx]
        #self.Select_clause['alias'] = [v for i, v in enumerate(self.Select_clause['alias']) if i not in Deleteindx]
    def Insert(self,IndxPosition,ColIndex):
        self.Select_clause['vcol'].insert(IndxPosition,list(self.Immutable_columns[ColIndex]))
        self.Select_clause['alias'].insert(IndxPosition,self.Immutable_columns[ColIndex][0])

	#def Insert(self,IndxPosition,Col,alias = None):
    #    self.Select_clause['vcol'].insert(IndxPosition,Col)
    #    if alias != None:
    #        self.Select_clause['alias'].insert(IndxPosition,alias)
    #    else:
    #        self.Select_clause['alias'].insert(IndxPosition,Col)
    def AddCol(self,ColIndex):
        self.Select_clause['vcol'].append(list(self.Immutable_columns[ColIndex]))
        self.Select_clause['alias'].append(self.Immutable_columns[ColIndex][0])
		
	#def AddCol(self,Col,alias = None):
    #    self.Select_clause['vcol'].append(col)
	#	if alias != None:
    #        self.Select_clause['alias'].append(alias)
	#	else:
	#	    self.Select_clause['alias'].append(Col)
		
    def Pop(self,IndxPosition):
        fromIndx =[]
        fromIndx.append(self.Select_clause['vcol'].pop(IndxPosition))
        fromIndx.append(self.Select_clause['alias'].pop(IndxPosition))
        #print(fromIndx[0])
        return fromIndx
    def Swap(self,FromIndx,ToIndx):
        ToVal= self.Pop(FromIndx)
		#call insert method
        self.Select_clause['vcol'].insert(ToIndx,ToVal[0])
        self.Select_clause['alias'].insert(ToIndx,ToVal[1])
    def UpdateAlias(self,AliasIndx,Newcol):
        try:
            if alias in self.Select_clause['alias']:
                raise NameError("Duplicates alias name is not allowed") 
        except NameError:
            raise
        self.Select_clause['alias'][AliasIndx]= Newcol
    def UpdateCol(self,ColIndx,Newcol):
        self.Select_clause['vcol'][ColIndx]=Newcol
    def ApplyMethods(self,str_txt,alias):
        #try:
        string=eval("self.df."+str_txt)
            
        #except Exception:
        #    string=eval("self.df."+str_txt+".str")
        #df = pd.read_excel('emp.xlsx')  
        #emplist =list(df.columns)
        #print(string)
        try:
            if alias in self.Select_clause['alias']:
                raise NameError("Duplicates alias name is not allowed") 
        except NameError:
            raise 
            #'Duplicates alias name is not allowed '
                #print(alias)
                #print(self.Select_clause['vcol'])
                #del self.Select_clause['vcol'][self.Select_clause['vcol'].index([alias])]
                #del self.Select_clause['alias'][self.Select_clause['alias'].index(alias)]
            
        self.Select_clause['vcol'].append([alias])
        self.Select_clause['alias'].append(alias)
        #try:
            
        self.df[alias] = string
        #except AttributeError:
        #    string=eval("self.df."+str_txt+".str")
        #    self.df[alias] = string
    def Extract(self,date,extract_val,alias):
        string=eval("self.df."+date+".dt."+extract_val)
        try:
            if alias in self.Select_clause['alias']:
                raise NameError("Duplicates alias name is not allowed") 
        except NameError:
            raise 
            #print(alias)
            #print(self.Select_clause['vcol'])
            #del self.Select_clause['vcol'][self.Select_clause['vcol'].index([alias])]
            #del self.Select_clause['alias'][self.Select_clause['alias'].index(alias)]
        
        self.Select_clause['vcol'].append([alias])
        self.Select_clause['alias'].append(alias)
        self.df[alias] = string
    def Date_Arthimatices(self,date,DateOptions,alias):
        dt = eval("pd.DateOffset("+DateOptions+")")
        inputdate=eval("self.df."+date)
        string = inputdate+dt
        #df.hiredate+pd.DateOffset(days=2)
        try:
            if alias in self.Select_clause['alias']:
                raise NameError("Duplicates alias name is not allowed") 
        except NameError:
            raise 
            #print(alias)
            #print(self.Select_clause['vcol'])
            #del self.Select_clause['vcol'][self.Select_clause['vcol'].index([alias])]
            #del self.Select_clause['alias'][self.Select_clause['alias'].index(alias)]
        
        self.Select_clause['vcol'].append([alias])
        self.Select_clause['alias'].append(alias)
        self.df[alias] = string
    
    def IfElse(self,col,alias,Decode_val={}):
	
        dic = dict(Decode_val)
        #syntax {'column name': dictionary of desired replacements}
        
        try:
            if alias in self.Select_clause['alias']:
                raise NameError("Duplicates alias name is not allowed") 
        except NameError:
            raise 
        
        self.Select_clause['vcol'].append([alias])
        self.Select_clause['alias'].append(alias)
		#df['D'] = df['C'].replace(['a', 'c'], 'A')
        
        self.df[alias] = self.df[col].replace(Decode_val)
        #Decode_val={10:'ten',20:'twenty',30:'thirty'}
        
    def Show(self):
        #elf.df = pd.read_excel('emp.xlsx')
        print(self.Select_clause)
        del self.dataframe
        self.dataframe = self.df[[item[0] for item in self.Select_clause['vcol']]]
        #self.df = self.df[self.Select_clause['vcol'][0][0]]
        self.dataframe.columns=self.Select_clause['alias']
        
        return self.dataframe
    def ShowDuplicates(self):
        return self.df[self.df.duplicated()]
    def ShowDistinct(self):
        return self.df.drop_duplicates()
    def SampleData(self,No_of_Rows):
        random_indices = np.random.choice(self.df.index.values, No_of_Rows, replace=False)

        return self.df.loc[random_indices]
    #def Sort(self,Sortcol):
    #    return self.df.sort_values(Sortcol)
    def Sort(self,SortcolIndx):
        return self.df.sort_values(self.Select_clause['alias'][SortcolIndx])
    def TopN(self,No_of_Rows,cols):
        return self.df.nlargest(No_of_Rows, cols, keep='first')
    #multiple columns allow to select
    def BottomN(self,No_of_Rows,cols):
        return self.df.nsmallest(No_of_Rows, cols, keep='first')   
    