import re
from utils.regex_patterns import EMAIL_REGEX, USERNAME_REGEX, HASH_REGEX

def extract_data(text):
    emails = re.findall(EMAIL_REGEX, text)
    usernames = re.findall(USERNAME_REGEX, text)
    hashes = re.findall(HASH_REGEX, text)

    return {
        "emails": list(set(emails)),
        "usernames": list(set(usernames)),
        "hashes": list(set(hashes))
    }