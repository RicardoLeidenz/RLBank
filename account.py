class Account:
    def __init__(self, account_number: int, name: str, initial_deposit: float = 0.0):
        """
        Initialize a new Bank Account
        :param name: Name associated with the account
        :type name: str
        :param initial_deposit: Amount of the initial balance in the account
        "type initial_deposit: float
        """
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit

    def __str__(self):
        """Prints the name and balance associated with the account"""
        account_number = self.account_number
        last,first = self.name.split(",")
        balance = self.balance
        return f"Account Number: {account_number}\nName: {first} {last}\nBalance: ${balance:,.2f}\n"

    @property
    def account_number(self) -> int:
        """Getter for account number"""
        return self._account_number

    @account_number.setter
    def account_number(self, account_number : int) -> None:
        """Setter for balance"""
        self._account_number = account_number

    @property
    def name(self) -> str:
        """Getter for name"""
        return self._name

    @name.setter
    def name(self, name : str) -> None:
        """Setter for name"""
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def balance(self) -> float:
        """Getter for balance"""
        return self._balance

    @balance.setter
    def balance(self, balance : float) -> None:
        """Setter for balance"""
        self._balance = balance
