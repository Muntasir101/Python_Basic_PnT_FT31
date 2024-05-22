purchase_amount = int(input("Enter Amount: "))

if purchase_amount <= 0:
    print("invalid purchase amount")

else:
    if 100 <= purchase_amount <= 199:
        discount_amount = purchase_amount - purchase_amount * 0.9
        total_amount = purchase_amount - discount_amount
        print("After Discount Total Payable:$", total_amount)
    elif 200 <= purchase_amount <= 499:
        discount_amount = purchase_amount - purchase_amount * 0.8
        total_amount = purchase_amount - discount_amount
        print("After Discount Total Payable:$", total_amount)
    elif purchase_amount >= 500:
        discount_amount = purchase_amount - purchase_amount * 0.7
        total_amount = purchase_amount - discount_amount
        print("After Discount Total Payable:$", total_amount)
