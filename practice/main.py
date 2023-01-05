# This is a sample Python script.
from dateutil import parser

from Employee import Employee

import dateutil
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def twos_comp(str):
    n = len(str)
    i = n - 1
    while (i >= 0):
        if (str[i] == '1'):
            break
        i -= 1
    if (i == -1):
        return '1' + str
    k = i - 1
    while (k >= 0):
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)
        k -= 1
    return str


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def is_num_binary(x):
    return  all(c in '01' for c in x)



def is_num_decimal(x):
    return x.isdecimal()


def convert_to_binary_from_decimal(number):
    return bin(number)


def dec_to_bin(a, l=[]):
    binary = 0
    ctr = 0
    temp = a  # copy input decimal

    # find binary value using while loop
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    return binary

def bin_to_dec(number):
    print(len(number))
    return int(number, 2)


def task_1():
    while True:
        choice = int(input("\n1: Decimal to binary\n2: Binary to decimal\n3: 2's Complement\n"))
        if choice == 1:
            try:
                integer = input("\nEnter decimal: ")
                is_num_decimal(integer)
                print(dec_to_bin(int(integer), []))
            except:
                print("\nnot integer\n")
                continue
        elif choice == 2:
            try:
                binary = input("\nEnter binary: ")
                is_num_binary(binary)
                print(bin_to_dec(binary))
            except:
                print("\nnot binary\n")
        elif choice == 3:
            try:
                binary = input("\nEnter binary")
                is_num_binary(binary)
                print("two's complement: " + str(twos_comp(binary)))
            except:
                print("\nnot binary\n")
        else:
            print("")






# Press the green button in the gutter to run the script.
def add_products(basket, products):
    name = input('\n1 Enter name\n2 Exit product-enter mode\n ')
    if name == "2":
        return
    else:
        if product_exists(name, products):
            quant = int(input("\nEnter quantity: "))
            try:
                basket[name] += quant
            except:
                print("\nWrong key\n")
            add_products(basket, products)


def product_exists(name, products):
    for entry in products:
        if entry[0] == name:
            return True
    return False


def remove_product(basket, products):
    display_basket(basket, products)
    choice = int(input("\nChoose line to remove from basket"))
    cnt = 0
    if choice >= 0 and choice < len(basket):
        for entry in basket:
            if cnt == choice - 1:
                basket[entry] = 0
                break
            cnt += 1

def display_basket(basket, products):
    sum = 0.0
    print('AA\tPRODUCT\tQUANTITY\tPRICE\tTOTAL VALUE\n')
    display_tuple = tuple({'AA': 0, 'PRODUCT': '', 'QUANTITY': 0, 'PRICE': '', 'TOTAL VALUE': ''} for _ in range(len(products)))

    for idx in range(len(products)):
        display_tuple[idx][0] = idx + 1
        display_tuple[idx][1] = products[idx][0]
        display_tuple[idx][2] = list(basket.items())[idx][1]
        display_tuple[idx][3] = str(products[idx][1]) + "E"
        display_tuple[idx][4] = str(int(display_tuple[idx][2]) * products[idx][1])
        sum += int(display_tuple[idx][2]) * products[idx][1]
        print(str(display_tuple[idx].values())[30: -2].split(","))
    # for idx in range(len( ))
    print("\nTotal: " + str(sum) + "E")


def display_basket_with_discount(basket, products):
    sum = 0.0
    print('AA\tPRODUCT\tQUANTITY\tPRICE\tTOTAL VALUE\n')
    display_tuple = tuple(
        {'AA': 0, 'PRODUCT': '', 'QUANTITY': 0, 'PRICE': '', 'TOTAL VALUE': ''} for _ in range(len(products)))
    for idx in range(len(products)):
        display_tuple[idx][0] = idx + 1
        display_tuple[idx][1] = products[idx][0]
        display_tuple[idx][2] = list(basket.items())[idx][1]
        display_tuple[idx][3] = str(products[idx][1]) + "E"
        display_tuple[idx][4] = str(int(display_tuple[idx][2]) * products[idx][1])
        sum += int(display_tuple[idx][2]) * products[idx][1]
        print(str(display_tuple[idx].values())[30: -2].split(","))
    print("\nTotal: " + str(sum * 0.93) + "E")


def buy_products(basket, products):
    display_basket(basket, products)
    cnt = 0
    for entry in basket:
        if basket[entry] != 0:
            cnt = 1
    if cnt == 0:
        print('\nThe basket is empty\n')
        exit(1)
    choice = int(input('Do you have a member\'s card? (1 for yes | 2 for no'))
    if choice == 1:
        display_basket_with_discount(basket, products)
        print("\nThe program will now exit\n")
        exit(1)



def by_female(employees):
    female_emp = {}
    for employee in employees:
        if employee.sex == 'f':
            female_emp[employee.forename + " " + employee.surname] = employee
    return female_emp


def by_degree(employees):
    degree_emp = {}
    for employee in employees:
        if employee.degree == True:
            degree_emp[employee.forename + " " + employee.surname] = employee
    return degree_emp


def classify(employees, condition, prefix_str):
    employees_subset = [employee for employee in employees if condition(employee)]
    print("\n" + prefix_str + " employees:\n")
    [print(x) for x in employees_subset]

def create_sets(employees):
    # Classify the students by their grade
    classify(employees, lambda employee: employee.sex == 'f', 'Female')
    classify(employees, lambda employee: employee.degree == True, 'Degree')
    classify(employees, lambda employee: employee.nightshift == True, 'Night shift')
    classify(employees, lambda employee: employee.work_status == 'Active', 'Active')


def print_other_employee_stats(employees):
    classify(employees,
             lambda employee: (employee.degree == True or employee.nightshift == True)
                              or (employee.degree == True and employee.nightshift == True),
             'Have degree and can work night, or both, ')
    classify(employees, lambda employee: (employee.nightshift == True ^ employee.transfer == True), "Can work night or can transfer to another city but not both")
    classify(employees, lambda employee: (employee.degree == True and employee.transfer == False), "Have degree and cant transfer")
    classify(employees, lambda employee: (employee.work_status != 'Active'), "Not active")
    age_avg_or_equal(input('\nEnter date to get all employees bornt after it: '), employees)

def age_avg_or_equal(minDOB, employees):
    classify(employees, lambda employee: parser.parse(employee.birthdate) >= parser.parse(minDOB), 'Born after '  + minDOB)

    dates = [parser.parse(date_string) for date_string in ['2022-03-10', '2022-03-11', '2022-03-12', '2022-03-13']]


if __name__ == '__main__':
    basket = {"MILK 1LT" : 0, 'YOGURT 2%': 0, 'ICE CREAM': 0, 'NESCAFFE': 0, 'BISCUITS': 0, "CHEF'S SALAD": 0, 'TOAST CHEESE': 0, 'EXTRA VIRGIN OLIVE OIL': 0, 'FILTERED COFFEE': 0, 'TOAST BREAD': 0}
    products = [('MILK 1LT', 1.5), ('YOGURT 2%', 2.0), ('ICE CREAM', 2.5),
                ('NESCAFFE', 7.5), ('BISCUITS', 1.0), ("CHEF'S SALAD", 1.0),
                ('TOAST CHEESE', 6.0), ('EXTRA VIRGIN OLIVE OIL', 8.0),
                ('FILTERED COFFEE', 7.0), ('TOAST BREAD', 1.5)]

    employees = [Employee("Pikos", "Apikos", "m", "1983/01/01", True, True, False, "Active"),
                 Employee("Manolis", "Manavis", "m", "1985/01/01", False, False, True, "Active"),
                 Employee("Magia", "Melissa", 'f', "1980/12/31", True, True, True, "Active"),
                 Employee("Roza", "Rozalia", "f", "1980/12/31", True, False, True, "Pending"),
                 Employee("Daisy", "Dak", "f", "1940/06/07", False, True, True, "Archived"),
                 Employee("Bilbo", "Baggins", "m", "1937/03/03", False, True, False, "Archived"),
                 Employee("Mixalis", "Karamanos", "m", "1938/01/01", True, True, True, "Archived"),
                 Employee("Elenor", "Rigby", "f", "1966/08/04", False, False, False, "Active")]

    print_hi('PyCharm')
    while True:
        choice = int(input("\n1: Task 1\n2: Task 2\n3: Task 3\n4: Task 4\n"))
        if choice == 1:
            task_1()
        elif choice == 2:
            choice = int(input("\n1. Add items to basket\n2. Show basket\n3. Remove from basket\n4. Buy products\n"))
            if choice == 1:
                add_products(basket, products)
            elif choice == 2:
                display_basket(basket, products)
            elif choice == 3:
                remove_product(basket, products)
            elif choice == 4:
                buy_products(basket, products)
        elif choice == 3:
            choice = int(input("\n1. Create and print employee sets\n2. Find employees born after date x\n3. Print other employee stats\n"))
            if choice == 1:
                create_sets(employees)
            elif choice == 2:
                age_avg_or_equal(input("\nEnter date [format(YYYY/MM/DD)]: "), employees)
            elif choice == 3:
                print_other_employee_stats(employees)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
