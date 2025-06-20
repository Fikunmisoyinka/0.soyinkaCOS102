class Program:

    # default constructor
    def __init__(self, course):
        self.course = course

    # a method for printing data members
    def print_Course(self):
        print("CSC 102 - Introduction to Problem Solving", self.course)


# creating object of the class
obj = Program("CSC 102")

# calling the instance method using the object obj
obj.print_Course()
