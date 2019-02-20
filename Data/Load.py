
import os, sys
import importlib
PATH = "/".join( os.path.abspath(__file__).split('/')[:-2])
sys.path.append(PATH)

#---------------------------------------------------------------
def FinData(dataset,select='',date='2000-01-01'):# dataset = 'CrudeOilPrices'
    if select in ['',[]]:
        select = FinDataList(dataset)
        
    if dataset not in ['TaiwanStockInfo','TaiwanStockPrice',
                       'TaiwanStockFinancialStatements','TaiwanStockStockDividend',
                       'TaiwanStockMarginPurchaseShortSale',
                       #-----------------------------------
                       'USStockInfo','USStockPrice',
                       #-----------------------------------
                       'JapanStockInfo','JapanStockPrice',
                       #-----------------------------------
                       'UKStockInfo','UKStockPrice',
                       #-----------------------------------
                       'EuropeStockInfo','EuropeStockPrice',
                       #-----------------------------------
                       'FinancialStatements','InstitutionalInvestorsBuySell',
                       'ExchangeRate','InstitutionalInvestors',
                       'InterestRate','GovernmentBonds','CrudeOilPrices',
                       'EnergyFuturesPrices','GoldPrice']:
        raise(AttributeError, "Hidden attribute")  
    else:
        data = getattr(importlib.import_module("FinMind.Data.{}".format(dataset)), dataset)(
                select = select,date = date)
        return data
#-------------------------------------------------------------------------------------------

def FinDataList(dataset):
    if dataset not in ['ExchangeRate','InstitutionalInvestors',
                       'InterestRate','GovernmentBonds',
                       'CrudeOilPrices','EnergyFuturesPrices']:
        raise(AttributeError, "Hidden attribute")  
    else:
        data = getattr(importlib.import_module("FinMind.Data.{}".format(dataset)), 'Load_Data_List')()
        return data

def CrawlerStockInfo(dataset = ''):

    data = getattr(importlib.import_module("FinMind.Data.{}".format(dataset)), dataset)(
            status = 'crawler')
    return data


