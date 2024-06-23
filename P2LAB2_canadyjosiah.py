dict1={'Camaro':18.21,'Prius':52.36,'Model S':110,'Silverado':26}
print(dict1.keys())
print('')
def search_dict1():
    key = input ('Enter a vehicle to see its mpg:')
    print('')
    if key in dict1:
        print( 'The' , key ,'gets' ,dict1[key], 'mpg')
        print('')
        miles= int(input(f'how many miles will you drives the {key}?'))
        print('')
        x=dict1[key]
        y=miles
        z=(y/x)
        
        p= round(z,2)
        
        print(p, 'gallon(s) of gas are needed to drive the' ,key, y , 'miles.')

    else:
        print('name not found')
search_dict1()
