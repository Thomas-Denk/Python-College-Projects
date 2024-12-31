#Averages.py with conditions involved

sum = 0
count = 0

#while True:
try:    
    user_input = input("Please enter a grade. Otherwise enter \'q\' to quit: ")
    if user_input == 'q';
        average = sum/count
        print(f"The average of the grades is {average}")
        break
    else:
        print("I am checking to see whether the number is a float")
        sum += float(user_input)
        count += 1
except(ValueError) as e:
    print(e)
    continue


# Check out the isInstanceof command
# Check out try and except format (see above) also called tricept

# on to Strings and Tuples
# Tuples cannot be changed once they are made. You can store multiple types of data in tuple (unlike Java)
my_tuple = (100, "one hundred", 100.0)
print(my_tuple[1:3]) # example of slicing....will return only 2nd and 3rd element (ending is not inclusive)
print(my_tuple[:-1])  # reverse order

# information can be extracted from tuples...

my_tuple = "Professor", "OOP", "Time"
instructor, classname, timeword = my_tuple    # creates three new separate variables 
# python is smart enough to define data type based off of what you enter

my_tuple = instructor, classname, timeword   # reverse order

# for loops

for each_information in my_tuple:
    print(each_information)  #itereates through the tuple

#range function
range(0,10)    # returns sequence of integers

for each_information in range(0,len(my_tuple),3):
    if (each_information % 2 == 0):    # only printing even numbers
        print(my_tuple[each_information])   # using index number iteration
        

# Nested tuples

tuple_students = "Mohan",("Satyam", "Rishab"), "Paul"
# midterm and final involve web data. Tuples are useful for this.

print(tuple_students[1][1])   



