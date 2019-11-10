import pandas as pd



from collections import defaultdict



class xlsxFileNsheets():

        def __init__(self,filename,filetype):

            self.filename = filename

            self.filetype = filetype

        def xlsxNsheets(self):

            excel_file = pd.ExcelFile(self.filename) 

            sheets = excel_file.sheet_names

            return sheets



class Dataframe_creation(xlsxFileNsheets):

        def __init__(self,filename,filetype,sheetname):

            super().__init__( filename, filetype)

            self.filename = filename

            #self.filetype = filetype

            self.sheetname = sheetname

            self.sheets = xlsxFileNsheets.xlsxNsheets(self)

            self.excel_file = pd.ExcelFile(self.filename) 

            

        def DataFrame_xlsc(self):

            

                if self.sheetname in self.sheets:

                    df = self.excel_file.parse(self.sheetname) 

                    return df

class DataSource(Dataframe_creation):

    

    def __init__ (self,inputval):

        

            super().__init__( inputval ['filename'],inputval ['type'] ,inputval ['sheet'])

            self.defaultinput = inputval

            self.defaultinput = defaultdict(lambda: 'No Values', self.defaultinput)

            self.shared_column_ind =self.defaultinput ['selcol']

            self.filename=self.defaultinput ['filename']

            self.filetype=self.defaultinput ['type']

            self.sheetname=self.defaultinput ['sheet']

            self.condition = self.defaultinput['where']

            self.group = self.defaultinput['group']

            self.agr = self.defaultinput['agr']

            self.distinct = self.defaultinput['distinct']

            self.sort = self.defaultinput['sort']

            self.rank = self.defaultinput['rank']

            self.df  = Dataframe_creation.DataFrame_xlsc(self)

            if self.condition == 'No Values':

                 self.whr_val = '0'

            else:

                self.whr_val=  (self.df[self.condition[0][0]] == self.condition[0][1]) | (self.df[self.condition[1][0]]  == self.condition[1][1])

            

            

            

    

    def Show_The_Result(self):

        try:

            if self.condition !='No Values' and self.group !='No Values' and self.agr != 'No Values' and self.distinct =='distinct':

                self.result = self.df[self.whr_val].groupby(self.group).agg({self.agr[0]:self.agr[1]})

                return self.result                        

            elif self.group !='No Values' and self.agr != 'No Values' :

                self.result = self.df.groupby(self.group).agg({self.agr[0]:self.agr[1]})

                return self.result

            elif self.shared_column_ind != 'No Values' and self.group !='No Values' and self.rank != 'No Values' :

                #self.result = self.df.groupby(self.group).agg({self.agr[0]:self.agr[1]})

                self.df['rank'] = self.df[self.shared_column_ind].groupby(self.group)[self.rank].rank(method='first')

                return self.df

            elif self.condition !='No Values' and self.group !='No Values':

                self.result = self.df[self.whr_val].groupby(self.group)

                return self.result    

            elif self.condition =='No Values' and self.group !='No Values' and self.distinct =='distinct':
                self.df = self.df.drop_duplicates()
                self.result = self.df.groupby(self.group)

                return self.result
            elif self.condition =='No Values' and self.group !='No Values' and self.distinct =='No Values':

                self.result = self.df.groupby(self.group)

                return self.result

            elif len(self.shared_column_ind) == 0 and self.distinct =='No Values' and self.condition !='No Values' :

                self.result= self.df[self.whr_val]

                return self.result

            elif len(self.shared_column_ind) == 0 and self.distinct =='distinct' and self.condition !='No Values' :

                self.result = self.df[self.whr_val].drop_duplicates()

                return self.result

            elif len(self.shared_column_ind) != 0 and self.distinct =='No Values' and self.condition !='No Values' :

                self.result = self.df[self.shared_column_ind][self.whr_val].drop_duplicates()

                return self.result

            elif self.shared_column_ind != 'No Values' and self.distinct =='distinct' and self.condition !='No Values' :

                self.result = self.df[self.shared_column_ind][self.whr_val].drop_duplicates()

                return self.result

            elif self.shared_column_ind != 'No Values' and self.distinct =='No Values' :

                self.result = self.df[self.shared_column_ind]

                return self.result

            elif self.shared_column_ind != 'No Values' and self.distinct =='distinct' :

                self.result =  self.df[self.shared_column_ind].drop_duplicates()

                return self.result

        except:

            print("shared column not exist")

            raise

            

