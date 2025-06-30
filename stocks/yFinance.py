import re
import os
import yfinance as yf
import pandas as pd

# Print the directory from where the script is running
print(os.getcwd())

# Define the file path
file_path = "/Users/dtsreddy/Documents/Sanjeev/MyPython/stocks/stocks.txt"

# Ensure the file exists
if not os.path.exists(file_path):
    print(f"The file {file_path} does not exist. Please ensure it is created.")
else:
    # Read and process the file
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Extract all tickers using regex
        tickers = re.findall(r"\$(\w+)", content)  # Captures words prefixed with $

        # Print length of tickers
        print('Total Tickers count: ', len(tickers))

        # Prepare a list to store the details
        data = []

        # Loop through each ticker
        for ticker in tickers:
            try:
                stock = yf.Ticker(ticker)
                stock_info = stock.info

                # Check if stock_info is available and contains expected data
                if stock_info:
                    # Clean the keys by removing any leading numbers and dots
                    cleaned_info = {key.split(".")[-1].strip(): value for key, value in stock_info.items()}

                    # Extract specific fields
                    data.append({
                        "Symbol": cleaned_info.get("symbol"),
                        "Long Name": cleaned_info.get("longName", "N/A")  # Default to "N/A" if longName is not found
                    })
                else:
                    print(f"Warning: No data found for ticker {ticker}")

            except Exception as e:
                print(f"Error processing ticker {ticker}: {str(e)}")

        # Create a pandas DataFrame
        df = pd.DataFrame(data)

        # Print the data in a tab-separated format for easy pasting into Excel
        # print("\nSymbol\tLong Name")
        # for row in data:
        #     print(f"{row['Symbol']}\t{row['Long Name']}")
        
        print("\nSymbol")
        for row in data:
            print(f"{row['Symbol']}")

        # print("\Long Name")
        # for row in data:
        #     print(f"{row['Long Name']}")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
