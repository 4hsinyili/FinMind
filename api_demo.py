
'''
example of loading FinMind api 
'''

from FinMind.Data import Load
import requests
import pandas as pd
url = 'http://finmindapi.servebeer.com/api/data'
list_url = 'http://finmindapi.servebeer.com/api/datalist'

'''----------------TaiwanStockInfo----------------'''
form_data = {'dataset':'TaiwanStockInfo',
             'stock_id':'',
             'date':''}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------TaiwanStockPrice----------------'''
form_data = {'dataset':'TaiwanStockPrice',
             'stock_id':['2330','2317'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()


'''----------------FinancialStatements----------------'''
form_data = {'dataset':'FinancialStatements',
             'stock_id':['2330','2317'],
             'date':'2019-01-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data = Load.transpose(data)
data.head()


'''----------------TaiwanStockStockDividend----------------'''
form_data = {'dataset':'TaiwanStockStockDividend',
             'stock_id':['2330','2317'],
             'date':'2018-01-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()


'''----------------TaiwanStockMarginPurchaseShortSale----------------'''
form_data = {'dataset':'TaiwanStockMarginPurchaseShortSale',
             'stock_id':['2330','2317'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------InstitutionalInvestorsBuySell----------------'''
form_data = {'dataset':'InstitutionalInvestorsBuySell',
             'stock_id':['2330','2317'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()


'''----------------Shareholding----------------'''
form_data = {'dataset':'Shareholding',
             'stock_id':['2330','2317'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------BalanceSheet----------------'''
form_data = {'dataset':'BalanceSheet',
             'stock_id':['2330','2317'],
             'date':'2019-01-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------TaiwanStockHoldingSharesPer----------------'''
form_data = {'dataset':'TaiwanStockHoldingSharesPer',
             'stock_id':['2330','2317'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------TaiwanStockMonthRevenue----------------'''
form_data = {'dataset':'TaiwanStockMonthRevenue',
             'stock_id':['2330','2317'],
             'date':'2019-01-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------USStockInfo----------------'''
form_data = {'dataset':'USStockInfo',
             'stock_id':'',
             'date':''}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------USStockPrice----------------'''
form_data = {'dataset':'USStockPrice',
             'stock_id':['^GSPC','^DJI'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------FinancialStatements----------------'''
form_data = {'dataset':'FinancialStatements',
             'stock_id':['AAPL'],
             'date':'2018-01-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------JapanStockInfo----------------'''
form_data = {'dataset':'JapanStockInfo',
             'stock_id':'',
             'date':''}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------JapanStockPrice----------------'''
form_data = {'dataset':'JapanStockPrice',
             'stock_id':['1352.T','1376.T'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------UKStockInfo----------------'''
form_data = {'dataset':'UKStockInfo',
             'stock_id':['2330','2317'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------UKStockPrice----------------'''
form_data = {'dataset':'UKStockPrice',
             'stock_id':['0TWH.L','0HZU.L'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------EuropeStockInfo----------------'''
form_data = {'dataset':'EuropeStockInfo',
             'stock_id':'',
             'date':''}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()
'''----------------EuropeStockPrice----------------'''
form_data = {'dataset':'EuropeStockPrice',
             'stock_id':['AB.PA','ABCA.PA'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()
'''----------------ExchangeRate----------------'''
form_data = {'dataset':'ExchangeRate',}
res = requests.post(
        list_url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = temp['data']
data
'''----------------ExchangeRate----------------'''
form_data = {'dataset':'ExchangeRate',
             'stock_id':['Canda', 'China', 'Euro', 'Japan', 'Taiwan', 'UK'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()
'''----------------InstitutionalInvestors----------------'''
form_data = {'dataset':'InstitutionalInvestors'}
res = requests.post(
        list_url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = temp['data']
data
'''----------------InstitutionalInvestors----------------'''
form_data = {'dataset':'InstitutionalInvestors',
             'stock_id':['Dealer', 'Dealer_Hedging', 'Foreign_Investor', 'Investment_Trust'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()
'''----------------InterestRate----------------'''
form_data = {'dataset':'InterestRate'}
res = requests.post(
        list_url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = temp['data']
data
'''----------------InterestRate----------------'''
form_data = {'dataset':'InterestRate',
             'stock_id':['BCB','BOC',],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()
'''----------------GovernmentBonds----------------'''
form_data = {'dataset':'GovernmentBonds'}
res = requests.post(
        list_url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = temp['data']
data
'''----------------GovernmentBonds----------------'''
form_data = {'dataset':'GovernmentBonds',
             'stock_id':['France 9-Month','France 9-Year'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()
'''----------------CrudeOilPrices----------------'''
form_data = {'dataset':'CrudeOilPrices'}
res = requests.post(
        list_url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = temp['data']
data
'''----------------CrudeOilPrices----------------'''
form_data = {'dataset':'CrudeOilPrices',
             'stock_id':['Brent', 'WTI'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()
'''----------------RawMaterialFuturesPrices----------------'''
form_data = {'dataset':'RawMaterialFuturesPrices'}
res = requests.post(
        list_url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = temp['data']
data
'''----------------RawMaterialFuturesPrices----------------'''
form_data = {'dataset':'RawMaterialFuturesPrices',
             'stock_id':['US Corn Futures','US Soybean Meal Futures',],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------GoldPrice----------------'''
form_data = {'dataset':'GoldPrice',
             'stock_id':'',
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

'''----------------CurrencyCirculation----------------'''
form_data = {'dataset':'CurrencyCirculation'}
res = requests.post(
        list_url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = temp['data']
data
'''----------------CurrencyCirculation----------------'''
form_data = {'dataset':'CurrencyCirculation',
             'stock_id':['Europe', 'Taiwan','US'],
             'date':'2019-06-01'}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data.head()

