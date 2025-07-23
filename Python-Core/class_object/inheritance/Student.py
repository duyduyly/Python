from class_object.inheritance.Person import Person


class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # add params for parents class
        self.graduation_year = year

    def studentInfo(self):
        print(
            f"Student {self.get_fullname()} graduated at {self.graduation_year}"
        )  # call fullname function from parent class


student = Student("Alan", "Ly", 2021)
student.studentInfo()
