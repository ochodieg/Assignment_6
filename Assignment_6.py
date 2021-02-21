import planner_data
import random


number_of_employees = \
    int(input("How many employees work at this location? "))

validated_employee_range = planner_data.is_in_range(number_of_employees, 1, 20)


if not validated_employee_range:
    print("\nYou must have between 1 and 20 employees.")
    number_of_employees = random.randrange(1, 21)
    print("Your random amount of employees is: " + str(number_of_employees))


for employee in range(1, number_of_employees + 1):

    hours_worked = planner_data.get_hours_worked()
    pay_rate = planner_data.get_pay_rate()
    classification = planner_data.classify_timecard(hours_worked)
    if hours_worked > 40:
        total_pay = format((40 * pay_rate) + ((pay_rate * 1.5) * (hours_worked - 40)), ".2f")
    else:
        total_pay = format(hours_worked * pay_rate, ".2f")

    print("\nEmployee " + str(employee) + " worked",
          str(hours_worked) + " hours at $" + str(pay_rate) + "/hr. \n"
          "\t\tclassified: " + classification,
          "\n\t\tGross paycheck: $" + str(total_pay))

