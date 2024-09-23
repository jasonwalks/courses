import re

url = input("URL: ").strip()
'''
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
'''
'''
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
'''
'''
if matches := re.search(r"^https?://(WWW\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(2)}")
'''
'''
if matches := re.search(r"^https?://(?:WWW\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
'''
if matches := re.search(r"^https?://(?:WWW\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")