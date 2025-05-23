import logging
import csv

logging.basicConfig(
    filename="atm.log", level=logging.INFO, format="%(levelname)s - %(message)s - %(asctime)s"
)

#Mask user PIN in the log sheet
def mask_PIN(user_pin):
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        masked_pin = "**" + user_pin[2:]
        for user in reader:
            if user_pin == user["PIN"]:
                user["PIN"] = masked_pin
                return masked_pin


# Identify user and display message with user's name
def greet_user(user_pin):
    try:
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["PIN"] == user_pin:
                    name = row["Name"]
                    print(f"\nWelcome, {name}")
    except FileNotFoundError as e:
        file_name = e.filename
        print(f" ⚠️ {file_name} was not found.")
        logging.error(f"LOGIN_FAILED - FileNotFoundError: {file_name}")


# Programm Main Menu
def main_menu():
    print("""
======= ATM MAIN MENU =======
1. Loging
2. Open Account
3. Exit
========================
""")


# Programm Menu
def menu():
    print("""
======= ATM MENU =======
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Log out
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
                            user_name = row["Name"]
                            auth_complete = True
                            logging.info(
                                f"AUTHENTICATION_SUCCESSFUL - LOGIN_SUCCESSFULL - USER: {user_name} - PIN: {mask_PIN(user_pin)}"
                            )
                            break

                    # Wrong user PIN
                    if not auth_complete:
                        print("\n❌ Wrong PIN, try again\n")
                        logging.warning(f"AUTHENTICATION_FAILED - PIN - {user_pin} - Wrong PIN")

            except FileNotFoundError as e:
                file_name = e.filename
                print(f" ⚠️ The file '{file_name}' was not found.")
                logging.error(f"{file_name} - FileNotFoundError OR COULD NOT BE OPENED")
        except ValueError:
            print("\n⚠️ Enter the correct 4 digit PIN to continue\n")
            logging.warning(f"LOGIN_FAILED - {user_pin} - ValueError")
    return user_pin


def check_balance(user_pin):
    try:
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["PIN"] == user_pin:
                    balance = row["Balance"]
                    print(f"\n✅ Account balance: ${balance}\n")
                    logging.info(
                        f"BALANCE_CHECK_SUCCESSFUL - USER: {row['Name']} - Balance: ${balance}"
                    )
                    return
        # If loop completes with no match
        logging.warning(f"BALANCE_CHECK_FAILED - PIN: {user_pin} - User not found")
    except FileNotFoundError as e:
        file_name = e.filename
        print(f" ⚠️ {file_name} was not found.")
        logging.error(f"BALANCE_CHECK_FAILED - File not found: {file_name}")


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

                # loop through the list containing dictionaries of users "all_user_list""
                for user in all_users_list:
                    if user["PIN"] == user_pin:
                        # promt for amount since user exists
                        try:
                            deposit_amount = float(input(">>> Enter amount to deposit: "))
                        except ValueError:
                            print("⚠️ Enter dollar value")
                            logging.info(
                                f"DEPOSIT_FAILED - USER: {user['Name']} - PIN: {mask_PIN(user_pin)} - ValueError: ${deposit_amount}"
                            )

                        # convert the user's balance to float
                        balance = float(user["Balance"])

                        # validate deposite amount  > 0
                        if deposit_amount > 0:
                            balance += deposit_amount
                            user["Balance"] = balance
                            deposit_successful = True
                            break
                        else:
                            print("⚠️ Enter positive amount")
                            logging.info(
                                f"DEPOSIT_FAILED - USER: {user['Name']} -  - PIN: {mask_PIN(user_pin)} - AMOUNT: ${deposit_amount}"
                            )

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
                    logging.error(f"DEPOSIT_FAILED - FILE_NOT_FOUND: {file_name}")

                # print success message to the screen
                print(
                    f"\n✅ The sum ${deposit_amount} has been deposited to your account successfully!!"
                )
                logging.info(
                    f"DEPOSIT_SUCCESSFUL - USER: {user['Name']} - PIN: {mask_PIN(user_pin)} - AMOUNT: ${deposit_amount}"
                )

        except FileNotFoundError as e:
            file_name = e.filename
            print(f"⚠️ {file_name} not found.")
            logging.error(f"DEPOSIT_FAILED - FileNotFoundError: {file_name}")


def withdraw(user_pin):
    withdrawal_successful = False
    while not withdrawal_successful:
        try:
            all_user_list = []
            with open("users.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # add all user dictionary from csv file to a list
                    all_user_list.append(row)

                # loop through the list containing dictionaries of users "all_user_list""
                for user in all_user_list:
                    if user["PIN"] == user_pin:
                        # prompt for amount
                        try:
                            amount_withdraw = float(input(">>> Enter amount to withdraw: "))
                        except ValueError:
                            print("⚠️Enter positive amount")
                            logging.info(f"WITHDRAWAL_ATTEMPT_FAILED - ValueError: {ValueError}")

                        # convert user's balance to float for float to float conparison
                        balance = float(user["Balance"])

                        if amount_withdraw > balance:
                            print("⚠️ Insufficient balance")
                            logging.info(
                                f"WITHDRAWAL_ATTEMPT_FAILED - AMOUNT: {amount_withdraw} - Greater than BALANCE: {balance}"
                            )

                        elif amount_withdraw <= 0:
                            print("⚠️ Minimum withdrawal is $1")
                            logging.info(
                                f"WITHDRAWAL_ATTEMPT_FAILED - AMOUNT: {amount_withdraw} - Less than Min. Withdrawal Amount: {balance}"
                            )
                        elif amount_withdraw == balance:
                            # recomfirn if user wants to do max withdrawal, if yes go ahead
                            try:
                                confirm_max_withdrawal = str(
                                    input(
                                        """\n⚠️ You about to withdraw the max amount in this account, Use "Y" to continue with max withdrawal "N" to discontinue: """
                                    )
                                ).title()
                                logging.warning(f"MAX_WITHDRAWAL_CONFIRMATION - BALANCE: {balance}")

                                if confirm_max_withdrawal == "Y":
                                    balance -= amount_withdraw
                                    user["Balance"] = balance
                                    withdrawal_successful = True
                                    print("\n✅ Withdrawal Successfully!!\n")
                                    logging.info(
                                        f"WITHDRAWAL_SUDCCESSFUL - AMOUNT: {amount_withdraw}"
                                    )
                                    break
                            except ValueError:
                                print('\n⚠️ Use "Y" to continue OR "N" to disconue.\n')
                                logging.warning(
                                    f"MAX_WITHDRAWAL_CONFIRMATION - VALUE_ERROR: {confirm_max_withdrawal}"
                                )
                        else:
                            balance -= amount_withdraw
                            user["Balance"] = balance
                            withdrawal_successful = True
                            print("\n✅ Withdrawal Successfully!!\n")
                            logging.info(
                                f"WITHDRAWAL_SUCCESSFUL - USER: {user['Name']} - BALANCE: {balance}"
                            )
                            break

                # log for user not found
                logging.warning(f"WITHDRAWAL_FAILED - USER_NOT_FOUND: {user_pin}")

                # Update User including the new changes
                if withdrawal_successful:
                    try:
                        with open("users.csv", "w") as file:
                            writer = csv.DictWriter(file, fieldnames=["PIN", "Name", "Balance"])
                            writer.writeheader()
                            writer.writerows(all_user_list)
                    except FileNotFoundError as e:
                        file_name = e.filename
                        print(f"⚠️ {file_name} not found")
                        logging.error(f"WITHDRAWAL_FAILED - FILE_NOT_FOUND: {file_name}")

        except FileNotFoundError as e:
            file_name = e.filename
            print(f"\n⚠️ {file_name} no found\n")
            logging.error(f"WITHDRAWAL_FAILED - FILE_NOT_FOUND: {file_name}")


def transfer():
    pass


def open_account():
    open_acct_successful = False
    while not open_acct_successful:
        try:
            # collect user details
            full_name = input(">>> Enter your full name :").title()

            # prompt for deposit amount, also validate for amount <5
            while True:
                try:
                    initial_deposite = float(input(">>> Enter initial deposite amount (Min. $5): "))
                    if initial_deposite < 5.0:
                        print("\n⚠️ Initial deposit amount must be up to $5")
                        logging.info(
                            f"ACCOUNT_CREATION_INTERRUPT - INITIAL_DEPOSIT - {initial_deposite} - < Min. amount for openning account"
                        )
                    elif initial_deposite >= 5.0:
                        break
                except ValueError:
                    print("⚠️ Enter dollar value")
                    logging.info(
                        f"ACCOUNT_CREATION_INTERRUPT - INITIAL_DEPOSIT - {initial_deposite} - ValueError"
                    )

            # prompt for account PIN
            pin = input(">>> Create 4-digit PIN: ")

            # Run pin through Db to avoid users sharing same pin
            try:
                with open("users.csv", "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if pin == row["PIN"]:
                            print("⚠️ This PIN already in use ")

                            logging.info(
                                f"ACCOUNT_CREATION_INTERRUPTED - USER: {full_name} - PIN - {pin} - Already in use"
                            )
                        else:
                            try:
                                with open("users.csv", "a", newline="") as file:
                                    add_user = csv.writer(file)
                                    add_user.writerow([pin, full_name, initial_deposite])
                                    open_acct_successful = True
                                    print(
                                        "\n✅ Account created successfully\n🎉 Welcome, {full_name}"
                                    )

                                    logging.info(
                                        f"ACCOUNT_CREATED_SUCCESSFULLY - NEW_USER - {full_name} - INITIAL_DEPOSIT: ${initial_deposite}"
                                    )

                                    break
                            except Exception as e:
                                print(f"An error occures {e}")

                                logging.error(
                                    f"ACCOUNT_OPENNING_FAILED - File not found OR Exception: {e}"
                                )
            except FileNotFoundError as e:
                file_name = e.filename
                print(f"{file_name} Not found")
                logging.error(f"ACCOUNT_OPENNING_FAILED - FileNotFoundError: {file_name}")

        except Exception as e:
            print(f"Error occured {e}")
            logging.error(f"ACCOUNT_CREATION_INTERRUPT - Exception - {e}")
