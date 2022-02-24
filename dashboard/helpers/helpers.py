import re

def server_abbr(name: str):
    words = re.split(" |-|_|'", name)
    abbr = ""
    for word in words:
        if word.isalnum():
            abbr += word[0]
    return abbr
