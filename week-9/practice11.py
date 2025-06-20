class Dogs:


    # Instance attribute
    def __init__(self, name, attr1):
        self.name = name
        self.attr1 = attr1

# Object instantiation
dog1 = Dogs("Oscar", "mammal")
dog2 = Dogs("Peaches", "mammal")

# Accessing class attributes
print("Oscar is a {}".format(dog1.attr1))
print("Peaches is also a {}".format(dog2.attr1))

# Accessing instance attributes
print("My name is {}".format(dog1.name))
print("My name is {}".format(dog2.name))
