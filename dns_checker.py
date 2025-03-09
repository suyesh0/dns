import dns.resolver
import sys

def check_dns_a_records(domain):
    """Checks for A records with TTL for a single domain."""
    resolver = dns.resolver.Resolver()

    try:
        answers = resolver.resolve(domain, 'A')
        print(f"A records for {domain}:")
        for rdata in answers:
            print(f"  IP: {rdata.address}, TTL: {answers.ttl}")
    except dns.resolver.NoAnswer:
        print(f"No A records found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
    except dns.resolver.Timeout:
        print(f"DNS query for {domain} timed out.")
    except Exception as e:
        print(f"An error occurred for {domain}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dns_checker.py domain")
        sys.exit(1)

    domain = sys.argv[1]
    check_dns_a_records(domain)
