# This code allows the user to enter as many numbers as they like. 
# When they input "stop", the code will return the average of their numbers.
numbers = [0]
total = int(0)
clock = 0
z = 0

total = float(numbers[z])
while clock == 0:
    numbers[z] = input("Please enter as many numbers as you would like. When you are done, enter \'stop\': ")
    if numbers[z].lower() == "stop":
        clock = 1

    else:
    
        numbers.append(0)
       
        total = total + float(numbers[z])
        
        z = z + 1


average = total / (z)
print(f"The average of the numbers you entered is: {str(average)}")  