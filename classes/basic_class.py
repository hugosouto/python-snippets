class Account:
    def __init__(self, name, balance, number):
        self.name = name
        self.balance = balance
        self.number = number

input = {'name': 'Hugo Souto',
         'balance': 1000,
         'number':123456789
         }

account = Account(name=input['name'],
                  balance=input['balance'],
                  number=input['number']
                  )

print(account.name)
print(account.balance)
print(account.number)