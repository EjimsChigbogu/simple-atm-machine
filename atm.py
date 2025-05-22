"""
ATM machine
"""
import csv

# ID user and display message 
def greet_user(user_pin):
    try:
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["PIN"] == user_pin:
                    print(f"\nWelcome, {row['Name']}")
    except FileNotFoundError as e:
        file_name = e.filename
        print(f" ⚠️ {file_name} was not found.")

#Programm Menu 
def main_menu():
    print("""
======= ATM MENU =======
1. Loging
2. Open Account
3. Exit
========================
""")
    
#Programm Menu 
def menu():
    print("""
======= ATM MENU =======
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Exit
========================
""")


# auth_user function
def auth_user():
    auth_complete = False
    while not auth_complete:
        try:
            # prompt for pin and then check the user Db to see if there a match
            user_pin = input("\n>>> Enter 4-digits PIN to continue: ")

            # open CSV, read through and check if the user_pin is in PIN
            try:
                with open("users.csv", "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if user_pin == row["PIN"]:
                            auth_complete = True
                            break

                    # Wrong user PIN
                    if not auth_complete:
                        print("\n❌ Wrong PIN, try again\n")

            except FileNotFoundError as e:
                file_name = e.filename
                print(f" ⚠️ The file '{file_name}' was not found.")
        except ValueError:
            print("\n⚠️ Enter the correct 4 digit PIN to continue\n")
    return user_pin


def check_balance(user_pin):
    try:
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["PIN"] == user_pin:
                    print(f"\n✅ Account balance: ${row['Balance']}\n")
    except FileNotFoundError as e:
        file_name = e.filename
        print(f" ⚠️ {file_name} was not found.")


def deposit(user_pin):
    deposit_successful = False
    while not deposit_successful:
        # open users.csv Db in read mode
        try:
            all_users_list = []
            with open("users.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    all_users_list.append(row)

                #loop through the list containing dictionaries of users "all_user_list""
                for user in all_users_list:
                    if user["PIN"] == user_pin:
                        #promt for amount since user exists
                        try:
                            deposit_amount = float(input(">>> Enter amount to deposit: "))
                        except ValueError:
                            print("⚠️ Enter dollar value")

                        # convert the user's balance to float
                        balanceTo_float = float(user["Balance"])

                        # validate deposite amount  > 0
                        if deposit_amount > 0:
                            balanceTo_float += deposit_amount
                            user["Balance"] = balanceTo_float
                            deposit_successful = True
                            break
                        else:
                            print("⚠️ Enter positive amount")

            # update users Db only after successful deposit
            if deposit_successful:
                try:
                    with open("users.csv", "w") as file:
                        writer = csv.DictWriter(file, fieldnames=["PIN", "Name", "Balance"])
                        writer.writeheader()
                        writer.writerows(all_users_list)
                except FileNotFoundError as e:
                    file_name = e.filename
                    print(f"⚠️ {file_name} not found.")

                # print success message to the screen
                print(f"\n✅ The sum ${deposit_amount} has been deposited to your account successfully!!")

        except FileNotFoundError as e:
            file_name = e.filename
            print(f"⚠️ {file_name} not found.")


def withdraw(user_pin):
    withdrawal_successful = False
    while not withdrawal_successful:
        try:
            all_user_list = [] 
            with open("users.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    #add all user dictionary from csv file to a list
                    all_user_list.append(row)

                # loop through the list containing dictionaries of users "all_user_list""
                for user in all_user_list:
                    if user["PIN"] == user_pin:
                        #prompt for amount
                        try:
                            amount_withdraw = float(input(">>> Enter amount to withdraw: "))
                        except ValueError:
                            print("⚠️Enter positive amount")

                        #convert user's balance to float for float to float conparison
                        balanceTo_float = float(user["Balance"])

                        if amount_withdraw > balanceTo_float:
                            print("⚠️ Insufficient balance")
                        elif amount_withdraw <= 0:
                            print("⚠️ Minimum withdrawal is $1")
                        elif amount_withdraw == balanceTo_float:
                            #recomfirn if user wants to do max withdrawal, if yes go ahead
                            try:
                                confirm_max_withdrawal = str(input('''\n⚠️ You about to withdraw the max amount in this account, Use "Y" to continue with max withdrawal "N" to discontinue: ''')).title()
                                if confirm_max_withdrawal == "Y":
                                    balanceTo_float -= amount_withdraw
                                    print("\n✅ Withdrawal Successfully!!\n")
                                    user["Balance"] = balanceTo_float
                                    withdrawal_successful = True
                                    break
                            except ValueError:
                                print('\n⚠️ Use "Y" to continue OR "N" to disconue.\n')
                        else:
                            balanceTo_float -= amount_withdraw
                            print("\n✅ Withdrawal Successfully!!\n")
                            user["Balance"] = balanceTo_float
                            withdrawal_successful = True
                            break

                #Update User including the new changes
                if withdrawal_successful:
                    try:
                        with open("users.csv", "w") as file:
                            writer = csv.DictWriter(file, fieldnames=["PIN","Name","Balance"])
                            writer.writeheader()
                            writer.writerows(all_user_list)
                    except FileNotFoundError as e:
                        file_name = e.filename
                        print(f"⚠️ {file_name} not found")

        except ValueError:
            print("\n⚠️ Enter amout to withdraw\n")


def transfer():
    pass

def open_account():
    open_acct_successful = False
    while not open_acct_successful:
        try:
            #collect user details
            full_name = input(">>> Enter your full name :").title()

            #prompt for deposit amount, also validate for amount <5
            while True:
                try:
                    initial_deposite = float(input(">>> Enter initial deposite amount (Min. $5): "))
                    if initial_deposite < 5.0:
                        print("\n⚠️ Initial deposit amount must be up to $5")
                    elif initial_deposite >= 5.0:
                        break
                except ValueError:
                    print("⚠️ Enter dollar value")
                
            #prompt for account PIN
            pin = input(">>> Create 4-digit PIN: ")

            #Run pin through Db to avoid users sharing same pin
            with open("users.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if pin == row["PIN"]:
                        print("⚠️ This PIN already use ")
                    else:
                        try:
                            with open("users.csv", "a", newline="") as file:
                                add_user = csv.writer(file)
                                add_user.writerow([pin, full_name, initial_deposite])
                                open_acct_successful = True
                                print("\n✅ Account created successfully")
                                print(f"🎉 Welcome, {full_name}")
                                break   
                        except Exception as e:
                            print(f"An error occures {e}")
        except Exception as e:
            print(f"Error occured {e}")



