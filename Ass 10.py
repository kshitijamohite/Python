## 1.create dictionary
employees = {
             'E0001' : ('Rachel Peters','Vice President'),
             'E0002' : ('Preeti Patil','Admin'),
             'E0003' : ('Fatima Kachwala Associate','Marketing'),
             'E0004' : ('James Peterson','Sales Engineer'),
             'E0005' : ('Satya Subramanian','Director')
            }
print(employees)

## 2. update dictionary
emp1 = {'E0006' : ('Ram Ratan','Director')}
employees.update(emp1)
emp2 = {'E0007' : ('Ganesh Kolhe','President')}
employees.update(emp2)
print(employees)
## OR
employees['E0006']=('Ram Ratan','Director')
employees['E0007']=('Ganesh Kolhe','President')
print(employees)

## 3.
for designation in employees.values():
    if designation[1] == 'Director':
        print(designation[0])


## 4.
employees = { 'E0001' : {'name' : 'Rachel Peters', 'Designation' : 'Vice President'},
              'E0002' : {'name' : 'Preeti Patil', 'Designation' : 'Admin'},
              'E0003' : {'name' : 'Fatima Kachwala Associate','Designation':'Marketing'},
              'E0004' : {'name' : 'James Peterson','Designation':'Sales Engineer'},
              'E0005' : {'name' : 'Satya Subramanian','Designation':'Director'}
            }
print(employees)

## 5.

for designation in employees.values():
    print(designation)
