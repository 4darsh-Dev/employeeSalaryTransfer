# A simple program for fetching User Details and Paying their Salary 
import random

class Employee:
    """Class for Getting information about the Employee and his salary"""
    salary = 120000
  
    def getInfo(self, first_name, last_name, age):
        # provides the details of the user
        first_name = first_name.title()
        last_name = last_name.title()
        self.first = first_name
        self.last = last_name
        self.age = age
        full_name = f"\n\tName : {self.first} {self.last}"
        print(full_name)
        print(f"\tAge : {self.age}")
       
        print(f"\tEmployee Id : {employeeId}")
        

    def getSalary(self, increment):
        # for getting totalSalry along with salary bonus
        totalSalary = self.salary + increment 
        self.totalSalary = totalSalary
        print(f"\n\tYour Total Salary is {self.totalSalary}")

    payment = False 
    def getPayment(self):
        # for transferring payment to the Employee's A/c
        if self.payment == False:
            print("\n\tProcessing Payemnt....")
            print("\tTransaction Successfull! ")
            rand = random.randint(3522352323,4000832880)
            print(f"\tTranscation Id : {rand}")
            print(f"\tDear {self.first},\n\t\t {self.totalSalary} deposited to your Bank A/c ************9853 kindly check your A/c balance ")
            self.payment = True
        else:
            print(f"\n\tDear {self.first},\n\t\tSalary had been already deposited to your Bank A/c ************9853 !")


    @staticmethod
    # a simple greet method 
    def greetFareWell():
        print('\tThanks for visiting Us!')



if __name__ == "__main__":
    employee1 = Employee()

    while(True):
        welcomeMsg = '''\n======= Welcome to The adWebSolutions.com =======
        Please Choose an option :-
        1. Get Info
        2. Get Salary Details
        3. Get Payment
        4. Exit 
        '''
        print(welcomeMsg)
        a = int(input("Enter a Choice : "))
        if a == 1:
            try:
                first_name = input('Enter your first name : ')
                last_name = input('Enter your last name : ')
                age = int(input('Enter your Age : '))
                
                employeeId = int(input("Enter Employee Id : "))
                print("\n\tVerifying Employee....")
                print("\tPlease wait...")
                print("\tVerified Successfully! ")
            except:
                print("\tInvalid Employee Id!")

            employee1.getInfo(first_name, last_name, age)
        elif a == 2:
            try:
                
                bonus = int(input("Enter Employee bonus : "))
                employee1.getSalary(bonus)
            except :
                print("Invalid Input")
            
        elif a == 3:
            employee1.getPayment()
        elif a == 4:
            employee1.greetFareWell()
            exit()
        else:
            print("Invalid Choice! ")


    