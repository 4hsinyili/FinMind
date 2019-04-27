
TABLE = 'BalanceSheet'
import os, sys
import platform
if 'Windows' in platform.platform():
    PATH = "\\".join( os.path.abspath(__file__).split('\\')[:-1])
else:
    PATH = "/".join( os.path.abspath(__file__).split('/')[:-1])
sys.path.append(PATH)
from BasedClass import Load

class ClassBalanceSheet(Load):
    def __init__(self):
        super(ClassBalanceSheet, self).__init__(TABLE,'stock_id')

def BalanceSheet(select = [],date = '',year = '',season = ''):
    
    self = ClassBalanceSheet()
    if date and year and season:
        print("date and year,season can't input at the same time ")
        raise(AttributeError, "Hidden attribute")

    if isinstance(select,int): select = str(select)
    
    if isinstance(select,str) or isinstance(select,list):
        if date:
            data = self.load(select,date)
        elif year and season:
            data = self.load_season(select,year,season)

    else:
        raise(AttributeError, "Hidden attribute")  

    return data
