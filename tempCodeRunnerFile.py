    while True:
            user_pin = auth_user()
            
            greet_user(user_pin)
            Inner_menu()
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

