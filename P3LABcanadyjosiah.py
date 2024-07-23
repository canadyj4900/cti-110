change= float(input('Enter the amount of monry as a float:'))
if change == 0:
    print("No change needed")

num_dollars = change / 100
x = change - (num_dollars * 100)
a= num_dollars * 100


num_quaters = change / 25
y = change - (num_quaters * 25)
s= num_quaters

num_dimes = change / 10
z = change - (num_dimes * 25)

num_nickles = change / 5
c = change - (num_nickles * 5)

num_pennies= change / 5
v = change - (num_pennies * 1)

if a > 0:
    print(f'{a:.0f}', end="")
    if a == 1:
        print(" dollar")
    else:
        print(" dollars")


if s > 0:
    print(f'{s:.0f}', end="")
    if s == 1:
        print(" quater")
    else:
        print(" quaters")


if num_dimes > 0:
    print(num_dimes, end="")
    if num_dimes == 1:
        print(" dime")
    else:
        print(" dimes")


if num_nickles > 0:
    print(num_nickles, end="")
    if num_nickles == 1:
        print(" nickle")
    else:
        print(" nickles")
 

if num_pennies > 0:
    print(num_pennies, end="")
    if num_pennies  == 1:
        print(" pennies")
    else:
        print(" pennies")
