"""
Name: Ng Tsz Yin
Class: 4B
Class no.: 12

Else - Exercise
"""

oprice = float(input("Please input the total price before discount: "))

if oprice >= 150:
    price = oprice * 0.8
elif oprice >= 100:
    price = oprice * 0.9
elif oprice >= 50:
    price = oprice * 0.95
else:
    price = oprice

print(price)




