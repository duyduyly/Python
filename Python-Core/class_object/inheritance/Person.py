class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def print_name(self):
        print(f"Firstname: {self.firstname}, Lastname: {self.lastname}")
