class SST:
    
    # Class attribute
    prog1 = "Computer Science"

    # Instance attribute
    def __init__(self, name):
        self.name = name
        self.prog1 = SST.prog1
    
    def speak(self):
        print("My name is {}".format(self.name))
        print("I'm studying {}".format(self.prog1))

# Object instantiation
stud1 = SST(input("Enter the name of the first student: "))
stud2 = SST(input("Enter the name of the second student: "))

# Accessing class methods
stud1.speak()
stud2.speak()
