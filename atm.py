"""
ATM machine
"""

# Users
users = {
    "1234": {"name": "Alice", "balance": 500},
    "5678": {"name": "Bob", "balance": 300},
    "2468": {"name": "Charlie", "balance": 750},
    "1357": {"name": "Diana", "balance": 620},
    "1122": {"name": "Ethan", "balance": 400},
    "3344": {"name": "Fiona", "balance": 1000},
    "5566": {"name": "George", "balance": 150},
    "7788": {"name": "Hannah", "balance": 920},
    "9900": {"name": "Ivan", "balance": 0},
    "2020": {"name": "Jade", "balance": 850},
}


# auth_user function
def auth_user():
    auth_complete = False
    while not auth_complete:
        try:
            # prompt for pin and then check the user Db to see if there a match
            user_pin = str(input("\n>>> Enter 4 digits PIN to continue: "))
            if user_pin in users:
                auth_complete = True
            elif user_pin not in users:
                    print("\n❌ Wrong PIN, try again\n")
        except ValueError:
            print("\n⚠️ Enter the correct 4 digit PIN to continue\n")
    return user_pin


def check_balance(user_pin):
    print(f"\n✅ Account balance: ${users[user_pin]['balance']}\n")


def deposit(user_pin):
    while True:
        try:
            amount_deposite = float(input(">>> Enter amount to deposit: "))
            copy_amount_deposite = amount_deposite

            if copy_amount_deposite:
                copy_amount_deposite += users[user_pin]["balance"]
                print(f'\n✅ The sum ${amount_deposite} has been deposited to your account successfully!!')
                print('✅ Deposite successfull!\n')
                break
            else:
                print('⚠️ Enter the exact amount to deposite')
        except ValueError:
            print('⚠️ Enter Number value')
            continue

        #Display Option to view Balance after withdrawal    
        try:
            option_check_balance = input(">>> Press (Y/N) to see account balance: ").title()
            if option_check_balance == "Y":
                check_balance(user_pin)  # just printing the bal after deposit to be sure
        except ValueError:
            print('⚠️ Use Y or N')

def withdraw(user_pin):
    while True:
        
        try:
            amount_withdraw = float(input(">>> Enter amount to withdraw: "))
            copy_amount_withdraw = amount_withdraw
            
            if copy_amount_withdraw > users[user_pin]["balance"]:
                print("\n⚠️ Insufficient balance.")
                insufficient_count = 0
                while insufficient_count < 2:
                    print(insufficient_count)
                    insufficient_count += 1
                    print(insufficient_count)

                    
                    # print(f"FYI: Your balance ${users[user_pin]['balance']}.")
            elif copy_amount_withdraw <= 0:
                print("\n⚠️ Minimum withdrawal amount $5")
            elif copy_amount_withdraw == users[user_pin]["balance"]:
                #recomfirn if user wants to do max withdrawal, if yes go ahead
                try:
                    two_factor = str(input('''\n⚠️ You about to withdraw the max amount in this account, Use "Y" to continue with max withdrawal "N" to discontinue: ''')).title()
                    if two_factor == "Y":
                        users[user_pin]["balance"] -= copy_amount_withdraw
                        print("\n✅ Withdrawal Successfully!!\n")
                        break
                except ValueError:
                    print('\n⚠️ Use "Y" to continue OR "N" to disconue.\n')
            else:
                users[user_pin]["balance"] -= copy_amount_withdraw
                print("\n✅ Withdrawal Successfully!!\n")
                break
                
        except ValueError:
            print("\n⚠️ Enter amout to withdraw\n")


def exit():
    print("\nThanks for banking with us, have a nice day!😊")


def main():
    while True:
        # Display welcome message
        print("\nGood day!!, Welcome to this ATM😊")
        print('What would you like to do?, Choose from the menu codes below\n')
        try:
            main_menu = str(input(
        """> Check Balance. (B)\n
> Deposit Money. (D)\n
> Make a Withdraw. (W)\n
> Exit (E).\n>>>: """)
            ).title()

            if main_menu in ["B","D","W"]:
                user_pin = auth_user() #catch the returned auth_user
                if main_menu == "B":
                    check_balance(user_pin)
                elif main_menu == "D":
                    deposit(user_pin)
                elif main_menu == "W":
                    withdraw(user_pin)
            elif main_menu == "E":
                exit()
                break
        except ValueError:
            print(">>>⚠️ Choose from the Options")


if __name__ == "__main__":
    main()
