from dns import resolver

def get_records(domain, record_type):
    try:
        answers = resolver.resolve(domain, record_type, timeout= 5)
        return [answer.to_text() for answer in answers]
    except Exception as err:
        return f"{record_type}Record Not Available⛔"

# Test 
# domain = "google.com"
# for record_type in ['A','NS','MX','TXT']:
#     try:
#         answers = resolver.resolve(domain, record_type)
#         print(f"{record_type} : OK ✅")
#     except Exception as err:
#         print(f"{record_type} ❌: {err}")
