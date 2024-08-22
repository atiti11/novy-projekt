students = [
    {"jméno": "Jan", "příjmení": "Novák", "věk": 20},
    {"jméno": "Petra", "příjmení": "Svobodová", "věk": 22},
    {"jméno": "Lukáš", "příjmení": "Dvořák", "věk": 19},
    {"jméno": "Eva", "příjmení": "Kučerová", "věk": 21},
    {"jméno": "Tomáš", "příjmení": "Král", "věk": 23},
]

for student in students:
    print("jméno:", student["jméno"], end=", ")
    print("příjmení:", student["příjmení"], end=", ")
    print("věk:", student["věk"])
    print("---------")

print("Konec programu")
