class Employee:
    recordDictionary = {
        "firstName": "",
        "lastName": "",
        "age": 0,
        "verified": False,
        "interests": []
    }

    def __init__(self, first_name, last_name, age):
        self.recordDictionary["firstName"] = first_name
        self.recordDictionary["lastName"] = last_name
        self.recordDictionary["age"] = age

    def verify(self):
        self.recordDictionary["verified"] = True

    def is_verified(self):
        return self.recordDictionary["verified"]


employee = Employee("Marcelo", "Martinez", 44)
employee.verify()
print(employee.recordDictionary["verified"])



