class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name.lower() == name.lower()]
        return result

    def search_by_salary(self, condition, value):
        if condition == ">":
            result = [emp for emp in self.employees if emp.salary > value]
        elif condition == "<":
            result = [emp for emp in self.employees if emp.salary < value]
        elif condition == ">=":
            result = [emp for emp in self.employees if emp.salary >= value]
        elif condition == "<=":
            result = [emp for emp in self.employees if emp.salary <= value]
        else:
            result = []
        return result

    def print_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            print("Employee ID\tName\tAge\tSalary (PM)")
            for emp in results:
                print(f"{emp.emp_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

def main():
    table = EmployeeTable()
    table.add_employee(Employee("161E90", "Raman", 41, 56000))
    table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose a search parameter:")
    print("1. Age\n2. Name\n3. Salary (> / < / <= / >=)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter age to search: "))
        results = table.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        results = table.search_by_name(name)
    elif choice == 3:
        condition = input("Enter condition (> / < / <= / >=): ")
        value = float(input("Enter salary value: "))
        results = table.search_by_salary(condition, value)
    else:
        print("Invalid choice")
        return

    table.print_results(results)

if __name__ == "__main__":
    main()
