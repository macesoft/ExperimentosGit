class Employee:

    firstName = ""
    lastName = ""
    age = 0
    verified = False
    interests = []

    def __init__(self, first_name, last_name, age):
        self.firstName = first_name
        self.lastName = last_name
        self.age = age

    def verify(self):
        self.verified = True

    def is_verified(self):
        return self.verified

    def add_interest(self, interest):
        self.interests.append(interest)

    def create_json(self):
        employee_as_json = {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'age': self.age,
            'verified': self.verified,
            'interests': self.interests
        }
        return employee_as_json
