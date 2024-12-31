# This code will read the list full_names and based off certain characterics of each name, output an appropriate email address they can be assigned.
import random



#print(random_number)

full_names = ["Alex Smith", "Samantha Smith", "Juan Smith", "Alex Patel", "Harry Kim", "Frank Smith", "Adam Smith"]
rutgers_emails = ["","","","","","",""]
print ("Given the list of names, the email addresses associated with these names are: ")

#print(full_names[0])

x = 0

while x < 7:
    random_number = random.randint(100, 999)
    separated_name = full_names[x].split(" ")
    name_emails[x] = separated_name[0][0].lower() + separated_name[1][0].lower() + str(random_number) + "@cooldomain.edu"
    x = x + 1


#print(separated_name)
#print(separated_name[0][0])
#print(separated_name[1][0])
print(name_emails)
