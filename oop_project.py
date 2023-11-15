from bank_accounts import *

Aryan = BankAccount(1000, "Aryan")
Poornima = BankAccount(2000, "Poornima")

############################################
Aryan.getBalance()
Poornima.getBalance()

#####################################
Poornima.deposit(500)
###################################\
Aryan.withdraw(10000)
Aryan.withdraw(10)
####################################
Aryan.transfer(100000, Poornima)
Aryan.transfer(100, Poornima)

#######################################
Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.getBalance()
Jim.transfer(100, Aryan)
##########################################

