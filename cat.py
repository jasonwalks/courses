def main():
    number = get_number()
    mewo(number)

def get_number():
    while True:
        n = int(input("Number of mewo? "))
        if n > 0: 
            return n
    
def mewo(n):
     for _ in range(n):
         print("meow")
        
main()     
'''
i = 0
while i < 3:
    print("meow")
    i += 1 # shorthand for i = i + 1
    
For loop solution
for _ in range(3):
    print("mewo")
 
One-line solution   
print("meow\n" * 3, end="")

Infinite loop solution:
White True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
'''