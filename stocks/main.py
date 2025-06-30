import json
from stock_info import get_company_details_by_ticker
from CompanyInfo import CompanyInfo

# Configuration
api_key = "YOUR_API_KEY"  # Replace with your actual Alpha Vantage API key
ticker = "AAPL"  # Example ticker (Apple Inc.)

def remove_numbered_keys(data):
    """Removes numbers and dots from dictionary keys."""
    if isinstance(data, dict):
        return {key.split(". ")[1]: value for key, value in data.items()}
    return data  # Return as is if not a dictionary

try:
    # Get the company details (full match data)
    company_details = get_company_details_by_ticker(ticker, api_key)
    #print('Company Detail...' , company_details)
    
    if isinstance(company_details, dict):
        # Clean the keys
        cleaned_details = remove_numbered_keys(company_details)

        # Create the model instance
        company = CompanyInfo(
            symbol=cleaned_details["symbol"],
            name=cleaned_details["name"]
        )

        # Print the model object
        print("Company Details Model Object:\n", company)

        # Optionally, print as JSON
        print("\nCompany Details as JSON:\n", json.dumps(company.to_dict(), indent=4))
    else:
        print(f"Error: {company_details}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
