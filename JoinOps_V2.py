import pandas as pd
class JoinOps():

    
    
    def __init__ (self):
        self.df1 = pd.read_excel('agent.xlsx')
        self.df2 = pd.read_excel('customer.xlsx')
        self.df3 =  pd.read_excel('orders.xlsx')
    def df_join(self,left,right,p_left_on,p_right_on,p_how,vl=None,vr=None):
        left = eval("self."+left)
        right =eval( "self."+right)
        #left_on=self.df1[p_left_on] = eval("self."+p_left_on)
        #left_on=eval("self."+p_left_on)  
        #right_on=self.df1[p_right_on] = eval("self."+p_right_on)
        #right_on=eval("self."+p_right_on)
        if vl == None:
            vl = left.columns
        if vr ==None:
            vr = right.columns
        self.df= pd.merge(
                     left[vl],
                     right[vr],
                     left_on= p_left_on,
                     right_on=p_right_on,
                     how = p_how,
                     suffixes=('_left','_right'))
        return self.df
    def df_join2(self,right,p_left_on,p_right_on,p_how,vl=None,vr=None):
        left = self.df
        right =eval( "self."+right)
        if vl == None:
            vl = left.columns
        if vr ==None:
            vr = right.columns
        self.df= pd.merge(
                     left[vl],
                     right[vr],
                     left_on= p_left_on,
                     right_on=p_right_on,
                     how = p_how,
                     suffixes=('_left','_right'))
        return self.df