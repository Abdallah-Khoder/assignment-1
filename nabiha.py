salaryMouth = input("Enter your salary of the month : ")
salaryMouth = input("Enter the name of the month : ")
categories = ["Savings" , "Rent" , "Electricity"]
amounts = [] 
for i in range(len(categories)) : 
    amount = input("Enter amount for " + categories[i] + " : ")
    amounts.append(amount)

for i in range(len(amounts)) : 
    print("Your amount for " + categories[i] + " = " + amounts[i])