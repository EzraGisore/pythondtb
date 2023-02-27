from main import People

try:
    person_name = input("Enter your name \n")
    person_phonenumber = input("Enter your phone number \n")
    person_email = input("Enter your email \n")
    person_county = input("Enter your county \n")
    person_gender = input("Enter your gender \n")
    person_religion = input("Enter your religion \n")
    person_password = input("Enter your password \n")

    People.create(name = person_name, phonenumber = person_phonenumber, email = person_email, county = person_county, gender = person_gender, religion = person_religion, password = person_password )
    print("Person's account created successfully.")
except:
    print("Failed to create account!")