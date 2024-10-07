class Person:
    name = "John"
    age = 36
    country = "USA"
    occupation = "Software Engineer"
    def info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Country: ", self.country)
        print("Occupation: ", self.occupation)
        
Rajdeep = Person()
# Rajdeep.name = "Rajdeep";
# Rajdeep.age = 19;
# Rajdeep.country = "India";
# Rajdeep.occupation = "IT student, software developer";
Rajdeep.info();
