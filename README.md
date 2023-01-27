# Stock Data Gather

This repository contains a script that allows you to gather various types of stock data from the GuruFocus API. The script is written in Python and uses the Tkinter library to launch a user interface (UI) that allows you to select which types of data you would like to gather.

## Getting Started

1. Download the repository and navigate to the directory where the files are located.

2. Run the `Setup.bat` file. This will install Python and all the necessary requirements for the script to run.

3. Once the setup is complete, run the `GatherStockData.bat` file. This will launch the UI.

4. The UI contains a text form where you can enter the ticker symbol of the stock you would like to gather data for, and a submit button to initiate the data gathering process.

5. There are also 12 checkboxes that correspond to different types of data that can be gathered. By default, all checkboxes are selected. You can choose to deselect any checkboxes that you do not need.

6. Once you have selected the desired data and entered the ticker symbol, click the submit button to start gathering the data.

7. The script will create a new folder with the current date and time (yyyy-mm-dd--h:m) as the name. This folder will contain 7 csv files:

- `Company_General_Data`: This file contains data from the Stock Summary Data, Historical Ownership Data, Company Key Statistics Data, Company Current Quote Data, Operating Data, and Segment Data endpoints.
- `Company_Ratio_Data`: This file contains a sub-part of the Stock Summary Data endpoint.
- `Company_Financial_Data`: This file contains data from the Company Financial Data endpoint. Note that this endpoint returns historical data and is updated only once every September.
- `Real_Time_Trades`: This file contains data from the Real-time Guru Trades and Real-Time Insider Trades endpoints.
- `Dividend_History_Data`: This file contains data from the Dividend History Data endpoint.
- `Analyst_Estimate_Data`: This file contains data from the Analyst Estimate Data endpoint.
- `Stock_History_Data`: This file contains historical stock data of the company.

8. The `Stock Historical Price` checkbox has two sub-options beneath it: "Get all data" and "Get last week data". These options allows you to choose whether to gather all historical data or just the data from the last week.

## Note

Please note that the use of this script is subject to GuruFocus's terms of use and data policy.
