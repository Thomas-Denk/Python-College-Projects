''' This code\" 1) creates a list of 100 random integers between 0 and 9 called "random_hundred", 2) creates a dictionary object called "count_dictionary" that stores the count of the number of times each of the numbers between 0 and 9 (the keys) appeared (values associated with keys) in the list, 3) prints the dictionary information using an f-string to the user, 4) creates a set object called "unique_set" that contains non-duplicate random numbers from the list, and 5) prints to the user the length of unique_set to confirm that it is 10.\"

'''


import random
x = 0
random_hundred = [0] * 100

count_dictionary = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0

}      

while x < 100:
    random_value = random.randint(0,9)
    #print(random_value)
    random_hundred[x] = random_value
    count_dictionary[random_value] = count_dictionary.get(random_value) + 1
    x = x + 1


random_hundred.sort()



#print(random_hundred)
#print(count_dictionary)
unique_set = {0}
y = 0

#print("Now we will try to print")
while y < 100:
    if random_hundred[y] < 10:
        #print(count_dictionary[y])
        unique_set.add(random_hundred[y])
    
        #print(unique_set)
        
    y = y + 1  
    
#unique_set.sort()
#print(unique_set)

print(f"Count of values: {count_dictionary}")
print(f"Length of Set: {len(unique_set)}")



