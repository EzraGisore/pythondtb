from main import Student

try:
    student_name = input("Enter name \n")
    student_age = input("Enter age \n")
    student_id_num = input("Enter ID number \n")
    student_stream = input("Enter stream \n")
    student_gender = input("Enter gender \n")

    Student.create(name=student_name, age=student_age, id_num=student_id_num, stream=student_stream, gender=student_gender)
    print("Student created successfully.")
except:
    print("Failed to create student. Try a different ID number.")
