import random

def sum_numbers(num_one, *args):
    return num_one + args[0] + args[1]

def sum_numbers(num_one, **kargs):
    return kargs

print(sum_numbers(2,3))


# optional arguments with tuples vs 

def full_name(first, last):
    return first + " " + last


def net_id(first, last):
    return first[0] + last[0] + random.randint(100,999)


# long name is determined to be 10 or more length
def long_name(function, first, last):
    if len(function(first,last)) > 10:
        print("The name using this function is long")
    else:
        print("The name using this function is not long")


long_name(full_name, "Professor", "Ahmed")

# Now we will look at nested functions


# there are two types: closures and regular

def average(list):
    def sum(list):
        sum = 0
        my_list = []
        for each in list:
            sum+= each
        return sum
    return sum(list) / len(list)

print(average([10,10,10]))


average_lambda = lambda my_list : sum(my_list) / len(my_list)
print(average_lambda([20,20,20]))


my_list = ["Juliet", "Hamlet", "William"]
my_list.sort(key=lambda name: name.split()[-1])



import Student

student = Student.Student("Elon","Musk")   # goes to init of function
print(student.first)
print(student.last)

print(f"Executing {__name__}")  # This is main method






