acholder={"ab":"10","bc":"20","cd":"30","de":"40"}
balance={"10":"100",  "20":"200",  "30":"300","40":"400"}

def print_menu():
    print ("1. List Account holders and Account no")
    print ("2. Open an Account")
    print ("3. Close an Account")
    print ("4. Withdraw money")
    print ("5. Deposit Money")
    print ("6. Quit")

menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-6): "))
    if menu_choice == 1:
     print(acholder.items())
    elif menu_choice == 2:
        print ("Enter a new Accountnumber")
        numbernew = input("New accountnumber: ")
        name=input("enter your name")
        acholdernew={name,numbernew}
        acholder.update(acholdernew)
        initialdeposit=input("enter initial deposit you want to deposit")
        balancenew={numbernew,initialdeposit}
        balance.update(balancenew)
        print (f"welcome {name} your Accountnumber {numbernew} opened.")
        acholder=acholder

    elif menu_choice == 3:
        print("Close an Accountnumber")
        number = input("Accountnumber: ")
        if number in balance:
            balance.pop(number)
            print (f"Accountnumber{number} is closed.")
        else:
            print (f"Accountnumber{ number}was not found")

    elif menu_choice == 4:
        print ("Withdraw money from Account.")
        number = input("Accoutnnumber: ")
        if number in balance:
            withdraw = int(input("How much money would you like to withdraw? > "))
            if withdraw < int(balance[number]):
                balance[number]=int(balance[number])-withdraw
                print (f"Your new balance is {balance[number]}")
            
            else:
                print ("There are no sufficient funds on this accountnumber")
       
        else:
            print ("accountnumber is invalid")
    
    elif menu_choice == 5:
        print ("Deposit money onto Account.")
        number = input("Accountnumber: ")
        if number in balance:
            deposit = float(input("How much money would you like to deposit? > "))
            balance[number]=int(balance[number])+deposit
            print (f"Your new balance is  {balance[number]}")
        else:
            print ("That accountnumber does not exist.")
    elif menu_choice == 6:
        print ("Quit.")
        break
    else:
        print ("Please enter a number between 1 and 6.")
    print_menu()