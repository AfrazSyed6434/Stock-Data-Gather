import json
from utils import *
# Open the file
from API_Requests import *
dataframe_options = {
        "Company_General_Data": pd.DataFrame(),
        "Company_Ratio_Data": pd.DataFrame(),
        "Company_Financial_Data": pd.DataFrame(),
        "Real_Time_Trades": pd.DataFrame(),
        "Analyst_Estimate_Data": pd.DataFrame(),
        "Dividend_History_Data": pd.DataFrame(),
        "Stock_History_Data": pd.DataFrame(),
    }
# with open("stockHistoricalPriceData.json", "r") as file:
#     # Read the contents of the file
#     data = json.load(file)

# Access the data in the file
# async def start2():
#     # data2= await stockHistoricalPriceData("AAPL")
#     x=await processStockHistoricalPriceData("APPLE","analyst Estimate","APPL",data)
#     # x=await generalDataParser("APPLE","stockSummaryData","AAPL",data,"")
#     x.to_excel(f"test2.xlsx", index=False)
#     return x

async def processStockHistoricalPriceData(company_name, category, company_symbol, data,metadata):
    df = pd.DataFrame(columns=data[0].keys())
    company_symbols = []
    company_names = []
    categories = []
    for d in data:
        company_symbols.append(company_symbol)
        company_names.append(company_name)
        categories.append(category)
        df = pd.concat([df,pd.DataFrame([d])], ignore_index=True)
    # df.insert(0, 'Company Name', company_names)
    df.insert(0, 'Symbol', company_symbols)
    df.insert(1,"Category",categories)
    dataframe_options["Stock_History_Data"]=pd.concat([dataframe_options["Stock_History_Data"],df],ignore_index=True)

    return df

async def processDividentHistoryData(company_name, category, company_symbol, data,metadata):
    if len(data)==0:
        return None
    df = pd.DataFrame(columns=data[0].keys())
    company_symbols = []
    company_names = []
    categories = []
    for d in data:
        company_symbols.append(company_symbol)
        company_names.append(company_name)
        categories.append(category)
        df = pd.concat([df,pd.DataFrame([d])], ignore_index=True)
    # df.insert(0, 'Company Name', company_names)
    df.insert(0, 'Symbol', company_symbols)
    df.insert(1,"Category",categories)
    dataframe_options["Dividend_History_Data"]=pd.concat([dataframe_options["Dividend_History_Data"],df],ignore_index=True)

    return df
    pass
async def processAnalystEstimateData(company_name, category, company_symbol, data,metadata):
    # rows = []
    dfMain=pd.DataFrame()
    # extra_cols={}
    company_symbols = []
    company_names = []
    categories = []
    for key, values in data.items():
        dfSub=pd.DataFrame()
        key_nums=0
        for types,data in values.items():
            if type(data)==list:
                key_nums=len(data)
                dfSub[types]=data
                
                company_symbols.append(company_symbol)
                company_names.append(company_name)
                categories.append(category)
            else:
                if key_nums>0:
                    column=[data]*key_nums
                    dfSub[types]=column
        dfMain = pd.concat([dfMain, dfSub], ignore_index=True)
    dfMain.insert(0, 'Company', company_symbols)
    dfMain.insert(1,"Category",categories)
    dataframe_options["Analyst_Estimate_Data"]=pd.concat([dataframe_options["Analyst_Estimate_Data"],dfMain],ignore_index=True)
    return dfMain
    pass
async def processRealTimeTrades(company_name, category,company_symbol,data,metadata):
    # data = json.loads(open(file_path).read())
    company_symbols = []
    company_names = []
    categories = []
    type_ = []
    times=[]
    dfMain=pd.DataFrame()
    subtype = []
    for company, info in data.items():
        if type(info)==dict:
            for t, vals in info.items():
                for val in vals:
                    # print(val)
                    company_symbols.append(company)
                    type_.append(t)
                    subtype.append("Guru Trades")
                    # company_names.append(company_name)
                    categories.append(category)
                    times.append(datetime.now().strftime("%Y-%m"))
                    df = pd.DataFrame(val, index=[0])
                    dfMain = pd.concat([dfMain, df], ignore_index=True)
        if type(info)==list:
            for val in info:
                    # print(val)
                    company_symbols.append(company)
                    subtype.append("Insider Trades")
                    type_.append(None)
                    # company_names.append(company_name)
                    categories.append(category)
                    times.append(datetime.now().strftime("%Y-%m"))
                    df = pd.DataFrame(val, index=[0])
                    dfMain = pd.concat([dfMain, df], ignore_index=True)
    # print(dfMain)
    dfMain.insert(0, 'Company', company_symbols)
    dfMain.insert(1, 'Type', type_)
    dfMain.insert(2,"time",times)
    dfMain.insert(2,"category",categories)
    dfMain.insert(3,"trade_Tyoe",subtype)
    dataframe_options["Real_Time_Trades"]=pd.concat([dataframe_options["Real_Time_Trades"],dfMain],ignore_index=True)
    return dfMain

async def processHistoricalOwnershipData(company_name, category, company_symbol, data,metadata):
    df = pd.DataFrame(columns=[ "Company Symbol", "Category", "Data Element", "Timeframe", "Value"])
    for key, value in data.items():
        df = pd.concat([df, pd.DataFrame([{
                    # "Company Name": company_name,
                    "Company Symbol": company_symbol,
                    "Category": category,
                    "Data Element": key,
                    "Timeframe": datetime.now().strftime("%Y-%m"),
                    "Value": value
                }])],ignore_index=True)
    dataframe_options["Company_General_Data"]=pd.concat([dataframe_options["Company_General_Data"],df],ignore_index=True)
    return df

async def processDividendHistoryData(company_name, category, company_symbol, data,metadata):
    df = pd.DataFrame(data)

    # Rename columns
    df = df.rename(columns={'amount': 'amount', 'ex_date': 'ex_date', 'record_date': 'record_date', 'pay_date': 'pay_date', 'type': 'type', 'currency': 'currency'})

    # Insert company_name column
    df.insert(0, 'Company_Name', company_name)
    df.insert(1, 'Category', category)
    df.insert(2, 'Company_Symbol',company_symbol)
    dataframe_options["Dividend_History_Data"]=pd.concat([dataframe_options["Dividend_History_Data"],df],ignore_index=True)
    return df


async def processFinancialData(company_name, category, company_symbol, data,metadata):
    print(data)
    if "financials" in data:
        # print("here")
        if "financial_template_parameters" in data["financials"]:
            await generalDataParser(company_name, category, company_symbol, data["financials"]["financial_template_parameters"],"financials>>financial_template_parameters")
        if "annuals" in data["financials"]:
            
            # print("here")
            data=data["financials"]["annuals"]
    # print(data)
    df = pd.DataFrame(data['Fiscal Year'], columns=['Fiscal Year'])

    # Add the Preliminary column to the dataframe
    df['Preliminary'] = data['Preliminary']

    # Add columns for each key in the per_share_data_array dict
    for key, value in data['per_share_data_array'].items():
        df[key] = value

    df.insert(0, 'Company_Name', company_name)
    df.insert(1, 'Category', category)
    df.insert(2, 'Company_Symbol',company_symbol)
    dataframe_options["Company_Financial_Data"]=pd.concat([dataframe_options["Company_Financial_Data"],df],ignore_index=True)
    return df
    # pass
    
    
    
async def processRatioData(company_name, category, company_symbol, ratio_data,metadata):
    df = pd.DataFrame(columns=[ "Company Symbol", "Category", "Data Element", "Timeframe", "Value"])
    rows = []

    for sub_ratio_type, sub_ratio_data in ratio_data.items():
                # Append the data to the list
                rows.append([ company_symbol,category, sub_ratio_type,
                            sub_ratio_data.get("indu", {}).get("global_rank", None),
                            sub_ratio_data.get("indu", {}).get("indu_med", None),
                            sub_ratio_data.get("indu", {}).get("indu_tot", None),
                            sub_ratio_data.get("value", None),
                            sub_ratio_data.get("status", None),
                            sub_ratio_data.get("his", {}).get("low", None),
                            sub_ratio_data.get("his", {}).get("high", None),
                            sub_ratio_data.get("his", {}).get("med", None)])

        # Create a DataFrame from the list of data
    df = pd.DataFrame(rows, columns=[ "Company Symbol", "Category","Ratio Type", "Indu Global Rank", "Indu Med", "Indu Tot", "Value", "Status", "His Low", "His High", "His Med"])
    dataframe_options["Company_Ratio_Data"]=pd.concat([dataframe_options["Company_Ratio_Data"],df],ignore_index=True)
    # df.to_excel(f"Company_Ratio_Data.xlsx", index=False)
    return df    



async def generalDataParser(company_name, category, company_symbol, data, parent_path):
    # print(f"{datetime.now()} : Processing {category} for {company_symbol} ")
    if "summary" in data:
        if "ratio" in data["summary"]:
            # print(data["summary"]["ratio"]) /
            await processRatioData(company_name,company_symbol,category,data["summary"]["ratio"],"")
            data["summary"].pop("ratio", None)
    df = pd.DataFrame(columns=[ "Company Symbol", "Category", "Data Element", "Timeframe", "Value"])
    tasks = []
    if type(data) is list:
        for i, item in enumerate(data):
                if type(item) is dict:
                    list_path = parent_path + ".list_{}".format(i)
                    tasks.append(asyncio.create_task(generalDataParser(company_name, category, company_symbol, item, list_path)))
    elif type(data) is dict:
        for key, value in data.items():
            current_path = parent_path + ">>" + key if parent_path else key
            if type(value) is dict:
                tasks.append(asyncio.create_task(generalDataParser(company_name, category, company_symbol, value, current_path)))
            elif type(value) is list:
                if len(value)>0:
                    if type(value[0]) is list:
                        for i, item in enumerate(value):
                            list_path = current_path + ".list_{}".format(i)
                            if type(item) is dict:
                                tasks.append(asyncio.create_task(generalDataParser(company_name, category, company_symbol, item, list_path)))
                    else:
                        
                        df = pd.concat([df, pd.DataFrame([{
                    # "Company Name": company_name,
                    "Company Symbol": company_symbol,
                    "Category": category,
                    "Data Element": current_path,
                    "Timeframe": datetime.now().strftime("%Y-%m"),
                    "Value": value
                }])],ignore_index=True)
                else:
                        df = pd.concat([df, pd.DataFrame([{
                    # "Company Name": company_name,
                    "Company Symbol": company_symbol,
                    "Category": category,
                    "Data Element": current_path,
                    "Timeframe": datetime.now().strftime("%Y-%m"),
                    "Value": value
                }])],ignore_index=True)
            else:
                df = pd.concat([df, pd.DataFrame([{
                    # "Company Name": company_name,
                    "Company Symbol": company_symbol,
                    "Category": category,
                    "Data Element": current_path,
                    "Timeframe": datetime.now().strftime("%Y-%m"),
                    "Value": value
                }])],ignore_index=True)
    else:
        print(f"Invalid response recieved from {category} for {company_symbol}. Data of type{type(data)}")
        print (f">>>> \n {data}")
    if tasks:
        results = await asyncio.gather(*tasks)
        for result in results:
            df = pd.concat([df, result],ignore_index=True)
    dataframe_options["Company_General_Data"]=pd.concat([dataframe_options["Company_General_Data"],df],ignore_index=True)

    return df




# z=asyncio.run(start2())



parser_options = {
        "Stock Summary Data":generalDataParser ,
        # "Company_Ratio_Data": pd.DataFrame(),
        "Company Financial Data": processFinancialData,
        "Company Key Statistics Data":generalDataParser,
        "Company Current Quote Data": generalDataParser,
        "Stock Historical Price": processStockHistoricalPriceData,
        "Historical Ownership Data":processHistoricalOwnershipData,
        "Real-time Guru Trades": processRealTimeTrades,
        "Real-Time Insider Trades": processRealTimeTrades,
        "Dividend History Data": processDividentHistoryData,
        "Analyst Estimate Data": processAnalystEstimateData,
        "Operating Data":generalDataParser,
        "Segments Data": generalDataParser
    }