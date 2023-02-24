from main import Teacher

teachers= Teacher.select()
for teacher in teachers:
    print(teacher.name, teacher.id_num)