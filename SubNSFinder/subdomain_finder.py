import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def find_subdomains(domain):
    subdomains = []
    # Get the date 6 days before the current date
    date = datetime.now().strftime('%Y-%m-%d')
    url = f"https://subdomainfinder.c99.nl/scans/{date}/{domain}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', class_='domain')
            for link in links:
                subdomains.append(link.text.strip())
        else:
            print(f"Failed to fetch subdomains for {domain}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching subdomains for {domain}: {e}")

    return subdomains
