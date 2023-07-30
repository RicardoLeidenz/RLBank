# RL Bank

#### Video Demo:  <https://youtu.be/gHUMp_b-0qI>

#### Description:

RL Bank is a simple banking system in which you can:
1. Create a new account.
2. Access an existing account.
3. Make a deposit in cash or crypto.
4. Withdraw money.
5. Transfer money from one account into another.

The bank automatically:
1. Loads and saves information.
2. Exchanges any cryptocurrency you want to deposit into your account to USD.

- "bank.py" handles the Bank class which saves a list of clients.

- "account.py" handles the Account class which saves an account number, name of the client and the balance on the account.

- "project.py" is the main file which handles all the bank menus and transactions.

- "test_project.py" tests all functions that can be testes by using pytest.

- "bank.csv" saves all the clients in the bank.
