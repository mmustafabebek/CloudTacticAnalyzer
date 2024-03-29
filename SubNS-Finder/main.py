import subdomain_finder
import ns_checker
import aws_checker

def main(domain):
    subdomains = subdomain_finder.find_subdomains(domain)
    ns_records = ns_checker.check_ns_records(domain)
    aws_resources = aws_checker.check_aws_resources(domain)

    if subdomains:
        print("Subdomains found:")
        for subdomain in subdomains:
            print(subdomain)

    if ns_records:
        print("NS Records found:")
        for ns_record in ns_records:
            print(ns_record)

    if aws_resources:
        print("AWS Resources found.")
    else:
        print("No AWS Resources found.")

if __name__ == "__main__":
    domain = input("Enter the domain to scan: ")
    main(domain)
