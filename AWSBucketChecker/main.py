import concurrent.futures
import time
from colorama import Fore, Style
from restricts import aws_is_valid_bucket_name
from aws_urls import check_aws_urls
from aws_regions import REGIONS

# Maximum number of concurrent connections
CONNECTIONS = 100
# Timeout duration (in seconds) for checking web pages
TIMEOUT = 5

# Function to obtain user input
def get_user_input():
    name = input("Enter an AWS S3 bucket name to check for accessibility: ").strip()

    # Check if the provided name is valid for AWS
    is_aws_valid = aws_is_valid_bucket_name(name)

    if is_aws_valid:
        return name
    else:
        print(Fore.RED + "Invalid input. Please enter a valid name for an AWS S3 bucket." + Style.RESET_ALL)
        exit(1)

# Function to fetch web pages in parallel
def fetch_web_pages(name, timeout):
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        time1 = time.time()
        aws_accessible, aws_inaccessible = check_aws_urls(name, REGIONS, timeout)
        time2 = time.time()

    print(Fore.BLUE + 'AWS Accessible URLs:' + Style.RESET_ALL)
    for url in aws_accessible:
        print(f'   {url}')

    print(Fore.BLUE + 'AWS Inaccessible URLs:' + Style.RESET_ALL)
    for url in aws_inaccessible:
        print(f'   {url}')

    return time2 - time1

# Main program
if __name__ == '__main__':
    name = get_user_input()
    if name:
        total_time = fetch_web_pages(name, TIMEOUT)
        print(f'Total time: {total_time:.2f} s')
