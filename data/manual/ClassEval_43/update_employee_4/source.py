class HRManagementSystem:
    def update_employee(employee_id, new_info):
        # Retrieve the employee from the HRManagementSystem using the employee_id
        employee = HRManagementSystem.get_employee(employee_id)
        
        # Update the employee's information with the new_info
        employee.update(new_info)
        
        # Save the updated employee back to the HRManagementSystem
        HRManagementSystem.save_employee(employee)