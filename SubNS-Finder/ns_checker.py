from dns import resolver

def check_ns_records(domain):
    ns_records = set()

    try:
        answers = resolver.resolve(domain, 'NS')
        for rdata in answers:
            ns_records.add(rdata.to_text())
    except Exception as e:
        print("An error occurred while fetching NS records:", e)

    return ns_records
