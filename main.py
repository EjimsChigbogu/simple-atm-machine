from atm import (
    auth_user,
     check_balance,
    deposit,
    withdraw,
    transfer,
    main_menu,
    menu,
    greet_user,
    open_account,
    logging,
    mask_PIN,
)


def main():
    print("💳 Good day!!, Welcome to Simple ATM")
    while True:
        main_menu()
        choice = input(">>> Choose an option (1-3): ").strip()

        if choice == "1":
            user_pin = auth_user()
            while True:
                greet_user(user_pin)

                menu()
                choice = input(">>> Choose an option (1-5): ").strip()

                if choice == "1":
                    check_balance(user_pin)
                elif choice == "2":
                    deposit(user_pin)
                elif choice == "3":
                    withdraw(user_pin)
                elif choice == "4":
                    transfer(user_pin)
                elif choice == "5":
                    print("👋 Thank you for using Simple ATM. Goodbye!")
                    logging.info(f"LOGOUT_SUCCESSFULL - PIN: {mask_PIN(user_pin)}")
                    break
                else:
                    print("⚠️ Invalid option. Please select 1, 2, 3, 4 and 5.")
                    logging.info(f"INVALID_MENU_CHOICE: {choice}")

        elif choice == "2":
            open_account()
        elif choice == "3":
            print("👋 Thank you for using Simple ATM. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please select 1, 2, or 3.")
            logging.info(f"INVALID_MAIN_MENU_CHOICE: {choice}")


if __name__ == "__main__":
    main()
