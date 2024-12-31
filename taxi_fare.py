# This code will ask for the distance traveled and then return the correct taxi fare for that distance.



user_distance = float(input("Enter the distance you have traveled (in kilometers): "))

meter_distance = user_distance * 1000

incremental_counter = meter_distance // 140
print(incremental_counter)
fare = 4.00 + (0.25 * incremental_counter)

print(f"The total cost of your trip should be: ${str(fare)}")

