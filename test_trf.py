import csv
import os
from atm import transfer  # Assuming transfer() is defined in atm.py
from unittest import mock

# Sample data to use for testing
test_users = [
    {"PIN": "1234", "AccountNumber": "10001", "Name": "John Doe", "Balance": "500"},
    {"PIN": "5678", "AccountNumber": "10002", "Name": "Jane Smith", "Balance": "300"},
]


# Utility to create a fresh users.csv
def setup_test_csv():
    with open("users.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["PIN", "AccountNumber", "Name", "Balance"])
        writer.writeheader()
        writer.writerows(test_users)


# Utility to read user balances
def get_balances():
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        return {row["AccountNumber"]: float(row["Balance"]) for row in reader}


# Main test function
def test_transfer_success():
    setup_test_csv()

    # Simulate user input (recipient account number and amount)
    with mock.patch("builtins.input", side_effect=["10002", "100"]):
        transfer("1234")  # Passing sender's PIN

    # Check the result
    balances = get_balances()
    assert balances["10001"] == 400  # 500 - 100
    assert balances["10002"] == 400  # 300 + 100
    print("✅ Test Passed: Successful transfer")


if __name__ == "__main__":
    test_transfer_success()
