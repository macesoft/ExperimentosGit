class Greeter:
    name_to_greet = ""

    def greet(self, name_to_greet):
        self.name_to_greet = name_to_greet
        print(f"Hello {name_to_greet}!")
