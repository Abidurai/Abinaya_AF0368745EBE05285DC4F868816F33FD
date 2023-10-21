   #Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.

def sort_students(students):
    students.sort(key=lambda student: student.cgpa, reverse=True)
  
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

students = [
    Student("John", "A001", 3.8),
    Student("Jane", "A002", 3.5),
    Student("Alice", "A003", 3.9),
    Student("Bob", "A004", 3.2),
]

sort_students(students)

for student in students:
    print(student.name, student.roll_number, student.cgpa)#- Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        return self.__account_balance
      # Create an instance of BankAccount
account = BankAccount("1234567890", "John Doe", 1000)

# Test deposit functionality
account.deposit(500)
print("Current balance:", account.display_balance()) 

# Test withdrawal functionality
account.withdraw(200)
print("Current balance:", account.display_balance())  

account.withdraw(2000)   

print("Current balance:", account.display_balance())