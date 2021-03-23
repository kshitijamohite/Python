x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

a=int(input('Enter no to perform : 1.Addition 2.Subtraction 3.Multipication 4.Division 5.Integer_division 6.Power 7.Modulus'))
            
if (a==1):
    print('Addition is :',x+y)

elif (a==2):
    print('Subtraction is :',x-y)
    
elif(a==3):
    print('Multiplication is :',x*y)
    
elif(a==4):
    print("Division is :",x/y)

elif(a==5):
     print('Integer division is :',x//y)

elif(a==6):
    print('Power is :',x**y)

elif(a==7):
    print('Modulus is :',x%y)

elif(a>7):
    print('incorrect choice')
