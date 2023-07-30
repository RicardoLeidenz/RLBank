import project
from project import Bank
from account import Account

# Project tests
def test_load_bank():
    b1 = Bank()
    project.load_bank(b1)
    assert b1.clients != None
    b2 = Bank()
    project.load_bank(b2)
    assert b2.clients != None

def test_exchange():
    assert project.exchange("Bitcoin",2) != 0
    assert project.exchange("Ethereum",12) != 0
    assert project.exchange("Solana",6) != 0
    assert project.exchange("Dogecoin",5) != 0

def test_deposit():
    account1 = Account(1,"Leidenz,Ricardo",100)
    project.deposit(account1,500)
    assert account1.balance == 600
    account2 = Account(2,"Casanova,Grecia",500)
    project.deposit(account2,500)
    assert account2.balance == 1000

def test_withdraw():
    account1 = Account(1,"Leidenz,Ricardo",1000)
    project.withdraw(account1,500)
    assert account1.balance == 500
    account2 = Account(2,"Casanova,Grecia",5000)
    project.withdraw(account2,500)
    assert account2.balance == 4500

def test_transfer():
    account1 = Account(1,"Leidenz,Ricardo",1000)
    account2 = Account(2,"Casanova,Grecia",5000)
    project.transfer(account1,account2,300)
    assert account1.balance == 700
    assert account2.balance == 5300

# Bank tests
def test_bank():
    b1 = Bank()
    assert b1 != None
    b2 = Bank()
    assert b2 != None
    b3 = Bank()
    assert b3 != None

# Account tests
def test_account():
    account1 = Account(1,"Leidenz,Ricardo",100)
    assert account1 != None
    account2 = Account(2,"Casanova,Grecia",500)
    assert account2 != None
