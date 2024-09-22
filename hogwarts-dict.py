'''
students = {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Hermione": "Gryffindor",
    "Draco": "Slytherin", 
}

for student in students:
    print(student, students[student], sep=", ")
'''    

students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
   print(student["name"], student["house"], student["patronus"], sep=", ")