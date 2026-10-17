class Parrot:
    species = "bird"  # Class attribute
    def __init__(self, name, age):
        
        self.name = name
        self.age = age

# Create an instance of the Parrot class
blu = Parrot("Blu", 10)
woo=Parrot("Woo", 15)

# Access the attributes
print(blu.species)
print(woo.species)

print(blu.name) 
print(woo.name)
print(blu.age)
print(woo.age)