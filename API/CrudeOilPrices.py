
TABLE = 'CrudeOilPrices'
from BasedClass import Load

class ClassCrudeOilPrices(Load):
    def __init__(self):
        super(ClassCrudeOilPrices, self).__init__(TABLE,'name')

def CrudeOilPrices(select = [],date = ''):
    
    self = ClassCrudeOilPrices()  
    #stock = select
    if isinstance(select,int): select = str(select)
    
    if isinstance(select,str):
        return self.load(select,date)
        
    elif isinstance(select,list):
        return self.load_multi(select,date)
    
    else:
        raise(AttributeError, "Hidden attribute")  
    

def Load_Data_List():
    self = ClassCrudeOilPrices()  
    return list( self.get_data_list() )


