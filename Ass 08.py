import ass07
print('\n\n\nArea of shapes\n\t1.circle\n\t2.square\n\t3.rectangle\n\t4.exit')
while 1:
    ch=int(input('enter choice'))
    if(ch==1):
        r=int(input('enter radius'))
        ass07.circle(r)
    elif(ch==2):
        l=int(input('enter length'))
        ass07.square(l)
    elif(ch==3):
        len=int(input('enter length'))
        bre=int(input('enter breadth'))
        ass07.rectangle(len,bre)
    elif(ch==4):
        break
     
