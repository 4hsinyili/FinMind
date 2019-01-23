
TABLE = 'TaiwanStockPrice'
import pandas as pd
import os, sys
PATH = "/".join( os.path.abspath(__file__).split('/')[:-1])
sys.path.append(PATH)
from BasedClass import Load,execute_sql2


class ClassStockPrice(Load):
    def __init__(self):
        super(ClassStockPrice, self).__init__(TABLE,'stock_id')
        
    def load(self,select = '',date = ''):
        
        colname = execute_sql2( 'SHOW COLUMNS FROM `{}_TW`'.format( select ),database = TABLE )
        select = '{}_TW'.format(select)
            
        colname = [ c[0] for c in colname if c[0] not in  ['id','url'] ]              
        
        sql = 'select `{}` from `{}`'.format( '`,`'.join( colname ) ,select)
        
        if date != '':
            sql = "{} WHERE `date` >= '{}' ".format(sql,date)
           
        data = execute_sql2( sql ,database = TABLE)
        data = pd.DataFrame(list(data))
        if len(data)>0:
            
            data.columns = colname
            
            if self.select_variable in data.columns:
                data = data.sort_values([self.select_variable,'date'])
            else:
                data = data.sort_values('date')
            data.index = range(len(data))
            data['stock_id'] = select.split('_')[0]

        return data
    
    def get_data_list(self):
        tem = execute_sql2( 'SHOW TABLES',database = TABLE )
        return [ te[0].split('_')[0] for te in tem ]
        
def StockPrice(select = [],date = ''):
    
    self = ClassStockPrice()  
    #stock = select
    if isinstance(select,int): select = str(select)
    
    if isinstance(select,str):
        return self.load(select,date)
        
    elif isinstance(select,list):
        return self.load_multi(select,date)
    
    else:
        raise(AttributeError, "Hidden attribute")  
