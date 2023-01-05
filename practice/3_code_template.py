# Όνομα, Επώνυμο, Φύλο, Ημερομηνία Γέννησης, Πτυχίο, Μετακίνηση, Νυχτερινή-Εργασία, Εργασιακό Καθεστώς
from Employee import Employee
from dateutil import parser

personnel = [Employee("Pikos", "Apikos", "m", "1983/01/01", True, True, False, "Active"),
                 Employee("Manolis", "Manavis", "m", "1985/01/01", False, False, True, "Active"),
                 Employee("Magia", "Melissa", 'f', "1980/12/31", True, True, True, "Active"),
                 Employee("Roza", "Rozalia", "f", "1980/12/31", True, False, True, "Pending"),
                 Employee("Daisy", "Dak", "f", "1940/06/07", False, True, True, "Archived"),
                 Employee("Bilbo", "Baggins", "m", "1937/03/03", False, True, False, "Archived"),
                 Employee("Mixalis", "Karamanos", "m", "1938/01/01", True, True, True, "Archived"),
                 Employee("Elenor", "Rigby", "f", "1966/08/04", False, False, False, "Active")]



# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ

# γυναίκες που έχουν πτυχίο ή τη δυνατότητα νυχτερινής εργασίας (ή και τα δύο)
def women_graduate_night_shift(employees):
    classify(employees,
             lambda employee: (employee.sex == 'f' and (employee.degree == True or employee.nightshift == True))
                              or (employee.sex == 'f' and employee.degree == True and employee.nightshift == True),
             'Women who have a degree and/or can work night, ')


# ενεργά μέλη του προσωπικού που έχουν τη δυνατότητα είτε νυχτερινής εργασίας ή μετακίνησης σε κοντινή πόλη, αλλά όχι και τα δύο
def active_night_shift_mobile(employees):
    classify(employees, lambda employee: (employee.nightshift == True ^ employee.transfer == True), "Can work night or can transfer to another city but not both")


# μέλη του προσωπικού που έχουν πτυχίο αλλά δεν μπορούν να μετακινηθούν
def graduate_not_mobile(employees):
    classify(employees, lambda employee: (employee.degree == True and employee.transfer == False),
             "Have degree and cant transfer")


# μέλη του προσωπικού που δεν είναι ενεργά
def inactive_staff(employees):
    classify(employees, lambda employee: (employee.work_status != 'Active'), "Not active")


# μέλη του προσωπικού με ημερομηνία γέννησης από ημερομηνία που εισαγάγει ο χρήστης και μετά
def age_limit(employees):
    age_avg_or_equal(input('\nEnter date to get all employees bornt after it: '), employees)

# δημιουργία των συνόλων με βάση τα στοιχεία της συμβολοσειράς personnel
def create_sets(employees):
    # Classify the students by their grade
    classify(employees, lambda employee: employee.sex == 'f', 'Female')
    classify(employees, lambda employee: employee.degree == True, 'Degree')
    classify(employees, lambda employee: employee.nightshift == True, 'Night shift')
    classify(employees, lambda employee: employee.work_status == 'Active', 'Active')

def classify(employees, condition, prefix_str):
    employees_subset = [employee for employee in employees if condition(employee)]
    print("\n" + prefix_str + " employees:\n")
    [print(x) for x in employees_subset]


# επιστροφή υποσυνόλου μελών προσωπικού με ημερομηνία γέννησης από minDOB και μετά
def age_avg_or_equal(minDOB, employees):
    classify(employees, lambda employee: parser.parse(employee.birthdate) >= parser.parse(minDOB), 'Born after '  + minDOB)
    dates = [parser.parse(date_string) for date_string in ['2022-03-10', '2022-03-11', '2022-03-12', '2022-03-13']]


def print_other_employee_stats(employees):
    women_graduate_night_shift(employees)
    active_night_shift_mobile(employees)
    graduate_not_mobile(employees)
    inactive_staff(employees)
    age_limit(employees)


#### κυρίως πρόγραμμα ####

# εδώ αρχικοποιήστε τα σύνολα καλώντας τη συνάρτηση create_sets()
if __name__ == "__main__":

    while True:
        print("ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ:")
        ### κλήση συναρτήσεων απάντησης ερωτημάτων γ1 έως γ5
        choice = int(input("\n1. Create and print employee sets\n2. Find employees born after date x\n3. Print other employee stats\n"))
        if choice == 1:
            create_sets(personnel)
        elif choice == 2:
            age_avg_or_equal(input("\nEnter date [format(YYYY/MM/DD)]: "), personnel)
        elif choice == 3:
            print_other_employee_stats(personnel)
        else:
            break