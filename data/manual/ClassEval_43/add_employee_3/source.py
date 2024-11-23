class HRManagementSystem:
    def add_employee(name, age, position):
        # Code to add the employee to the HRManagementSystem
        # You can use a database or a list to store the employee information
        
        # Example implementation using a list
        employee = {
            'name': name,
            'age': age,
            'position': position
        }
        employees.append(employee)
        
        # Optionally, you can return a success message or the updated list of employees
        return "Employee added successfully!"