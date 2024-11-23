class HRManagementSystem:
    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns False.
        """
        if employee_id in self.employees:
            return self.employees[employee_id]
        else:
            return False