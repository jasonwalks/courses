'''
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house
'''
'''
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)
'''
'''
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")
    
def get_student():
#    name = input("Name: ")
#    house = input("House: ")
    return [input("Name: "), input("House: ")]
'''
'''
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")
    
def get_student():
#    student = {}
#    student["name"] = input("Name: ")
#    student["house"] = input("House: ")
    return {"name": input("Name: "), "house": input("House: ")}
'''
'''
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")
    
def get_student():
    return {"name": input("Name: "), "house": input("House: ")}
'''
'''
class Student:
#    def __init__(self, name, house, patronus):
    def __init__(self, name, house):
     #   if not name: # if name == ""
     #       raise ValueError("Missing name") 
     #  if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
     #       raise ValueError("Invalid house")
        self.name = name
        self.house = house
    #    self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
'''
'''    
    def charm(self):
        match self.patronus: 
            case "Stag":
                return "🫎"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🤷‍♂️"
'''


'''
def main():
    student = get_student()
#    print("Expecto Patronum!")
#    print(student.charm())
#    student.house = "Number Four, Privet Drive"
    print(student)
'''
'''
def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student.name 
'''
'''
def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student.name 
'''
'''
def get_student():
 #   name = input("Name: ")
 #   house = input("House: ")
 #   patronus = input("Patronus: ")
 #   return Student(input("Name: "), input("House: "), input("Patronus: "))
     return Student(input("Name: "), input("House: "))
'''
'''
if __name__ == "__main__": 
    main()
'''



class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        return cls(input("Name: "), input("House: "))    

def main():
    student = Student.get()
    print(student)        


if __name__ == "__main__": 
    main()
