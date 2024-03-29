import boto3

def check_aws_resources(domain):
    try:
        client = boto3.client('route53', region_name='us-east-1')
        response = client.list_hosted_zones_by_name(DNSName=domain)
        hosted_zones = response.get('HostedZones', [])
        return len(hosted_zones) > 0
    except Exception as e:
        print("An error occurred while checking AWS resources:", e)
        return False
