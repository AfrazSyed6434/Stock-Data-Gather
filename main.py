import asyncio
import requests
import os
import pandas as pd
from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from utils import *
from API_Requests import *
from parsers import *
# Create a list of companies
companies = []

async def get_company_data(company,data_options_selected):
    print(f"{datetime.now()} : Started gathering data for {company} ")
    df = pd.DataFrame(columns=["Company Name", "Company Symbol", "Category", "Data Element", "Timeframe", "Value"])
    tasks = []
    for key,value in data_options_selected.items():
        if value==True:
            parserFunctionName=parser_options[key]
            endpointFunctionName =endpoints_map[key]
            tasks.append(parserFunctionName("",key,company,endpointFunctionName(company),""))

    company_data = await asyncio.gather(*tasks)
    
    return company_data



def main():
    root = Tk()
    root.title("Company Data Extractor")
    root.geometry("500x400")
    root.configure(bg='#f0f0f0')

    # Create the text form for the company names
    label = Label(root, text="Enter comma separated company names:",font=("Helvetica", 12),bg='#f0f0f0')
    label.pack()
    entry = Entry(root, width=50)
    entry.pack()
    data_options = {
        "Stock Summary Data": BooleanVar(),
        "Company Financial Data": BooleanVar(),
        "Company Key Statistics Data": BooleanVar(),
        "Company Current Quote Data": BooleanVar(),
        "Stock Historical Price": BooleanVar(),
        "Historical Ownership Data": BooleanVar(),
        "Real-time Guru Trades": BooleanVar(),
        "Real-Time Insider Trades": BooleanVar(),
        "Dividend History Data": BooleanVar(),
        "Analyst Estimate Data": BooleanVar(),
        "Operating Data": BooleanVar(),
        "Segments Data": BooleanVar()
    }
    
    for option, var in data_options.items():
        var.set(True)
        checkbox = ttk.Checkbutton(root, text=option, variable=var)
        checkbox.pack()
        if option == "Stock Historical Price":
            all_data = BooleanVar()
            all_data.set(True)
            # xt=ttk.Style().configure()
            all_data_checkbox = ttk.Checkbutton(root, text="       -Collect all data", variable=all_data)
            all_data_checkbox.pack()
            last_week_data = BooleanVar()
            last_week_data.set(False)
            last_week_data_checkbox = ttk.Checkbutton(root, text="      -Collect Last Week Data", variable=last_week_data)
            last_week_data_checkbox.pack()
    

    async def startProcessing(data_options_selected):
        df = pd.DataFrame(columns=["Company Name", "Company Symbol", "Category", "Data Element", "Timeframe", "Value"])
        tasks = [get_company_data(c,data_options_selected) for c in companies]
        company_data = await asyncio.gather(*tasks)
        for dataType,dataFrame in dataframe_options.items():
            if len(dataFrame)>0:
                date = datetime.now().strftime("%Y-%m-%d---%H:%M")
                if not os.path.exists(date):
                    os.makedirs(date)
                current_time=datetime.now()
                dataFrame.to_excel(f"{date}/{dataType}_{current_time}.xlsx", index=False)
        # for data in company_data:
        #     df = pd.concat([df, data],ignore_index=True)

        # # Save DataFrame to Excel
        # current_time=datetime.now()
        # df.to_excel(f"company_data_{current_time}.xlsx", index=False)
        messagebox.showinfo("Info", f"Data saved to company_data_{current_time}.xlsx")
        root.destroy()



    def submit():
        global companies
        companies = entry.get().split(',')
        label.configure(text="Loading...",foreground="black")
        data_options_selected = {k: v.get() for k, v in data_options.items()}

        asyncio.run(startProcessing(data_options_selected))
    # Create the submit button
    submit_button = ttk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=10)

    root.mainloop()




if __name__ == "__main__":
    main()