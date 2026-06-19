import ipaddress
import DNS_lookup as dnslookup
import whois_lookup as whois
import DNS_records as dr
import ssl_lookup as ssl

# Recive ip or domain as target and start calling process on it
def main():
    # Input authentication
    targ = input("Enter the target name or IP address : ")
    try:
        ip = ipaddress.ip_address(targ)
        targ = dnslookup.get_domain(ip)
        if targ is None:
            print("IP does not match to any targ")
            raise SystemExit(1)
    # targ Ip address
    except ValueError:
        ip = dnslookup.get_ip(targ)
        if ip is None:
            print("Domain does not exist")
            raise SystemExit(1)

    print(f"\ntarg : {targ}")
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
    print("\n\tSSL Information 🔐")
    print("="*70)
    ssl_data = ssl.get_ssl_info(targ)
    if ssl_data:
        for key, value in ssl_data.items():
            print(f"{key:<15}:\t{value}")
    else:
        print("SSL data not found")


    # DNS Records A / MX / NS / TXT
    print("\n\tDNS Records 📝")
    print("="*70)
    for record_type in ['A', 'MX', 'NS', 'TXT']:
        print(f"{record_type} \t:\t{dr.get_records(targ, record_type)}")
        if record_type == 'TXT':
            txt_record = dr.get_records(targ, record_type)
    if txt_record is not None:
        spf = 0
        dmarc = 0
        print("-"*30)
        print("\tEmail Security ✉")
        for record in txt_record:
            if "v=spf1" in record.lower():
                spf +=1
                print("\n\tSPF : found ✅")

            if "v=dmarc1" in record.lower():
                dmarc +=1
                print("\tDMARC : found ✅")

        if spf == 0:
            print("\n\tSPF : not found ❌")
        if dmarc == 0:
            print("\tDMARC : not found ❌")

if __name__ == "__main__":
    main()
