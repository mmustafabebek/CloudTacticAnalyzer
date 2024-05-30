import dns

def check_dns_records(subdomains):
    aws_domains = []

    for subdomain in subdomains:
        try:
            answers = dns.resolver.resolve(subdomain, 'TXT')
            for rdata in answers:
                txt_data = rdata.to_text()
                if any(word in txt_data for word in ["Amazon", "AWS", "S3", "Elastic Beanstalk"]):
                    aws_domains.append(subdomain)
                    break
        except Exception as e:
            print(f"Error fetching DNS information for {subdomain}: {e}")

    return aws_domains
