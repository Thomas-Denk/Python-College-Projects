# Today we are talking about lists
# Lists have only been around since Python 2.0

seasons = ["winter", "spring", "summer", "fall"]
print(seasons[-1])

---------------------
my_list = []  


students_tuple = (("Harry", "harry@gmail.com"), ("Lucy", "lucia@gmail.com"), ("Sally", "sally@gmail.com"))
# example of nested tuples
for each_student in students_tuple:
    print(each_student)

    if "rutgers" in each_student[1]:     # keyword check for specific location....
        each_student[0]
        my_list.append(each_student[0])   

        # alternate option is insert command...

        print(seasons.insert(2, "spring-summer"))  # will insert new value into existing list at number location...

        campus_locations = ["college avenue", "busch campus"]
        other_locations = ["livingston campus", "douglass campus"]
        campus_locations.extend(other_locations)  # a way to combine two lists!
        print(campus_locations)


---------

solfedge = ["do", "do", "mi", "fa", "sol", "la", "do", "do"]
solfedge[1] = "re"    # overwrites the value in this position in the list


-----------

# deleting list items...

my_list = list(range(1,6))
print(my_list)

del my_list[2]  # deletes value at place 2
my_list.remove(3)   # this instead deletes the first occurance of the specified value
number_removed = my_list.pop()   # another variation on removing. Thsi time it is sent to a variable

print(len(my_list))  # gives you the length of the list
print(my_list.count(1)) # tells you how many occurances of the entered value are in the list.
print(" ".join(my_list)) # joins items in lists while including the between value that's entered
print(my_list.split(" "))  # splits items and incudes the between value that's entered.

#   nLogn is still a great go to for sorting algorithms

my_list = list(range(1,6))
my_other_list = [3, 5, 1, 2]
my_other_list.sort()
sorted(my_other_list, reverse = True)
print(my_other_list)






