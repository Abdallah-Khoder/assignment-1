salaryMonth = input("Enter your salary of the month : ")
monthName = input("Enter the name of the month : ")
categories = ["Savings" , "Rent" , "Electricity"]
amounts = [] 
for i in range(len(categories)) : 
    amount = input("Enter amount for " + categories[i] + " : ")
    amounts.append(amount)
print("Your salary of the mounth =  " + salaryMonth)
for i in range(len(amounts)) : 
    print("Your amount for " + categories[i] + " = " + amounts[i])

    