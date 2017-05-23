"""This program will allow us to deposit and withdraw $ amounts from a bank account."""

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = self
  def __repr_(self):
    return "%s's account.  Balance: $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print "Balance: $%.2f" % (self.balance)
  def deposit(self, amount):
    if amount <= 0:
      print "Cannot deposit this amount."
      return
    else:
      print "Deposit of $%.2f" % (amount)
      balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance:
      print "Cannot withdraw this amount."
      return
    else:
      print "$%.2f has been withdrawn from your account." % (amount)
      self.balance -= amount
      self.show_balance()
my_account = BankAccount("Mitchell")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
