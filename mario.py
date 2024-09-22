def main():
    size = int(input("What's the size of the square? "))
    print_square(size)


def print_square(n):
    for i in range(n):
        print_row(n)
        
def print_row(j):
    print("#" * j)
                      
main()