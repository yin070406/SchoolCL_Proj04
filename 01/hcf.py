num1 = int(input("Number01: "))
num2 = int(input("Number02: "))

if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller+1):
    if (num1%i == 0) and (num2%i == 0):
        hcf = i

print(hcf)
