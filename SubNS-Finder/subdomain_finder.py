import requests
from bs4 import BeautifulSoup
from datetime import datetime

def find_subdomains(domain):
    subdomains = set()

    try:
        today_date = datetime.now().strftime('%Y-%m-%d')
        url = f"https://subdomainfinder.c99.nl/scans/{today_date}/{domain}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a', class_='d-block'):
            href = link.get('href')
            if href and domain in href:
                subdomain = href.split('.')[0]
                subdomains.add(subdomain)
    except Exception as e:
        print("An error occurred while fetching subdomains:", e)

    return subdomains
