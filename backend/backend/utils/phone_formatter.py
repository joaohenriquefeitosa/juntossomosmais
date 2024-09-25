import re

def format_phone_number(phone):
    return '+55' + re.sub(r'\D', '', phone)