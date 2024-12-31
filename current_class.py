students = 32
candies = 91
name = "Thomas"
print("Each student will receive",candies // students, "candies")


print("The teacher will have",candies % students,"candies left")

print("The teacher will have " + str(candies % students) + " candies left")

print(r"This escape character is \n") #here the r character tells python to treat the entire contents literally

#name = input("Enter your name: ")

#print("Hello"*100)

print(name[-1])
print(name[0:4]) #Slicing is not inclusive for the second number in the range
print(name[2:]) #zero is assumed if there is a space


print(len(name)) # length method that provides the length of the variable as an int. Can be used with print here.

print(len(str(candies)))  # example with casting to convert original int value to string

print(name[2:len(name)]) # can use len method instead of -1

print(name.count("o") + name.count("t"))    #count function lets you count how many times a character appears in a string

#.upper() will provide an uppercase version of your entire string
#.lower() will provide a lowercase version of your entire string

print(name.upper()) # prints an uppercase version of string 
print(name.lower()) # prints a lowercase version of string

#.title() --> Makes the first letter capitalized (does not override prior capitalization)

# f-strings (formatted strings) make string concatenation easier and faster

print("hello" + name + "world") #traditional concatenation needs + operator

print(f"hello {name} How are you?") # f-strings let us avoid using operators and instead use "f" and curly braces. Spacing is also more natural.

salary = 20000

#print(f"Your salary is" ${salary:,}) # the comma tells the formatted text to behave like money
      
#print(f"Your salary is" ${salary:,.2f}) # the period tells the formatted text to behave as a decimal. The 2 tells it how many places.     

#if name:   This will assume you mean name==True
# if not name: This will assume you mean name==False


if name == "Thomas":
    print("The condition was met!")   # if statements in python require proper indentation to function as a group.

elif name == "David":
    print("The condition was unexpected")  # example of else if clause
else:
    print("The condition was not met")  # example of an else clause

# name = input().lower()   This is an example of taking string input and turning it into lowercase

# inputs can be nested..... 
# name = input("What's your name?").lower() 
# if name == "Thomas":
#    name = input("What's your favorite sport?").lower()
#

# In conditionals, we can also check if something is greater or less than....

# if number > 10:
#    print("Your number is greater than 10")

# if number % 2 == 0:
#   print"Your number is evenly divisible by 2....aka its an even number")

#-------------------------------------------------------------------------
# 9/28/23 Class








