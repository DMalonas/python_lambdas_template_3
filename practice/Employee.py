class Employee:

    def __init__(self, forename, surname, sex, birthdate, degree, transfer, nightshift, work_status):
        self.forename = forename
        self.surname = surname
        self.sex = sex
        self.birthdate = birthdate
        self.degree = degree
        self.transfer = transfer
        self.nightshift = nightshift
        self.work_status = work_status



    def __str__(self) -> str:
        return self.forename + " " + self.surname + " " + self.sex + " " + self.birthdate + " " + str(self.degree) + " " + str(self.transfer) + " " + str(self.nightshift) + " " + self.work_status + "\n"


