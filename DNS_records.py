from dns import resolver

def get_records(domain, record_type):
    try:
        answers = resolver.resolve(domain, record_type)
        return [answer.to_text() for answer in answers]
    except Exception as err:
        return f"{record_type}Record Not Available⛔"
