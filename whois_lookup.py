# Gathering Whois information
import whois

def get_whois(domain):
    try:
        data = whois.whois(domain)
        return data
    except Exception as err:
        print(f"Error : {err}")
        return None
