# Stock Data Gather

This repository contains a script that allows you to gather various types of stock data from the GuruFocus API. The script is written in Python and uses the Tkinter library to launch a user interface (UI) that allows you to select which types of data you would like to gather.

## Getting Started

1. Download the repository as a zip file from the website.

2. Extract the files from the zip archive and navigate to the directory where the files are located.

3. Run the `Setup.bat` file. This will install Python and all the necessary requirements for the script to run.

4. Once the setup is complete, run the `GatherStockData.bat` file. This will launch the UI.

5. The UI contains a text form where you can enter the ticker symbol of the stock you would like to gather data for, and a submit button to initiate the data gathering process.

6. There are also 12 checkboxes that correspond to different types of data that can be gathered. By default, all checkboxes are selected. You can choose to deselect any checkboxes that you do not need.

7. Once you have selected the desired data and entered the ticker symbol, click the submit button to start gathering the data.

8. The script will create a new folder with the current date and time (yyyy-mm-dd--h:m) as the name. This folder will contain 7 csv files:

- `Company_General_Data`: This file contains data from the Stock Summary Data, Historical Ownership Data, Company Key Statistics Data, Company Current Quote Data, Operating Data, and Segment Data endpoints. This file will contain information such as the company's name, ticker symbol, market cap, revenue, and other key financial metrics.
- `Company_Ratio_Data`: This file contains a sub-part of the Stock Summary Data endpoint. This file will contain financial ratios such as the P/E ratio, P/B ratio, and debt-to-equity ratio.
- `Company_Financial_Data`: This file contains data from the Company Financial Data endpoint. This file will contain historical financial statements such as income statements, balance sheets, and cash flow statements. Note that this endpoint returns historical data and is updated only once every September.
- `Real_Time_Trades`: This file contains data from the Real-time Guru Trades and Real-Time Insider Trades endpoints. This file will contain information about recent trades made by gurus and insiders.
- `Dividend_History_Data`: This file contains data from the Dividend History Data endpoint. This file will contain information about the company's dividend history, including the amount and frequency of dividends paid.
- `Analyst_Estimate_Data`: This file contains data from the Analyst Estimate Data endpoint. This file will contain earnings estimates and target prices from analysts covering the stock.
- `Stock_History_Data`: This file contains historical stock data of the company. This file will contain information such as the open, high, low, and close prices of the stock, as well as trading volume.

9. The `Stock Historical Price` checkbox has two sub-options beneath it: "Get all data" and "Get last week data". These options allows you to choose whether to gather all historical data or just the data from the last week.

## Note

Please note that the use of this script is subject to GuruFocus's terms of use and data policy.
