from atm import auth_user, deposit, withdraw, check_balance, main_menu, menu, greet_user, open_account


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
                    pass
                elif choice ==  "5":
                    print("👋 Thank you for using Simple ATM. Goodbye!")
                    break
                else:
                    print("⚠️ Invalid option. Please select 1, 2, 3, 4, 5 or 6.")

        elif choice == "2":
            open_account()
        elif choice == "3":
            print("👋 Thank you for using Simple ATM. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
