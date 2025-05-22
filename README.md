# 🏧 Simple ATM Machine in Python
## 👨‍💻 Author
Ejims Chigbogu

A command-line ATM simulation that handles basic banking operations like deposits, withdrawals, and user authentication using a CSV file for storage. This project is designed to practice file handling, data management, and Python fundamentals.

---
## 📂 Project Structure
├── atm.py              # Core logic for ATM operations and menu functions
├── main.py             # Main entry point and flow control
├── users.csv           # Database of user records
├── test_atm.py         # Unit tests for ATM functions
├── README.md           # Project documentation


## 🚀 Features
### ✅ Completed
- [x] PIN-based user authentication
- [x] View balance
- [x] Deposit money
- [x] Withdraw money
- [x] User data stored in `users.csv`
- [x] Add new users feature 
      - New users can create account with initial deposit
      - Validted new PIN, makes sure all PIN are uniqeu

- [x] Added Main menu 
      - Allows new users to create account
      - Exisiting users to login as well


### 🛠️ In Progress / Planned
- [ ] 
- [ ] Transfer funds between users
- [ ] Transaction history log (saved to `transactions.csv`)
- [ ] Mini account statement (print last 5 transactions)
- [ ] PIN change feature
- [ ] Lock account after multiple failed attempts
- [ ] Admin panel for overview/reporting
- [ ] Daily or session-based CSV backups
- [ ] Export user statement to `.txt` or `.pdf`
- [ ] Date/time record of transactions

---

## 🧪 How to Run

1. Make sure Python is installed on your system.
2. Run the main script:
   python main.py
3. Follow the on-screen prompts to log in using your 4-digit PIN.


## Technologies Used
Python 3.x
CSV for file-based storage
Ruff for formating and linting






