customer_deposit = 1000
converted_customer_deposit = float(customer_deposit)
# print(converted_customer_deposit)

employee_salary = int(input("Your Salary: "))
employee_tax_rate = 10.42 / 100
provident_fund = employee_salary * 20 / 100
tax_amount = employee_salary * employee_tax_rate
net_salary = employee_salary - tax_amount - provident_fund

print("Your Tax Amount is:", tax_amount)
print("Your Provident Fund Contribution is:", provident_fund)
print("Your Net Salary After Tax Deduction and Provident Fund is:", int(net_salary))

