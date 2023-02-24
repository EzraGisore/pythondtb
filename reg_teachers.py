from main import Teacher

try:
    teacher_name= input("Enter name \n")
    teacher_id_num= input("Enter ID number \n")

    Teacher.create(name=teacher_name,id_num=teacher_id_num)
    print("Teacher account created successfully.")
except:
    print("failed to create account. Try a different ID NUmber.")