'''
def main():
    yell("This is CS50P")

def yell(phrase):
    print(phrase.upper())

if __name__ == "__main__":
    main()
'''
'''
def main():
    yell(["This", "is", "CS50P"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()   
'''
'''
def main():
    yell("This", "is", "CS50P")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()   
'''
'''
def main():
    yell("This", "is", "CS50P")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()   
'''
def main():
    yell("This", "is", "CS50P")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()   