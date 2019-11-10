import pandas as pd
import cx_Oracle
def multi_df(filename):   
    source_absolute_path_details = filename
    metadata ={}
   # sourceType =='oracle':
    sevice_name = source_absolute_path_details['servicename']
    user = source_absolute_path_details['username']
    password = source_absolute_path_details['password']
    dsn_tns= cx_Oracle.makedsn('localhost','1521',service_name=sevice_name)
    conn = cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)
    df_schema = pd.read_sql('''select username from all_users''' , conn)
    metadata['schema'] = df_schema['USERNAME']
    df_table=pd.read_sql('''select * from {}'''.format('user_tables') , conn)
    metadata['table'] = df_table['TABLE_NAME']
    list_tab = source_absolute_path_details['tables']
    list_df =[]
    
    for i in list_tab:
        
        df = pd.read_sql('''select * from {}'''.format(i) , conn)
        list_df.append(df)
    
    return list_df ##it will return all data frames in list[] 
	


	

##testing function

import pandas as pd
filename = {
    "username": 'system',
    "password": 'VasuJay@1024',
    "HOST":'localhost',
    "PORT":1521,
    "servicename":'XE',
    "tables":['EMP','DEPT']}

dataframe = multi_df(filename) ##function  will return all data frames in list[] 
result = pd.merge(dataframe[0] ,
                 dataframe[1][['DEPTNO','DNAME']],
                 on='DEPTNO' ,how = 'left')
print(result)


