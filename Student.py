class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        print(f"Executing: {__name__}")
        return self.first + " " + self.last
    

