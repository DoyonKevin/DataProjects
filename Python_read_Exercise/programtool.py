#Kevin Doyon
#Week 1 python assignment

import sys

#Makes employees for the csv
def genemploy():
    """Allows user to generate employees"""
    count, employee_list = 0,[]
    
    #Allows user to enter how many employees to add
    while(True):
        try: 
            num_enploy = int(input("Enter how many employee's you would like to enter: "))
        except ValueError: print("Please enter an interger: ")
        else:
            #Exits program if no employees are to be added
            if num_enploy == 0:
                sys.exit()
            break  
    #Adds number of employees previously selected
    while(count<num_enploy):
        try: 
            tem_employ = {"first":input("Enter the employee's first name: "),
            "last":input("Enterh the employee's last name: "),
            "birth":int(input("Enter the employee's birth year: ")),
            "department":input("Enter the employee's department: "),
            "salary":int(input("Enter the employee's salary: "))}          
        except ValueError: print("Please enter integers for year and pay.")
        else: 
            employee_list.append(tem_employ)
            count+=1

    return employee_list




#Finds the oldest employee
def old_employ(employees):
    """Finds the oldest employee"""
    #Initializes search
    oldest_employee,oldest_age = employees[0]['first']+' '+employees[0]['last'],employees[0]['birth']
    #for every employee in list
    for employee in employees:
        #If current employee is older than saved employee
        if(employee['birth']<oldest_age):
            #Save current employee data
            oldest_employee, oldest_age = employee['first']+' '+employee['last'],employee['birth']
    print(f"The oldest employee is {oldest_employee}.")




#Finds the average employees salary
def avg_employ(employees):
    """Finds the average employee salary"""
    #Finds the average salary of employees
    emp_avg = sum([int(employee['salary']) for employee in employees])/(len(employees))
    #emp_avg = sum(sum_list)/(len(employees))
    print(f'The average employee salary is ${emp_avg}')




#Finds the employee salary by department
def avg_depart(employees):
    """Finds the employee salary by department"""
    departments = []
    #Lists all know departments in employee with no duplicates
    for employee in employees:
        if employee['department'] not in departments:
            departments.append(employee["department"])    
    # For every department
    for department in departments:
        department_sum, num_employ = 0,0
        #For every employee
        for employee in employees:
            #If current employee is in the current department 
            if department == employee["department"]:
                #add employee pay to department sum
                department_sum += int(employee['salary'])
                num_employ +=1
        department_avg = department_sum/num_employ
        print(f"The {department} average salary is ${department_avg}")





#Finds the top three paid employees
def three_top(employees):
    """Finds the top three paid employees"""
    #Ensure there are enough employees to find the top three
    if(len(employees)>=3):
        employee_name,employee_salary,top_three = [],[],[]
        
        #For every employee
        for employee in employees:
            #Makes index matching list for name and salary
            employee_name.append(employee['first']+' '+employee['last'])
            employee_salary.append(int(employee['salary']))
        #For three times
        for i in range(3):
            #Find max payed salary
            max_pay = max(employee_salary)
            #Find index of max pay
            max_index = employee_salary.index(max_pay)
            #Pop max name to list
            top_three.append(employee_name.pop(max_index))
            #pop previous max from both lists
            employee_salary.pop(max_index)
        print(f"The three highest payed employees are {top_three[0]}, {top_three[1]}, and {top_three[2]}")
    else:
        print("There are not enough employees to show the top 3.")





#Runs all programtools functions
def sortdata(employees):
    """Runs all programtools functions"""
    avg_employ(employees)
    avg_depart(employees)
    three_top(employees)
    old_employ(employees)

if __name__ == "__main__":
    print("This is programtool")