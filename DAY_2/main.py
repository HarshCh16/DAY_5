print("WELCOME TO THE TIP CALCULATOR!")
total_bill = input("\nWhat was the total bill? $")
tip_percent = input("\nHow much tip would you like to give? 10, 12 or 15? ")
no_of_people = input("\nHow many people to split the bill? ")
tip = (float(tip_percent) / 100) * float(total_bill)
total_amount = float(total_bill) + tip
share_per_person = total_amount / float(no_of_people)
rounded_off_amount = round(share_per_person , 2)
print(f"\nEach person should pay ${rounded_off_amount}.")