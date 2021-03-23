list = [(30,40,50), (12,24,36), (30,60,90)]
print([tup[:-1] + (100,) for tup in list])


books = [('Atlas Shrugged', '1005'), ('Black Swan', 2001), ('Sapiens', 999)]
print( sorted(books, key=lambda x: int(x[1]), reverse=False))


def sort_tuple(books):  
    return(sorted(books, key = lambda x: int(x[1])))   
books = [('Atlas Shrugged', '1005'), ('Black Swan', 2001), ('Sapiens', 999)] 
print(sort_tuple(books))


def lcm(tup):
   if tup[0] > tup[1]:
       greaterno = tup[0]
   else:
       greaterno = tup[1]
   while(True):
       if((greaterno % tup[0] == 0) and (greaterno % tup[1] == 0)):
           lcm = greaterno
           break
       greaterno = greaterno + 1

   return lcm
tup =[24,54]
print("the L.C.M is ",lcm(tup))

