class Employee:
    def __init__(self, emp_id, emp_name, emp_designation, experience, age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_designation = emp_designation
        self.experience = experience
        self.age = age

    def displayDetails(self):
        print("\n--- Employee Details ---")
        print(f"ID          : {self.emp_id}")
        print(f"Name        : {self.emp_name}")
        print(f"Designation : {self.emp_designation}")
        print(f"Experience  : {self.experience} years")
        print(f"Age         : {self.age}")

    def calculateSalary(self, basic):
        multiplier = 1.0  # Default multiplier

        if self.age < 30 and self.experience >= 5:
            multiplier = 1.5
        elif self.age < 40 and self.experience >= 10:
            multiplier = 2.0
        elif self.age < 40 and self.experience >= 5:
            multiplier = 1.75
        elif self.age < 50 and self.experience >= 25:
            multiplier = 2.5
        elif self.age < 50 and self.experience >= 20:
            multiplier = 2.25
        elif self.age < 58 and self.experience >= 30:
            multiplier = 3.0

        salary = basic * multiplier
        print(f"Calculated Salary (basic ₹{basic}): ₹{salary}")
        return salary


# Function to add an employee from user input
def addEmployee():
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_designation = input("Enter Designation: ")
    experience = int(input("Enter Experience (in years): "))
    age = int(input("Enter Age: "))
    basic = float(input("Enter Basic Salary: "))

    emp = Employee(emp_id, emp_name, emp_designation, experience, age)
    emp.displayDetails()
    emp.calculateSalary(basic)


# Simulating for multiple employees
def simulate():
    print("Add Employee 1:")
    emp1 = Employee("E101", "Ravi Kumar", "Manager", 6, 28)
    emp1.displayDetails()
    emp1.calculateSalary(40000)

    print("\nAdd Employee 2:")
    emp2 = Employee("E102", "Anita Mehra", "Senior Developer", 12, 39)
    emp2.displayDetails()
    emp2.calculateSalary(50000)

    print("\nAdd Employee 3:")
    emp3 = Employee("E103", "Sunil Joshi", "Project Lead", 26, 48)
    emp3.displayDetails()
    emp3.calculateSalary(60000)

    print("\nAdd Employee 4 (User Input):")
    addEmployee()


# Run the simulation
if __name__ == "__main__":
    simulate()
