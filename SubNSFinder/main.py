import subdomain_finder
import ns_checker

def main():
    domain = input("Enter the domain to scan: ")

    # Step 1: Find subdomains
    print("Finding subdomains...")
    subdomains = subdomain_finder.find_subdomains(domain)

    # Print subdomains found
    print("Subdomains found:")
    for subdomain in subdomains:
        print(subdomain)

    # Step 2: Check NS records for AWS resources
    print("Checking NS records for AWS resources...")
    aws_resources = ns_checker.check_ns_records(subdomains)

    # Step 3: Output results
    if aws_resources:
        print("You have potential resources focused on AWS, pay attention to them and review them!")
        print("AWS Resources found:")
        for resource in aws_resources:
            print(resource)
    else:
        print("No AWS-focused resources.")

if __name__ == "__main__":
    main()
