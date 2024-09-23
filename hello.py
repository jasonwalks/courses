'''
# Ask the user for their name
name = input("what's your name? ").strip().title()

# Split the name into first and last name variables with .split()
first, last = name.split(" ")

# Greet the user
print(f"Hello, {first}")
'''

def main():
  name = input("What's your name? ")
  print(hello(name))

def hello(to="world"):
  print(f"Hello, {to}")


if __name__ == "__maim__":
  main()
