print("Welcome to the tip calculator")
total_bill = float(input("what was the total bill"))
tip = int(input("what percentage tip would you like to give?"))
people_split = int(input("how many people to split the bill?"))

bill_with_tip=tip/100*total_bill+total_bill

print(bill_with_tip)

