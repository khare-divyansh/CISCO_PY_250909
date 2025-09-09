empolyees = [] # list
# create employee
employee = ('Bhanu', 22,  50000, True) 
empolyees.append(employee)


employee = ('Mahesh', 22,  50000, True) 
empolyees.append(employee)

employee = ('Vaishnavi', 22,  50000, True) 
empolyees.append(employee)

print('after add all employees:',empolyees)

# search employee
I = 0
search = 'Vaishnavi'
index = -1

for emp in empolyees:
    if emp[0] == search:
        Index = I
        break
    I += 1

if index == -1:
    print('Employee not found')
else:
    search_employee = empolyees[index]
    print(search_employee)
    salary = float(input("Salary: "))
    employee = (search_employee[0], search_employee[1], salary, search_employee[3])
    empolyees[index] = employee
print('after search and update : ', empolyees)

employee = ('Dravd', 50, 200.75, True)
empolyees.append(employee)
print('After add dravid', empolyees)
empolyees.pop()# delete last elem
print('after delete dravid:', empolyees)#[hanu, mahesh, vaisnavi]

# delete employee Mahesh by osition
position = 1
empolyees.pop(position)# delete last 
print('after delete Mahesh: ',empolyees)
