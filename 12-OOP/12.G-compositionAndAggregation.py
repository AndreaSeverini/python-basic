# COMPOSITION
class Salary:  # CONTENT
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay * 12) + self.reward


class Employee:  # CONTAINER
    def __init__(self, name, position, pay, reward):
        self.name = name
        self.position = position
        self.final_salary = Salary(pay, reward)  # Creating a new instance of the Salary class

    def final_salary_m(self):
        return self.final_salary.annual_salary()


# Salary is part of Employee (Composition)
# Salary is a component/content of the Employee class

person = Employee('Andrea', 'Developer', 2100, 6000)
print(person.final_salary_m())  # Output: 29400

# In this example, we have two classes: Salary and Employee.

# The Salary class represents the content or component of an employee's salary.
# It has attributes for pay and reward, as well as a method to calculate the annual salary.

# The Employee class represents the container that holds the salary content.
# It has attributes for name, position, and a final_salary attribute that is an instance of the Salary class.

# When we create an Employee object, we also create a Salary object as part of it using composition.
# The Salary object is instantiated within the Employee's __init__ method using Salary(pay, reward).

# The Employee class has a final_salary_m method that accesses the annual_salary method of the contained Salary object.
# This demonstrates the composition relationship, where the Employee class
# contains a Salary object as part of its structure.

# We create an Employee object named person with the name 'Andrea', position 'Developer', pay 2100, and reward 6000.
# We then call the final_salary_m method on the person object, which calculates and returns the final salary.
# The output will be 29400, which is the result of the annual_salary calculation.

# AGGREGATION - One-way relationship
# Bank has an Employee
# Library has a Book

class Salary2:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay * 12) + self.reward


class Employee2:
    def __init__(self, name, position, sal):
        self.name = name
        self.position = position
        self.final_salary = sal

    def final_salary_m(self):
        return self.final_salary.annual_salary()


# They are now completely separated entities
sal = Salary2(2100, 6000)  # Creating an instance of Salary2
person = Employee2('Andrea', 'Developer', sal)  # Creating an instance of Employee2 with a Salary2 object

print(person.final_salary_m())  # Output: 29400

# In this example, we have two classes: Salary2 and Employee2.

# The Salary2 class represents an independent entity that calculates an annual salary based on pay and reward.
# It has an annual_salary method that performs the calculation.

# The Employee2 class represents another independent entity that holds a reference to a Salary2 object.
# It has attributes for name, position, and a final_salary attribute that is assigned a Salary2 object.

# The Employee2 and Salary2 classes are completely separate entities without any special relationship between them.
# The Employee2 class simply holds a reference to a Salary2 object, establishing an aggregation relationship.

# We create a Salary2 object named sal with pay 2100 and reward 6000.
# We then create an Employee2 object named person with the name 'Andrea', position 'Developer',
# and the sal object as the final_salary attribute.

# Finally, we call the final_salary_m method on the person object,
# which accesses the annual_salary method of the contained Salary2 object.
# The output will be 29400, which is the result of the annual_salary calculation.

# This demonstrates the aggregation relationship, where the Employee2 class has a reference
# to the Salary2 object but does not own or control it.
