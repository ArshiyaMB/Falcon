import DNS_lookup as dnslookup
import whois_lookup as whois
import DNS_records as dr
import ipaddress
import ssl_lookup as ssl


def main():
    # Input authentication
    targ = input("Enter the domain name or IP address : ")
    try:
        ip = ipaddress.ip_address(domain)
        domain = dnslookup.get_domain(ip)
        if domain is None:
            print("IP does not match to any domain")
            raise SystemExit(1)
    # Domain Ip address
    except ValueError:
        ip = dnslookup.get_ip(domain)
        if ip is None:
            print("Domain does not exist")
            raise SystemExit(1)

    print(f"\ndomainet : {domain}")
    print(f"\nIP : {ip}")



    print("\n\tWhois Information")
    print('='*70)
    whois_data = whois.get_whois(domain)
    if whois_data:
        print(f"Registrar \t:\t{whois_data.registrar}")
        print(f"Created\t:\t{whois_data.creation_date}")
        print(f"Expire \t:\t{whois_data.expiration_date}")
    else:
        print("Whois data not found")

    # SSL Certification 
    print("\n\tSSL Information 🔐")
    print("="*70)
    ssl_data = ssl.get_ssl_info(domain)
    if ssl_data:
        for key, value in ssl_data.items():
            print(f"{key:<15}:\t{value}")
    else:
        print("SSL data not found")


    # DNS Records A / MX / NS / TXT
    print("\n\tDNS Records 📝")
    print("="*70)
    for record_type in ['A', 'MX', 'NS', 'TXT']:
        print(f"{record_type} \t:\t{dr.get_records(domain, record_type)}")



if __name__ == "__main__":
    main()
