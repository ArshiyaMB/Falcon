import DNS_lookup as dnslookup
import whois_lookup as whois
import DNS_records as dr
import ipaddress
import ssl_lookup as ssl


def main():
    # Input authentication
    targ = input("Enter the targ name or IP address : ")
    try:
        ip = ipaddress.ip_address(targ)
        targ = dnslookup.get_domain(ip)
    # Domain Ip address
    except ValueError:
        ip = dnslookup.get_ip(targ)
        if ip is None:
            print("Domain does not exist")
            raise SystemExit(1)

    print(f"\nTarget : {targ}")
    print(f"\nIP : {ip}")



    print("\n\tWhois Information")
    print('='*70)
    whois_data = whois.get_whois(targ)
    if whois_data:
        print(f"Registrar \t:\t{whois_data.registrar}")
        print(f"Created\t:\t{whois_data.creation_date}")
        print(f"Expire \t:\t{whois_data.expiration_date}")
    else:
        print("Whois data not found")

    # SSL Certification 
    ssl_data = ssl.get_ssl_info(targ)
    print("\n\tSSL Information 🔐")
    print("="*70)
    if ssl_data:
        for key, value in ssl_data.items():
            print(f"{key:<15}:\t{value}")
    else:
        print("SSL data not found")


    # DNS Records A / MX / NS / TXT
    print("\n\tDNS Records 📝")
    print("="*70)
    print(f"\nA \t: \t{dr.get_a_record(targ)}")
    print(f"MX \t: \t{dr.get_mx_record(targ)}")
    print(f"NS \t: \t{dr.get_ns_record(targ)}")
    print(f"TXT \t: \t{dr.get_txt_record(targ)}")




if __name__ == "__main__":
    main()
