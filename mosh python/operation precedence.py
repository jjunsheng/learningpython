#order of operation multipler has a higher precedence which will be execute first
x = 10 + 3 * 2
print(x)

#order of precedence
#parenthesis
#exponentiation 2 ** 3
#multiplication or division
#addition or subtraction

x = 10 + 3 * 2 ** 2
print(x)

x = (10 + 3) * 2 ** 2
print(x)

x = (2 + 3) * 10 - 3
print(x)
