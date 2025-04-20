class Employee: 
    company_name = "TechCorp" 
 
    @staticmethod 
    def company_info(): 
        return f"Company: {Employee.company_name}" 
 
    @staticmethod 
    def calculate_salary(hours_worked, hourly_rate): 
        return hours_worked * hourly_rate 
 
    @staticmethod 
    def is_eligible_for_bonus(salary, years_with_company): 
        if salary > 50000 and years_with_company >= 3: 
            return True 
        return False 
 
employee1 = Employee() 
employee2 = Employee() 
 
print(Employee.company_info()) 
print(Employee.calculate_salary(40, 25)) 
print(Employee.is_eligible_for_bonus(55000, 4)) 
print(Employee.is_eligible_for_bonus(45000, 2)) 