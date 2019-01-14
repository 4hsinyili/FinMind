

TABLE = 'USStockInfo'

import pandas as pd
import os, sys
PATH = "/".join( os.path.abspath(__file__).split('/')[:-1])
sys.path.append(PATH)
from BasedClass import execute_sql2

class ClassUSStockInfo:
    def __init__(self):
        pass

    def load_all(self,status = 'package'):
        colname = execute_sql2( 'SHOW COLUMNS FROM {}'.format( TABLE ) )
        colname = [ c[0] for c in colname if c[0] not in  ['id','url'] ]     
        colname.remove('date')
        sql = 'select `{}` from {}'.format( '`,`'.join( colname ) ,TABLE)
        tem = execute_sql2(sql)
        data = pd.DataFrame( list(tem) )
        data.columns = colname
        if status == 'package':
            sql = 'SHOW TABLES '
            tem = execute_sql2(sql,TABLE.replace('Info','Price'))
            stock_id = [ te[0] for te in tem ]
            bo = [ True if x in stock_id else False for x in data['stock_id'] ]
            data = data[bo]
            data.index = range(len(data))
        
        return data

def USStockInfo(select = [],date = '',status = 'package'):
    
    self = ClassUSStockInfo()  
    data = self.load_all(status)
        
    return data


