import csv
import pytest
from atm import check_balance


# Create a temporary users.csv file for the test
@pytest.fixture
def setup_csv(tmp_path):
    file_path = tmp_path / "users.csv"
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["PIN", "name", "balance"])
        writer.writerow(["1234", "Alice", "500"])
        writer.writerow(["5678", "Bob", "300"])
    return file_path


# Test the check_balance function
def test_check_balance(setup_csv, monkeypatch, capsys):
    # Patch the CSV path used in the function
    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: open(setup_csv, *args[1:], **kwargs))

    check_balance("1234")

    captured = capsys.readouterr()
    assert "Account balance: $500" in captured.out
