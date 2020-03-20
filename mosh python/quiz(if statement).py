# price of house is $1M. if buyer has good credit, they need to put down 10% otherwise they need to put down 20% print the down payment

has_good_credit = True
price_of_house = 1000000
downpayment = 0

if has_good_credit:
    downpayment = price_of_house * 0.1

else:
    downpayment = price_of_house * 0.2

print(f"Down payment = ${downpayment}")