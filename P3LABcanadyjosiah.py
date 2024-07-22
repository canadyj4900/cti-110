change= float(input('Enter the amount of monry as a float:'))
if change == 0:
    print("No change needed")

num_dollars = change // 100
change = change- (num_dollars * 100)

num_quaters = change // 25
change = change - (num_quaters * 25)

num_dimes = change // 10
change = change - (num_dimes * 25)

num_nickles = change // 5
change = change - (num_nickles * 5)

num_pennies= change // 5
change = change - (num_pennies * 1)

if num_dollars>0:
    print(num_dollars, end="")
    if num_dollars == 1:
        print("dollar")
    else:
        print("dollars")
if num_quaters>0:
    print(num_quaters, end="")
    if num_dollars == 1:
        print("quater")
    else:
        print("quaters")
if num_dimes>0:
    print(num_dimes, end="")
    if num_dimes == 1:
        print("dime")
    else:
        print("dimes")
if num_nickles>0:
    print(num_nickles, end="")
    if num_nickles == 1:
        print("nickle")
    else:
        print("nickles")
if num_pennies > 0:
    print(num_pennies, end="")
    if num_pennies  == 1:
        print("pennies")
    else:
        print("pennies")
