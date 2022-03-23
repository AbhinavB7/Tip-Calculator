bill_amount = float(input('What is the total bill?'))
tip_percent = int(input("How much would you like to tip?(5%,10%) "))
total_people = int(input("How many people are splitting the bill? "))

tip_amount = bill_amount * tip_percent/100
bill_with_tip = bill_amount + tip_amount

split_amount = bill_with_tip / total_people

print("Each person has to pay ", split_amount)