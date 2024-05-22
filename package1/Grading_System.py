"""
Grade System :
 1 - 40  = F
 41 - 50 = D
 51 - 60 = C
 61 - 70 = A-
 71 - 80 = A
 81- 100 = A+

input: 30
Output: Grade F
"""
# Static variables
# Student_mark = 10

# dynamic variables
Student_mark = int(input("Enter Student Mark: "))

if Student_mark <= 0:
    print("Invalid marks")

else:
    if Student_mark <= 40:
        print("Grade F")
    elif Student_mark <= 50:
        print("Grade D")
    elif Student_mark <= 60:
        print("Grade C")
    elif Student_mark <= 70:
        print("Grade A-")
    elif Student_mark <= 80:
        print("Grade A")
    elif Student_mark <= 100:
        print("Grade A+")


