from dns import resolver

def get_a_record(domain):
    try:
        answers = resolver.resolve(domain,'A')
        return [answer.to_text() for answer in answers]
    except Exception as err:
        return "Not Available⛔"
def get_mx_record(domain):
    try:
        answers = resolver.resolve(domain, 'MX')
        return [answer.to_text() for answer in answers]
    except Exception as err:
        return "Not Available⛔"

def get_ns_record(domain):
    try:
        answers = resolver.resolve(domain, 'NS')
        return [answer.to_text() for answer in answers]
    except Exception as err:
        return "Not Available⛔"
def get_txt_record(domain):
    try:
        answers = resolver.resolve(domain, "TXT")
        return [answer.to_text() for answer in answers]
    except Exception as err:
        return "Not Available⛔"
    

# Test 
# domain = "google.com"
# for record_type in ['A','NS','MX','TXT']:
#     try:
#         answers = resolver.resolve(domain, record_type)
#         print(f"{record_type} : OK ✅")
#     except Exception as err:
#         print(f"{record_type} ❌: {err}")
