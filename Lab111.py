#write a program to create a class Employee to id,name,age,email,phone
import time
class Employee:
    empId = None
    empName = None
    empAge = None
    empEmail = None
    empPhone = None
    empAddress = None


    def __init__(self, id, name,age,email,phone,address):
        self.empId = id
        self.empName = name
        self.empAge = age
        self.empEmail = email
        self.empPhone = phone
        self.empAddress = address


    def print_employe(self):

        print(f"Employee Id is:\t{self.empId}")
        print(f"Employee Name is:\t{self.empName}")
        print(f"Employee Age is:\t{self.empAge}")
        print(f"Employee Email is:\t{self.empEmail}")
        print(f"Employee PhoneNumber is:\t{self.empPhone}")
        print(f"Employee Address is:\t{self.empAddress}")


emp_id = input("EmployeeId is:\t")
name = input("Employee Name:\t")
age = int(input("Employee Age:\t"))
email = input("Employee EmailId:\t")
phone = input("Employee PhoneNum:\t")
address = input("Employee Address:\t")

time.sleep(6)
E1 = Employee(emp_id,name,age,email,phone, address)
print(E1.print_employe())

emp_id = input("EmployeeId is:\t")
name = input("Employee Name:\t")
age = int(input("Employee Age:\t"))
email = input("Employee EmailId:\t")
phone = input("Employee PhoneNum:\t")
address = input("Employee Address:\t")

E2 = Employee(emp_id,name,age,email,phone, address)
print(E2.print_employe())
