from forex_python.converter import currencyRates
c = currencyRates()
amount = int(input("Enter Amount: "))
from_currency =  input("From currency: ").upper()
to_currency = input("To cureency: ").upper
print(from_currency, " To ", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)
