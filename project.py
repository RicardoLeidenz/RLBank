import csv
import os
import sys
import requests
from account import Account
from bank import Bank

# Menu functions

def welcome_menu(bank: type[Bank]) -> None:
    """
    Starts the program with a welcome menu and asks if the user already has an account or if they'd like to create one

    :param bank: Bank from which to save all client information into 'bank.csv'
    :type bank: Bank
    """
    while True:
        try:
            print("#---------------------#")
            print("#  Welcome to RLBank  #")
            print("#---------------------#")
            selection = input("1. Existing client\n2. New client\n3. Exit\nSelect option: ")
            match selection:

                # If client already has an account we find it
                case "1":
                    os.system("clear")
                    account = fetch_account(bank)

                # If new client we create a new client and add it to the bank
                case "2":
                    first = input("Please enter your first name: ").capitalize()
                    last = input("Please enter your last name: ").capitalize()
                    while True:
                        initial_deposit = float(input("Please enter the amount of your initial deposit: $"))
                        if (initial_deposit > 0):
                            break
                        else:
                            os.system("clear")
                            print("Please enter a valid number")
                    name = last + "," + first
                    # Create a new account with the information given and add it to the banks clients list
                    account = Account(len(bank.clients) + 1, name, initial_deposit)
                    bank.clients.append(account)

                case "3":
                    sys.exit()

                case _:
                    raise ValueError

            save_bank(bank)
            main_menu(bank,account)

        except ValueError:
            os.system("clear")
            print("Please enter a valid option")

def main_menu(bank: type[Bank], account: type[Account]) -> None:
    """
    Gives the client options for transactions and processes them
    :param bank: Bank to which load all client information saved in 'bank.csv'
    :type bank: Bank
    :param account: The account that's activating the transaction
    :type account: Account

    """
    # Match the account to the one in the banks client list
    for client in bank.clients:
        if client == account:
            os.system("clear")
            while True:
                try:
                    # Ask what type of transaction is going to be started
                    print(f"{client}\n1. Make a deposit\n2. Withdraw money\n3. Transfer Money\n4. Exit")
                    selection = input("Select option: ")
                    match selection:

                        # Deposit
                        case "1":
                            os.system("clear")
                            while True:
                                try:
                                    # Show the account and request deposit type
                                    print(client)
                                    selection = input("What would you like to deposit?\n1. Cash\n2. Crypto\nSelect option: ")
                                    match selection:

                                        # Deposit in cash
                                        case "1":
                                            os.system("clear")
                                            print(client)
                                            amount = float(input("Enter amount to deposit: "))

                                        # Deposit in crypto
                                        case "2":
                                            os.system("clear")
                                            # Request type of coin to exchange
                                            selection = input("Select a coin to exchange:\n1. Bitcoin\n2. Ethereum\n3. Solana\n4. Dogecoin\nSelect option: ")
                                            # Request amount of coins to exchange
                                            how_many = float(input("Enter amount of coins to exchange: "))
                                            os.system("clear")
                                            print(client)
                                            match selection:

                                                # Exchange amount into Bitcoin
                                                case "1":
                                                    amount = exchange("Bitcoin",how_many)

                                                # Exchange amount into Ethereum
                                                case "2":
                                                    amount = exchange("Ethereum",how_many)

                                                # Exchange amount into Solana
                                                case "3":
                                                    amount = exchange("Solana",how_many)

                                                # Exchange amount into Dogecoin
                                                case "4":
                                                    amount = exchange("Dogecoin",how_many)

                                                case _:
                                                    raise ValueError

                                        case _:
                                            raise ValueError

                                    deposit(client,amount)
                                    print(f"\nNew balance: ${client.balance:,.2f}")
                                    break

                                except ValueError:
                                    os.system("clear")
                                    print("Please enter a valid number\n")
                                    pass

                        # Withdraw
                        case "2":
                            os.system("clear")
                            while True:
                                try:
                                    print(client)
                                    # Request amount to withdraw
                                    amount = float(input("Enter amount to withdraw: "))
                                    if (client.balance >= amount):
                                        withdraw(client,amount)
                                        print(f"\nNew balance: ${client.balance:,.2f}")
                                        break
                                    else:
                                        os.system("clear")
                                        print("Balance insufficient for transaction, please try again\n")
                                        pass

                                except ValueError:
                                    os.system("clear")
                                    print("Please enter a valid number\n")
                                    pass

                        # Transfer
                        case "3":
                            os.system("clear")
                            print("Who would you like to transfer the money to?\n")
                            account_2 = fetch_account(bank)
                            for client_2 in bank.clients:
                                if client_2 == account_2:
                                    while True:
                                        os.system("clear")
                                        print(client)
                                        amount = float(input("Enter transfer amount: "))
                                        if (client.balance >= amount):
                                            transfer(client,client_2, amount)
                                            print(f"\nNew balance: ${client.balance:,.2f}")
                                            break
                                        else:
                                            os.system("clear")
                                            print("Balance insufficient for transaction, please try again\n")
                                            pass
                        case "4":
                            sys.exit()

                        case _:
                            raise ValueError

                    save_bank(bank)
                    what_now(bank,client)

                except ValueError:
                    os.system("clear")
                    print("Please enter a valid number\n")
                    pass

# Load and save functions

def load_bank(bank: type[Bank]) -> None:
    """
    Load all Accounts saved in 'bank.csv' into a bank

    :param bank: Bank to which load all client information saved in 'bank.csv'
    :type bank: Bank
    """
    clients_list = []
    with open("bank.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Save every account number, name and balance for each client
            number = int(row["Account number"])
            name = row["Name"]
            balance = float(row["Balance"].replace(',', ''))
            # Asign them to a new Account
            account = Account(number, name, balance)
            # Add the account to the banks client list
            clients_list.append(account)
        bank.clients = clients_list

def save_bank(bank: type[Bank]) -> None:
    """
    Save all clients in Bank into 'bank.csv'

    :param bank: Bank from which to save all client information into 'bank.csv'
    :type bank: Bank
    """
    with open("bank.csv", "w") as file:
        file.write("Account number,Name,Balance\n")
        for client in bank.clients:
            writer = csv.DictWriter(file, fieldnames=["Account number","Name", "Balance"])
            writer.writerow({"Account number": client.account_number,"Name": client.name, "Balance": round(client.balance, 2)})

# Transaction functions

def deposit(account: type[Account], amount: float) -> None:
        """
        Deposit 'amount' from the account

        :param amount: Amount to deposit
        :type amount: float

        """
        account.balance += amount

def withdraw(account: type[Account], amount: float) -> None:
    """
    Withdraw 'amount' from the account

    :param amount: Amount to withdraw
    :type amount: float


    """
    if account.balance < amount:
        raise ValueError("You broke")
    account.balance -= amount

def transfer(account: type[Account],other: type[Account], amount: float) -> None:
    """
    Withdraw 'amount' from the account and deposits it into 'other'

    :param other: Account which to transfer
    :type other: Account
    :param amount: Amount to transfer
    :type amount: float

    """
    withdraw(account,amount)
    deposit(other,amount)

# Other functions

def exchange(coin: str,amount: float) -> float:
    """
    Exchange 'amount' based on 'coin' price

    :param coin: Crypto to exchange
    :param amount: Amount to exchange
    :return: A string with the amount of $ the coins are worth
    :rtype: str
    """
    match coin:

        case "Bitcoin":
            response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,CNY,JPY,GBP")

        case "Ethereum":
            response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,CNY,JPY,GBP")

        case "Solana":
            response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD,EUR,CNY,JPY,GBP")

        case "Dogecoin":
            response = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR,CNY,JPY,GBP")

    c = response.json()
    rate = float(c["USD"])
    total = amount * rate
    print(f"{amount} {coin} = ${total:,.2f}")
    return total

def what_now(bank: type[Bank], account: type[Account]) -> None:
    """
    Asks the user if they'd like to exit or continue with a new transaction

    :param bank: Bank from which to save all client information into 'bank.csv'
    :type bank: Bank
    """
    while True:
        try:
            selection = input("\n1. Start new transaction\n2. Exit\nSelect option: ")
            match selection:

                case "1":
                    main_menu(bank,account)

                case "2":
                    sys.exit()

                case _:
                    raise ValueError

        except ValueError:
                os.system("clear")
                print ("Please enter a valid option")


def fetch_account(bank: type[Bank]) -> Account:
    """
    Returns an account the user searches by account number or  name

    :param bank: Bank to which load all client information saved in 'bank.csv'
    :type bank: Bank
    :return: A bank account
    :rtype: Account
    """
    while(True):
        try:
            print("Find account by:\n1. Account number\n2. Name\n\nB. Go back")
            how = input("Selection: ").upper()
            os.system("clear")
            match how:

                case "1":
                    account_number = int(input("Enter account number: ").strip())
                    for client in bank.clients:
                        if client.account_number == account_number:
                            os.system("clear")
                            return client
                    os.system("clear")
                    print("Account not found, please try again.")
                    pass

                case "2":
                    first = input("First name: ").strip().capitalize()
                    last = input("Last name: ").strip().capitalize()
                    name = f"{last},{first}"
                    for client in bank.clients:
                        if client.name == name:
                            os.system("clear")
                            return client
                    os.system("clear")
                    print("Client not found, please try again.")
                    pass

                case "B":
                    os.system("clear")
                    return None

                case _:
                    pass

        except ValueError:
            os.system("clear")
            print("Wrong input")

def main():
    bank = Bank()
    load_bank(bank)
    os.system("clear")
    welcome_menu(bank)

if __name__ == "__main__":
    main()
