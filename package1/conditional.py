"""
if
elif
else
"""
student1_mark = -0
student2_mark = 20

if student1_mark <= 0 or student2_mark <= 0:
    print("Invalid marks")
else:
    if student1_mark == student2_mark:
        print("Student 1 and Student 2 getting same marks")
    elif student1_mark < student2_mark:
        print("Student 1 getting less marks")
    elif student1_mark > student2_mark:
        print("Student 1 getting more marks")
    elif student1_mark != student2_mark:
        print("Student 1 and Student 2 have different marks")
