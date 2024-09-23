import re

locations = {
  "+1": "United States and Canada",
  "+62": "Indonesia",
  "+505": "Nicaragua"
}

def main():
  pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
  number = input("Number: ")

  if match := re.search(pattern, number):
    print(f"Country: {locations[match.group(1)]}")
  else: 
    print("Invalid")

main()
