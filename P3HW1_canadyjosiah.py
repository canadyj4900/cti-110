a=float(input('Enter grade for Module 1:'))
b=float(input('Enter grade for Module 2:'))
c=float(input('Enter grade for Module 3:'))
d=float(input('Enter grade for Module 4:'))
e=float(input('Enter grade for Module 5:'))
f=float(input('Enter grade for Module 6:'))
print('')
print('------------Results------------')
grade_list=[a,b,c,d,e,f]
list_min=min(grade_list)
print(f"Lowest Grade: {list_min}")
list_max=max(grade_list)
print(f"Highest Grade: {list_max}")
list_sum=sum(grade_list)
print(f"Sum of Grades: {list_sum}")
x=(a+b+c+d+e+f)
y=(x/6)
print("Sum of Grades:",end="")
print(f'{y:.2f}')
print('-------------------------------')
print("Your grade is:",end="")
if y==100:
    print("A")
if y==0:
    print("F")
if 89<y<100:
    print('A')
if 79<y<80:
    print('B')
if 69<y<70:
    print('C')
if 59<y<60:
    print('D')
if 0<y<59:
    print('F')
