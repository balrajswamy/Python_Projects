#write a program to create a class Employee to store empId,name,age,email,phone

class Employee:
    empId = None
    empName = None
    empAge = None
    empEmail = None
    empPhone = None
    empAddress = None
    empData = []

    def __init__(self, id, name,age,email,phone,address):
        self.empId = id
        self.empName = name
        self.empAge = age
        self.empEmail = email
        self.empPhone = phone
        self.empAddress = address


    def store_record(self):
        self.empRecord = [self.empId,self.empName,self.empAge,self.empEmail,self.empPhone,self.empAddress]
        self.empData.append(self.empRecord)

        return self.empData

#creating an object

prompt = "\n1. Please enter the  values for the Name, Age, Email, Phone, Address fields:"
prompt += "\n2. Enter '1 for add record or enter 2 to exit':\t "
i = 0
while True:
    i = i+1
    addrecord = input(prompt)

    if addrecord == "2":
        print("You have asked to exit the Program!, Thanks!!!")
        break
    else:
        emp_id = i
        name = input("Employee Name:\t")
        age = int(input("Employee Age:\t"))
        email = input("Employee EmailId:\t")
        phone = input("Employee PhoneNum:\t")
        address = input("Employee Address:\t")

        e1 = Employee(emp_id,name,age,email,phone, address)
        print(e1.store_record())



