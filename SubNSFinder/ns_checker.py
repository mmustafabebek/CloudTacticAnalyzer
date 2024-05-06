import requests
from bs4 import BeautifulSoup
import socket

def check_ns_records(domains):
    aws_domains = []

    for domain in domains:
        try:
            ip_address = socket.gethostbyname(domain)
            response = requests.get(f"https://who.is/whois-ip/{ip_address}")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                if "Amazon" in soup.get_text() or "AWS" in soup.get_text():
                    aws_domains.append(domain)
            else:
                print(f"Failed to fetch WHOIS information for {domain}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error fetching WHOIS information for {domain}: {e}")

    return aws_domains
