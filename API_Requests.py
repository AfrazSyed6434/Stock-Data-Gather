import requests
import json
import inspect

from datetime import datetime
api_token = '0ff0c8353aa45686bd999f354792fe22:5593a83b9e79b5ce0e9eef0288b3ef4c'

def stockSummaryData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/summary'
    response = requests.get(url)
    data = response.json()
    # # with open("stockSummaryData2.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

def companyFinancialData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/financials'
    response = requests.get(url)
    data = response.json()
    # with open("companyFinancialData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()


def companyKeyStatisticsData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/keyratios'
    response = requests.get(url)
    data = response.json()
    # with open("companyKeyStatisticsData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

def companyCurrentQuoteData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/quote'
    response = requests.get(url)
    data = response.json()
    # with open("companyCurrentQuoteData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

def stockHistoricalPriceData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    # url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/quote
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/price_ohlc'
    response = requests.get(url)
    data = response.json()
    # with open("stockHistoricalPriceData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()
    

def historicalOwnershipData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/indicator_history'
    response = requests.get(url)
    data = response.json()
    # with open("historicalOwnershipData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

def realTimeGuruTrades(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/gurus'
    response = requests.get(url)
    data = response.json()
    # with open("realTimeGuruTrades.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

# def realTimeInsiderTrades
def realTimeInsiderTrades(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/insider'
    response = requests.get(url)
    data = response.json()
    # with open("realTimeInsiderTrades.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

def dividendHistoryData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/dividend'
    response = requests.get(url)
    data = response.json()
    # with open("dividendHistoryData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

def analystEstimateData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/analyst_estimate'
    response = requests.get(url)
    data = response.json()
    # with open("analystEstimateData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

def operatingData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/operating_data'
    response = requests.get(url)
    data = response.json()
    # with open("operatingData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

def segmentsData(company_symbol):
    current_frame = inspect.currentframe()
    function_name = inspect.getframeinfo(current_frame).function
    print(f"{datetime.now()} : Started gathering {function_name} for {company_symbol} ")
    url = f'https://api.gurufocus.com/public/user/{api_token}/stock/{company_symbol}/segments_data'
    response = requests.get(url)
    data = response.json()
    # with open("segmentsData.json", "w") as outfile:
        # pass
    if response.status_code!=200:
        print("Error gettting data from "+function_name+" endpoint")
        print(response.json())
        return None
    return response.json()

endpoints_map = {
    'Stock Summary Data': stockSummaryData,
    'Company Financial Data': companyFinancialData,
    'Company Key Statistics Data': companyKeyStatisticsData,
    'Company Current Quote Data': companyCurrentQuoteData,
    'Stock Historical Price': stockHistoricalPriceData,
    'Historical Ownership Data': historicalOwnershipData,
    'Real-time Guru Trades': realTimeGuruTrades,
    'Real-Time Insider Trades': realTimeInsiderTrades,
    'Dividend History Data': dividendHistoryData,
    'Analyst Estimate Data': analystEstimateData,
    'Operating Data': operatingData,
    'Segments Data': segmentsData
}

