from main import People

people=People.select()
for person in people:
    print(person.name, person.phonenumber, person.email, person.county, person.gender, person.religion, person.password)