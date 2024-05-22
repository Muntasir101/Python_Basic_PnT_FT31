student_1_name = 'smith'
student_2_name = "John"
student_3_name = 'kevin'
student_4_name = 'david'

student_names = ['smith', 'John', 'kevin', 'david']

student_count = len(student_names)
print(student_count)  # 4

print(student_names[0])  # smith

for student in student_names:
    print(student)

# list append
student_names.append("Superman")

print(student_names)  # ['smith', 'John', 'kevin', 'david', 'Superman']

# Superman Dropout
student_names.remove("Superman")
print(student_names)  # ['smith', 'John', 'kevin', 'david']
