# Text-Based Banking System

## Overview
This project is a **text-based banking system** that uses an interactive, menu-driven approach to manage accounts, transactions, and administrative operations.

Key features include:
- **Account Management**: Accounts are stored as instances of a user-defined class, keyed by account numbers in a dictionary.
- **Account Number Assignment**: Each new account is automatically assigned a unique, randomly generated 8-digit account number.
- **Account Types**: Supports two types of accounts — Savings (S) and Current (C).
- **Single System**: Accessible by both users and bank admins, with admin access protected by a hard-coded password (modifiable by admins, initially set to 1234).

### User Features
Users can:
- Create an account.
- Check their account balance.
- Deposit or withdraw funds.
- Transfer funds to another account.

### Admin Features
Admins can:
- Change the admin password.
- Create multiple accounts at once using a CSV or text file with comma-separated values.
- Export account registries to a CSV file.
- Delete user accounts.

---

## Input & Export CSV Formats

### Input CSV Format (for mass account creation):
| Name            | Opening Balance | Account Type (S/C) |
|------------------|-----------------|---------------------|
| Alice Johnson    | 1000            | S                  |
| Bob Smith        | 2000            | C                  |

### Export CSV Format (for account registries):
| Account Number | Name            | Balance | Account Type         |
|----------------|-----------------|---------|----------------------|
| 12345678       | Alice Johnson   | 1000    | Savings Account      |
| 87654321       | Bob Smith       | 2000    | Current Account      |

---

## Testing
The program has been tested for:
- Account creation (both individual and mass creation using CSV files).
- Deposits, withdrawals, and transfers.
- Admin operations like password changes, account deletions, and data export.

### Test Files
- **`Account_Data.csv`**: A sample input CSV file for mass account creation.
- **`Registry_CSV.csv`**: The output file generated during account registry export.


