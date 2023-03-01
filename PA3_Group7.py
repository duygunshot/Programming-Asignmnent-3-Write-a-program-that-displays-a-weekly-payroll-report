#Group7
#Dean Tran, Edwin Rodriguez, Elisa Shukuru
#03/06/2023
"""the purpose of the programming assignment is to write a program that displays a weekly payroll report. A loop in the program 
should ask the user for the employee number, gross pay, state tax, federal tax, 
and FICA withholdings. The loop will terminate when 0 is entered for the 
employee number. After the data is entered, the program should display totals 
for gross pay, state tax, federal tax, FICA withholdings, and net pay.
"""
emNumber = 0
grossPayTotal = 0
stateTaxTotal = 0
federalTaxTotal = 0
ficaTotal = 0
netPayTotal = 0

while True:
    emNumber = int(input("Plese enter employee number (Enter 0 to exit): "))#Ask user to enter employee number
    while (emNumber < 0):
        emNumber = int(input("The number cannot be negative. Please enter again (Enter 0 to exit): "))#Ask user to re-enter if the number is negative
    if (emNumber == 0):#break the loop if user enters 0
        break
    
    while True:
        grossPay = float(input("Please enter gross pay number: "))#Ask user to enter gross pay
        while (grossPay < 0):
            grossPay = float(input("The number cannot be negative. Please enter again: "))#Ask user to re-enter if the number is negative

        stateTax = float(input("Enter state tax number: "))#Ask user to enter state tax
        while(stateTax < 0):
            stateTax = float(input("The number cannot be negative. Please enter again: "))#Ask user to re-enter if the number is negative
        
        federalTax = float(input("Please enter federal tax number: "))#Ask user to enter federal tax
        while(federalTax < 0):
            federalTax = float(input("The number cannot be negative. Please enter again: "))#Ask user to re-enter if the number is negative

        fica = float(input("Please enter FICA withholding: "))#Ask user to enter FICA withholdings
        while(fica < 0):
            fica = float(input("The number cannot be negative. Please enter again: "))#Ask user to re-enter if the number is negative

        if (grossPay < (stateTax + federalTax + fica )):#Ask user to enter datas for this employee again if the sum of state tax + federal tax + FICA withholdings is greater than gross pay
            print("The sum of state tax + federal tax + FICA withholdings cannot be greater than gross pay. Please enter datas for this employee again.")
            break
        #add entered numbers to totals
        grossPayTotal += grossPay
        stateTaxTotal += stateTax
        federalTaxTotal += federalTax
        ficaTotal += fica

        print("Please enter datas for the next employee")#switch to the next employee
        break


netPayTotal = grossPayTotal - (stateTaxTotal + federalTaxTotal + ficaTotal)#calculate the total of net pays
#Display total datas
print(f"The total gross pay is: ${grossPayTotal:,.2f}")
print(f"The total state tax is: ${stateTaxTotal:,.2f}")
print(f"The total federal tax is: ${federalTaxTotal:,.2f}")
print(f"The total FICA withholding is: ${ficaTotal:,.2f}")
print(f"The total net pay is: ${netPayTotal:,.2f}")


        





            

    
