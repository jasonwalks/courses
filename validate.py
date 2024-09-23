import re

email = input("What's your email? ").strip()

#if re.search(r"^.+@.+\.edu$", email):
#if re.search(r"^[^@]+@[^@]+\.edu$", email):
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
if re.search(r"^\w+@\w+\.(com|gov|org|edu)$", email):
    print("Valid")
else:
    print("Invalid")

'''
..* == .+
username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
'''
