from main import Student

students= Student.select()
for student in students:
    print(student.name, student.id_num, student.gender, student.stream, student.age)