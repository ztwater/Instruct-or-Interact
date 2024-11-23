class HRManagementSystem:
    def update_employee(self, employee_id: int, employee_info: dict):
        """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: The employee's information, dict.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        if employee_id in self.employees:
            # Retrieve the employee from the HRManagementSystem using the employee_id
            employee = self.get_employee(employee_id)
            
            # Update the employee's information with the new_info
            employee.update(employee_info)
            
            # Save the updated employee back to the HRManagementSystem
            self.save_employee(employee)
            
            return True
        else:
            return False