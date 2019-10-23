

cus_dict = {}


def add_cust(id,name,age,salary):
    cus_dict.update({id:[name,age,salary]})
    return

def search_cust(id):
    cus = cus_dict[id]
    return cus

def delete_cus(id):
    cus_del = cus_dict.pop(id)
    return cus_del

def updateCustomer(id,name,age,salary):
    cus_dict[id][0]= name
    cus_dict[id][1] = age
    cus_dict[id][2] = salary
    #cusDict.update({id:[age,name]})






print('WELCOME TO MY CUSTOMER MANAGEMENT SYSTEM')
while True:
    print('1. ADD CUSTOMER \n 2. SEARCH CUSTOMER \n 3. DELETE CUSTOMER \n 4. MODIFY CUSTOMER '
          '\n 5. DISPLAY ALL CUSTOMER')

    choice = input('ENTER YOUR CHOICE: ')
    if choice == '1':
        id = int(input('enter the customer id: '))
        name = input('enter the customer name: ')
        age = int(input('enter the customer age: '))
        salary = int(input('enter the customer salary: '))
        add_cust(id,name,age,salary)
        print('CUSTOMER DETAILS ID ADDED SUCCESSFULLY')

    elif choice == '2':
        id = int(input('enter the customer id which you wants to search:  '))
        cus = search_cust(id)

        print('cust ID:',id,'cus Name:',cus[0],'cus Age:',cus[1],'cus Salary:',cus[2])


    elif choice == '3':
        id = int(input('enter the customer id for delete any id: '))
        cus_del = delete_cus(id)
        print('customer details is deleted successfully')

    elif choice == '4':
        id = int(input('enter the customer id which you wants to modify: '))
        name = input('enter the update name: ')
        age = int(input('enter the customer update age: '))
        salary = int(input('enter the customer update salary: '))
        updateCustomer(id,name,age,salary)
        print('Customer details is modified successfully')

    elif choice == '5':
        for key,value in cus_dict.items():
            print('cusId:',key,'cus Name:',value[0],'cus Age:',value[1],'cus Salary:',value[2])
