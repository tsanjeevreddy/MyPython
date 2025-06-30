import requests
import json

# Function to get company details using stock ticker
def get_company_details_by_ticker(ticker, api_key):
    # Alpha Vantage API URL for SYMBOL_SEARCH
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ticker}&apikey={api_key}"

    # Make the GET request to Alpha Vantage API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Print the full JSON response for logging purposes
        print("Full API Response:")
        print(json.dumps(data, indent=4))  # Pretty-print the JSON data

        # Check if any matches were found
        if 'bestMatches' in data and len(data['bestMatches']) > 0:
            # Iterate over all matches in bestMatches
            for match in data['bestMatches']:
                # Extract relevant fields for each match
                company_symbol = match.get('1. symbol', '').strip()
                company_name = match.get('2. name', '').strip()
                type = match.get('3. type', '').strip()
                currency = match.get('8. currency', '').strip()
                region = match.get('4. region', '').strip()

                # Check if the region is United States, currency is USD, and the symbol matches the ticker
                if region == "United States" and currency == "USD" and company_symbol == ticker and type == "Equity":
                    # Return the full match data (as a dictionary)
                    return match  # This is the full match data from the API response

            # If no valid match is found
            return f"No valid U.S. stock found for ticker {ticker}. The region should be 'United States' and currency 'USD'."
        else:
            return f"No matching company found for ticker {ticker}."
    else:
        return f"Error: {response.status_code}, unable to fetch data."
