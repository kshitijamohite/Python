
no = int(input('Enter no until which u want prime nos to be displayed: '))
j=2
while(j<=no):
        count=0
        i = 2
        while(i<=j//2):
           if(j%i==0):
              count=count+1
              break
           i=i+1
        if(count==0):
           print("%d"%j)
        j=j+1
