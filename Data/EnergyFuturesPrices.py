
TABLE = 'EnergyFuturesPrices'
import os, sys
import platform
if 'Windows' in platform.platform():
    PATH = "\\".join( os.path.abspath(__file__).split('\\')[:-1])
else:
    PATH = "/".join( os.path.abspath(__file__).split('/')[:-1])
sys.path.append(PATH)
from BasedClass import Load

class ClassEnergyFuturesPrices(Load):
    def __init__(self):
        super(ClassEnergyFuturesPrices, self).__init__(TABLE,'futures_type')

def EnergyFuturesPrices(select = [],date = ''):
    
    self = ClassEnergyFuturesPrices()  
    #stock = select
    if isinstance(select,int): select = str(select)
    
    if isinstance(select,str) or isinstance(select,list):
        return self.load(select,date)
        
    #elif isinstance(select,list):
    #    return self.load_multi(select,date)
    
    else:
        raise(AttributeError, "Hidden attribute")  

def Load_Data_List():
    self = ClassEnergyFuturesPrices()  
    return list( self.get_data_list() )


