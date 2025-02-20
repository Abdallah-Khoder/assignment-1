import math 
salaryMonth = input("Enter your salary of the month : ")
monthName = input("Enter the name of the month : ")
categories = ["Savings" , "Rent" , "Electricity"]
amounts = [] 
for i in range(len(categories)) : 
    amount = input("Enter amount for " + categories[i] + " : ")
    amounts.append(amount)
print("Your salary of the mounth =  " + salaryMonth + "$")
for i in range(len(amounts)) : 
    print("Your amount for " + categories[i] + " = " + amounts[i] + "$")

totalAmount = int(amounts[0]) +int(amounts[1]) + int(amounts[2])
print("The total amount for the month = " + str(totalAmount) + "$")
restSalary = int(salaryMonth) - totalAmount
print("Your rest Salary = " + str(restSalary) + "$")
rentElectYear = (int(amounts[1]) + int(amounts[2]))*12 
print("Amounts for Rent and Electricity in one year = " + str(rentElectYear) + "$")
salaryPower2 = math.pow(int(salaryMonth) , 2) 
print("The total salary raised of power 2 = " + str(salaryPower2) + "$")