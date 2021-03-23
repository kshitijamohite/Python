l1=[50,20,22,1,5,8,9,42,49]
l1.append(55)
l1[len(l1):]=[60]
print(l1)

l2=list(range(10,100,10))
print(l2)

l1.extend(l2)    #list=l1+l2
print(l1)

l1.remove(10)       #removes 10 from list
print(l1)

l1.insert(5,111)      #insert in list
print(l1)

l1.pop()              #last element delet hoto
print(l1)

l1.pop(3)              #delete that index cha no
print(l1)

l2.clear()          #clear the list
print(l2)

p=l1.index(20)     #show no at that index

a=l1.count(20)       #count element 20 in list

l1.sort()            #sort the list
print(l1)

l3=['ab','cl','cb']
l3.sort()
print(l3)

l1.sort(reverse=True)
print(l1)

l1.reverse()
print(l1)

l4=l1.copy()
print(l4)

lm=[[4]*2]*3
print(lm)

lm[0][0]=5  
print(lm)

l5=[10]*3
for i in range(3):
    l5[i]=[10]*2
print(l5)

l5[0][0]=20
print(l5)
