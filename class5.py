# while loops
# Spotify track playback loop counter

user_input = int(input("What is the max amount of times you'd like to listen? "))

amount_listened = 0
while amount_listened < user_input:
    print(f"The number of times you have listened is: {amount_listened}")
    amount_listened += 1

# another variation on this is while True loop. This variation has nested loops.


while True:
    amount_listened += 1
    print(f"The number of times you have listened is: {amount_listened}")
    if amount_listened > user_input:
        break

# third option

while True:
    user_input = input("Would you like to still listen to the song? Y/N ").lower() # lower method makes sure case doesnt matter
    if user_input = "y":
    
        amount_listened += 1
        print(f"The number of times you have listened is: {amount_listened}")
        
    else:
        break

# fourth option

while True:
    user_input = input("Would you like to still listen to the song? Y/N ").lower() # lower method makes sure case doesnt matter
    if user_input = "y":
    
        amount_listened += 1
        print(f"The number of times you have listened is: {amount_listened}")
        continue
    break

# Option 5 with else statement

while True:
    user_input = input("Would you like to still listen to the song? Y/N ").lower() # lower method makes sure case doesnt matter
    if user_input = "y":
    
        amount_listened += 1
        print(f"The number of times you have listened is: {amount_listened}")
    else:
        print("Looks like you must be tired of listening to this song.")
    break

#-----------------------------------------------------

# Moving on to for loops

# demonstration for matching letter in string

vowels = "aeiou"

index = 0
last_index = len(vowels) -1

#while loop
while index < last_index:
    print(vowels[index])
    index += 1
# For loop

for each_vowel in vowels:
    print(each_vowel)

#For loop with range

for each_index in range(0,len(vowels)-1,2):    # the 2 makes it only show every other!
    print(each_index)





