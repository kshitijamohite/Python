a= int(input("how many nos u want : "))
b=[]

for i in range(0,a):
    no = int(input("Enter nos:"))
    b.append(no)
print("\n1.Addition\n2.Subtract\n3.Multiplication\n4.Division\n5.Integer division\n6.Modulus\n7.Power\n8.Exit")
   
while 1:
    c=int(input("\nEnter choice"))
    if (c==1):
        sum = b[0]
        for no in range (1 ,len(b)):
            sum = sum + b[no]
        print("Sum of is : ", sum)

    elif (c==2):
         diff = b[0]
         for no in range (1,len(b)):
             diff = diff - b[no]
         print("Subtraction is : ", diff)
 
    elif (c==3):
        mul = b[0]
        for no in range (1,len(b)):
            mul = mul * b[no]
        print("Multiplication is : ", mul)

    elif (c==4):
        div = b[0]
        for no in range (1,len(b)):
            div = div / b[no]
        print("Division is : ", div)

    elif (c==5):
        idiv = b[0]
        for no in range (1,len(b)):
            idiv = idiv // b[no] 
        print("Division is : ", idiv)
   
    elif (c==6):
        modulus = b[0]
        for no in range (1,len(b)):
            modulus = modulus % b[no]
        print("Modulus is : ", modulus)


    elif (c==7):
        power= b[0]
        for no in range (1,len(b)):
            power=power**b[no]
        
        print("Power is : ", power)
    
    elif (c==8):
        break
