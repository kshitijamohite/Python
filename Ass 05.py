
def add(list1):
    sum = list1[0]
    elem = 1
    while (elem < len(list1)):
        sum = sum + list1[elem]
        elem += 1
    print("Sum of given numbers : ", sum)


def sub(list1):
    diff = list1[0]
    elem = 1
    while (elem < len(list1)):
        diff = diff - list1[elem]
        elem += 1
    print("Subtraction of given numbers : ", diff)


def mul(list1):
    mul = list1[0]
    elem = 1
    while (elem < len(list1)):
        mul = mul * list1[elem]
        elem += 1
    print("Multiplication of given numbers : ", mul)

def div(list1):
    div = list1[0]
    elem = 1
    while (elem < len(list1)):
        div = div / list1[elem]
        elem += 1
    print("Division of given numbers : ",div )

def idiv(list1):
    idiv = list1[0]
    elem = 1
    while (elem < len(list1)):
        idiv = idiv// list1[elem]
        elem += 1
    print("Integer division of given numbers : ", idiv)

def power(list1):
    power = list1[0]
    elem = 1
    while (elem < len(list1)):
        power = power ** list1[elem]
        elem += 1
    print("Power of given numbers : ", power)

def  modulus(list1):
    modulus = list1[0]
    elem = 1
    while (elem < len(list1)):
        modulus = modulus % list1[elem]
        elem += 1
    print("Modulus of given numbers : ", modulus)
    
if __name__ == "__main__":
    count=int(input('how many no:'))
    list=[]
    for i in range(0,count):
        elem=int(input('enter no:'))
        list.append(elem)
    print(list)    
    add(list)
    sub(list)
    mul(list)
    div(list)
    idiv(list)
    power(list)
    modulus(list)
