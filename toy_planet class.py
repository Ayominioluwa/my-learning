class Planet:
    def __init__(self, name, type, star):
        self.name = name
        self.type = type 
        self.star = star
        if not all(isinstance(input, str) for input in (self.name, self.type, self.star)):
            raise TypeError("Name, Type and star must be strings")
        if not all(input for input in (self.name, self.type, self.star)):
            raise ValueError("Name, Type and Star must  be a non-empty string")
    def orbit(self):
        print(f"{self.name} is orbiting the {self.star}...")
    def __str__(self):
        return (f"Planet {self.name} is of type {self.type} with {self.star} as it's star.")