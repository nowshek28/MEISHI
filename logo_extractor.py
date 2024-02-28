import requests
from bs4 import BeautifulSoup
import csv
import os

def download_logo(url, company_name):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Adjust the file path as needed
        file_path = os.path.join("logo_folder", f"{company_name}_logo.png")
        
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Logo for {company_name} downloaded successfully.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading logo for {company_name}: {e}")

def scrape_company_logos():
    # Example list of companies and their websites
    companies = [
        #{"name": "Toyota", "website": "https://www.toyota.com"},
        {"name": "Toyota", "website": "https://www.toyota.co.uk/"},
        # Add more companies as needed
    ]

    for company in companies:
        try:
            response = requests.get(company["website"])
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the logo element
            logo_element = soup.find('img', {'class': 'logos'})

            # Check if the logo element is found and has a 'src' attribute
            if logo_element and 'src' in logo_element.attrs:
                logo_url = logo_element['src']
                logo_url = 'https://cdn.cookielaw.org/logos/065366f9-7c51-4d6b-9709-f69f5578e81b/08ee3b27-ef72-4488-8ea8-b6594ec73408/bfb9fa73-26fd-46ea-9c56-ac3b938b1aec/toyota_logo.png'
            
             # Download the logo
                download_logo(logo_url, company["name"])
            else:
                print(f"No logo found for {company['name']}")

        except requests.exceptions.RequestException as e:
            print(f"Error scraping data for {company['name']}: {e}")

def main():
    # Create a folder to store logos
    if not os.path.exists("logo_folder"):
        os.makedirs("logo_folder")

    # Scraping company logos
    scrape_company_logos()

if __name__ == "__main__":
    main()