import random
import time
import os

account_registry ={}
account_numbers = []
admin_pin = '1234'

class BankAccount():
    
    def __init__(self,acc_number, acc_name,balance,acc_type,int_rate = 0, min_balance = 0):
        
   
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = balance
        self.acc_type = acc_type
        self.int_rate = int_rate
        self.min_balance = min_balance

        
    def __str__(self):
        return f"{self.acc_name}, holder of {self.acc_type} account, number {self.acc_number}, has available balance {self.balance}"

    def __del__(self):
        print(f"Account of holder {self.acc_name} has been deleted. \nBalance to withdraw - {self.balance}")
    
    def account_created(self):
        print (f"Account Successfuly Created \n"
                f'Account Number - {self.acc_number} \n'
                f'Holders Name - {self.acc_name} \n'
                f'Account Type - {self.acc_type}\n'
                f'Available Balance - {self.balance} \n')
        
        
        


    
    def deposit(self,amount):
   
        self.balance += amount
        print(f'Transaction successful \n Deposit: {amount}, New balance: {self.balance}')
        
        

    def withdraw(self,amount):

        if amount > self.balance:
            print('Insufficent funds, transaction Unsuccesful')
        
        else:
            self.balance -= amount
            print(f'Transaction successful \nWithdrawn: {amount}, New balance: {self.balance}')
        
    def check_balance(self):
        print (f'Curent balance: {self.balance}')
    
    def transfer(self,amount,recipient_number):

        if amount > self.balance:
            print('Insufficent funds, transaction Unsuccesful')
        
        else:
            self.balance -= amount
            account_registry[recipient_number].balance += amount

            print(f'Transaction successful. New Balance - {self.balance}')

def clear_terminal():
   
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')

def create_instance(acc_name,balance,acc_type,CSV):
    global account_registry

    y = account_number()
    acc_name = acc_name.title()
    balance = int(balance)

    if acc_type.upper() == 'S':
        acc_type = 'Savings Account'
    else:
        acc_type = 'Current Account'

    account_registry[f"{y}"] = BankAccount(y,acc_name,balance,acc_type)
    
    if not CSV:
        clear_terminal()
        account_registry[f"{y}"].account_created()

        print('returning to the main menu...')
        time.sleep(4)
    
        main_menu()
    else:
        pass

def money():
    while True:
        try:
            money = float(input("Enter the monetary value: "))
            if money < 0:
                print("Value cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    return money

def account_number():
    while True:
            y = str(random.randint(10000000, 99999999))

            if y not in account_numbers:
                break
    account_numbers.append(y)
    return y

def user_input():
    

    print("Enter the following details to create an account.")
    
    acc_name = input('Please enter the account holders name - ')

    balance = money()

    while True:
        try:
            acc_type = input('Please enter the account type, S for savings, C for current account - ')
            
            if acc_type.upper() not in ['S','C']:
                print('Incorrect Input, Please try again')
                continue
            break
        except ValueError:
            print('Invalid input, Please try again')

    print('\n')
    
    return acc_name,balance,acc_type

def add_csv():
    counter = 0
    while True:

        file_name = input('Enter the file name to open, or the directory - ')
        try:
            with open(file_name, 'r') as file: 
                next(file)
                for line in file:
                    counter +=1

                    name,balance,acc_type = line.strip().split(',')
                    
                    create_instance(name,balance,acc_type,True)

            break

        except:
            print('File not found,please try again.')
    print(f"{counter} records succesfuly added \n Returning to the Admin Menu...")
    

def export_csv():
    if len(account_registry) == 0:
        print("ERROR: No accounts added to the system.")
    else:
        with open('Registry_CSV.csv','w') as file:
            file.write(f"Account Number,Name,Balance,Account Type\n")
            for key in account_registry.keys():
                file.write(f"{account_registry[key].acc_number},{account_registry[key].acc_name},{account_registry[key].balance},{account_registry[key].acc_type}\n")
        print('File (Registry_CSV.csv) Succesfully expoted to the directory of the currect program.')

    print('\nReturning to the Admin Menu...')
    time.sleep(2)
    
 
def transaction_menu():
    clear_terminal()
    def transaction_sub_menu():
            while True:
                option = input(
                    'Please enter the transaction you would like to pick. \n'
                    '1 - Check Balance \n'
                    '2 - Deposit \n'
                    '3 - Withdraw \n'
                    '4 - Transfer \n'
                    '5 - Return to main menu \n'
                    'Enter 1,2,3,4 or 5: '
                    
                )

                

                if option in ['1', '2', '3', '4', '5']:
                    print(f"You selected option {option}.\n") 
                    break
                else:
                    print('Incorrect Input, Please try again. \n')
            
            if option == "1":
                account_registry[number].check_balance()
            
            if option == '2':
                account_registry[number].deposit(money())

            if option == '3':
                account_registry[number].withdraw(money())
            
            if option == '4':
                while True:
                    recipient = input( 'Please enter account number of recipient. \n'
                                        'Account Number - ')
                    
                    if recipient in account_registry.keys():
                        print(f"Transfer to - {account_registry[recipient].acc_name}") 
                        break

                    else:
                        print('Incorrect acccount number, Please try again. \n')

                account_registry[number].transfer(money(),recipient)

            if option == '5':
                clear_terminal()
                main_menu()

            print('Returning to transaction menu... \n')
            time.sleep(3)
            transaction_sub_menu()
            

    while True:
        number = input( 'Transaction Menu, Please enter your account number. \n'
                        'Account Number - ')

        if number in account_registry.keys():
            print(f"Welcome {account_registry[number].acc_name}") 
            break
        else:
            print('Incorrect acccount number, Please try again. \n')
    
    transaction_sub_menu()

    

def admin_menu():
    clear_terminal()
    global admin_pin 

    def admin_sub_menu():
        global admin_pin
        while True:
                option = input(
                    'Admin Menu, Please enter the option you would like to pick. \n'
                    '1 - Change Admin Pin \n'
                    '2 - Add data using CSV file \n'
                    '3 - Export Account Registeies as CSV file \n'
                    '4 - Delete an acccount \n'
                    '5 - Return to main menu \n'
                    'Enter 1,2,3,4 or 5: '
                )

                if option in ['1', '2', '3', '4', '5']:
                    print(f"You selected option {option}.\n") 
                    break
                else:
                    print('Incorrect Input, Please try again. \n')
                
        if option == '1':
            print('Re-enter current pin')
            if check_pin():
                
                admin_pin = input('Enter new pin - ')
                print(f'Admin Pin Succesfuly changed to {admin_pin}')
                
                    
        
            else:
                print('Returning to admin menu...')
                

            admin_sub_menu()

        if option == '2':
            add_csv()
            admin_sub_menu()

        if option =='3':
            export_csv()
            admin_sub_menu()

        if option == '4':
            while True:
                number = input( 'Enter Account Number of the holder to delete. \n'
                        'Account Number - ')

                if number in account_registry.keys():
                    print(f"Deleting acccount of holder - {account_registry[number].acc_name}") 
                    break
                else:
                    print('Returning to admin menu...')
                    admin_sub_menu()

        if option == '5':
                clear_terminal()
                main_menu()

        

    def check_pin():
        while True:
            
            pin = input('Please Enter the Admin Pin - ')
        
            if pin == admin_pin:
                print(' \n Authentication Successful.')
                return True

            else:
                print('Incorrect Pin. Returning to main menu...')
                time.sleep(1.5)
                return False
    
    if check_pin():
        admin_sub_menu()
    else:
        clear_terminal()
        main_menu()

def main_menu():
    
    while True:
        option = input(
            'Welcome to the banking system, Please select an option to continue. \n'
            '1 - Create an account \n'
            '2 - Transactions \n'
            '3 - Admin \n'
            'Enter 1,2 or 3: '
        )

        if option in ['1', '2', '3']:
            print(f"You selected option {option}.\n") 
            break
        else:
            print('Incorrect Input, Please try again. \n')

    if option == '1':
        acc_name,balance,acc_type = user_input()
        create_instance(acc_name,balance,acc_type,False)
        
    
    elif option == '2':
        transaction_menu()

    else:
        admin_menu()


main_menu()
