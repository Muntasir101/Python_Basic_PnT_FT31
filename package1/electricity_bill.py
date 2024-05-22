electricity_used = int(input("Enter electricity used : "))

if electricity_used <= 0:
    print("Invalid Electricity Unit")

else:
    if electricity_used <= 100:
        total_bill = electricity_used * 0.12
        print("Your total bill is: $", total_bill)
    elif electricity_used <= 300:
        total_bill = electricity_used * 0.15
        print("Your total bill is: $", total_bill)
    elif electricity_used >= 500:
        total_bill = electricity_used * 0.20
        print("Your total bill is: $", total_bill)
