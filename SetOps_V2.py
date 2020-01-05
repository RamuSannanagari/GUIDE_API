import pandas as pd
import numpy as np
import datacompy as dc
class SetOps():

    def __init__ (self):
        
        self.df1 = pd.read_excel('emp2.xlsx')
        self.df2 = pd.read_excel('emp3.xlsx')
        

        #self.Select_clause = {'vcol':[[k,v] for k, v in dict(self.df.dtypes).items()],'alias' :list(self.df.columns)}
        #self.Immutable_columns = [[k,v] for k, v in dict(self.df.dtypes).items()]
        #self.Immutable_columns =[tuple(element) for element in self.Immutable_columns]
        #self.Immutable_columns = tuple(self.Immutable_columns)
    def df_compare(self,joincolumns):
        self.compare = dc.Compare(
                                    self.df1,
                                    self.df2,
                                    #df3,
                                    
                                    join_columns=joincolumns,  #You can also specify a list of columns eg ['policyID','statecode']
                                    abs_tol=0, #Optional, defaults to 0
                                    rel_tol=0, #Optional, defaults to 0
                                    df1_name='Original', #Optional, defaults to 'df1'
                                    df2_name='New' #Optional, defaults to 'df2'
                                    )
        report = self.compare.report()
        #return report
        print(report)
    def df_matches(self):
        """Return True or False if the dataframes match."""
        return self.compare.matches()
    def df_columns_count_matches(self):
        """Whether the columns all match in the dataframes"""
        #return self.compare.all_columns_match()
        
        return self.compare.all_columns_match()
    #def df_columns_matches(self,change):
    #    
    #    if len(set(self.df1.columns)-set(self.df2.columns)) !=0 :
    #        #change = input("rename dataframe columns from and to: ")
    #        if change =='Y':
    #            self.df1.columns=self.df2.columns
    #       # self.change[0].columns=self.change[2].columns
    #    return self.df1.columns.equals(self.df2.columns)
    def df_columns_matches(self,change,from_df,to_df):
        
        if self.df1.columns . equals(self.df2.columns) ==False :
            #change = input("rename dataframe columns from and to: ")
            
            if change =='Y' and from_df == 'df1':
                self.df2.columns=self.df1.columns
            elif change =='Y' and from_df == 'df2':
                self.df1.columns=self.df2.columns
                
           # self.change[0].columns=self.change[2].columns
        else:
            return self.df1.columns . equals(self.df2.columns)
    def df_columns_dtypes_matches(self,change,from_df,to_df):
        
        if self.df1.dtypes . equals(self.df2.dtypes) ==False :
            #change = input("rename dataframe columns from and to: ")
            
            if change =='Y' and from_df == 'df1':
                self.df2=self.df2.astype(self.df1.dtypes)
            elif change =='Y' and from_df == 'df2':
                self.df1=self.df1.astype(self.df2.dtypes)
                
           # self.change[0].columns=self.change[2].columns
        else:
            return self.df1.dtypes . equals(self.df2.dtypes)
           
    def df_df1_mismatch_columns(self):
        """Get columns that are not in df2"""
        return self.compare.df1_unq_columns()
    def df_df2_mismatch_columns(self):
        """Get columns that are not in df1"""
        return self.compare.df2_unq_columns()
    def df_common_columns(self):
        """Get common columns between two dataframes"""
        return self.compare.intersect_columns()
    def df_all_mismatches(self):
        """Get not common columns between two dataframes"""
        return set(self.df1).symmetric_difference(self.df2)
    def df_union(self):
        return pd.concat([self.df1,self.df2],join ='inner')
    def df_union_all(self):
        return pd.concat([self.df1,self.df2],ignore_index=True)
    def df_intersect(self):
        return pd.merge(self.df1,self.df2,how = 'inner')
    def df_minus_df1(self):
        return self.df1.merge(self.df2, how = 'outer',indicator =True).loc[lambda x : x['_merge']=='left_only']
    def df_minus_df2(self):
        return self.df2.merge(self.df1, how = 'outer',indicator =True).loc[lambda x : x['_merge']=='left_only']
    def df_except(self):
        return pd.concat([self.df1,self.df2]).drop_duplicates(keep=False)