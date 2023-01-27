from tkinter import BooleanVar
import requests
import pandas as pd
from datetime import datetime
import json
import asyncio

async def recursive_json_parser(company_name, category, company_symbol, data, parent_path):
    # print(f"{datetime.now()} : Processing {category} for {company_symbol} ")
    df = pd.DataFrame(columns=["Company Name", "Company Symbol", "Category", "Data Element", "Timeframe", "Value"])
    tasks = []
    if type(data) is list:
        for i, item in enumerate(data):
                if type(item) is dict:
                    list_path = parent_path + ".list_{}".format(i)
                    tasks.append(asyncio.create_task(recursive_json_parser(company_name, category, company_symbol, item, list_path)))
    elif type(data) is dict:
        for key, value in data.items():
            current_path = parent_path + ">>" + key if parent_path else key
            if type(value) is dict:
                tasks.append(asyncio.create_task(recursive_json_parser(company_name, category, company_symbol, value, current_path)))
            elif type(value) is list:
                if len(value)>0:
                    if type(value[0]) is list:
                        for i, item in enumerate(value):
                            list_path = current_path + ".list_{}".format(i)
                            if type(item) is dict:
                                tasks.append(asyncio.create_task(recursive_json_parser(company_name, category, company_symbol, item, list_path)))
                    else:
                        
                        df = pd.concat([df, pd.DataFrame([{
                    "Company Name": company_name,
                    "Company Symbol": company_symbol,
                    "Category": category,
                    "Data Element": current_path,
                    "Timeframe": datetime.now().strftime("%Y-%m"),
                    "Value": value
                }])],ignore_index=True)
                else:
                        df = pd.concat([df, pd.DataFrame([{
                    "Company Name": company_name,
                    "Company Symbol": company_symbol,
                    "Category": category,
                    "Data Element": current_path,
                    "Timeframe": datetime.now().strftime("%Y-%m"),
                    "Value": value
                }])],ignore_index=True)
            else:
                df = pd.concat([df, pd.DataFrame([{
                    "Company Name": company_name,
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
    return df

# df=recursive_json_parser("APPlE","Stock Summary Data",company_symbol,response.json(),"")
# df.to_excel(f"company_data_{datetime.now()}.xlsx", index=False)