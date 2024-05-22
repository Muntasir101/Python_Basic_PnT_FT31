"""
output:
even_numbers = [2,4,6,8,10]
odd_numbers = [1,3,5,7,9]
"""
numbers = [11, 30, 23, 57, 74, 49, 84, 100, 99]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
    else:
        even_numbers.append(number)

print("Even numbers: ", even_numbers)
print("odd numbers: ", odd_numbers)