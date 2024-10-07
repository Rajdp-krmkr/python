class Person:
    def __init__(self, name , age, country, occupation):
        print("Constructor is called");
        self.name = name;
        self.age = age;
        self.country = country;
        self.occupation = occupation;
    def info(self):
        print(f"{self.name} is {self.age} years old, lives in {self.country} and works as a {self.occupation}");

Rajdeep = Person("Rajdeep", 19, "India", "IT student, software developer");
Rajdeep.info();

jeff_Bezos = Person("Jeff Bezos", 57, "USA", "Businessman");
jeff_Bezos.info();