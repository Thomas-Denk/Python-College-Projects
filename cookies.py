# This code asks the user for ingredients to make cookies. They can enter as many ingredients as they like. 
# When they input "stop", the code will let them know if they have all the required ingredients.

ingredients = ("place_holder",)
clock = 0
z = 0
eggs = False
flour = False
butter = False
sugar = False
chocolate_chips = False


#total = float(ingredients[z])
while clock == 0:
    input_data = (input("Please enter your ingredients. When you are done, enter \'stop\': "),)
    ingredients = ingredients + input_data
    #print(ingredients)
    #z = z + 1
    if ingredients[len(ingredients) - 1].lower() == "stop":
        #print("You entered stop....")
        clock = 1

z = len(ingredients) - 1
while z > -1:
    if ingredients[z].lower() == "eggs" or ingredients[z].lower() == "egg":
        eggs = True
        z = -1
    else:
        z = z - 1



z = len(ingredients) - 1
while z > -1:
    if ingredients[z].lower() == "flour" or ingredients[z].lower() == "wheat flour" or ingredients[z].lower() == "white flour":
        flour = True
        z = -1
    else:
        z = z - 1

z = len(ingredients) - 1
while z > -1:
    if ingredients[z].lower() == "butter":
        butter = True
        z = -1
    else:
        z = z - 1

z = len(ingredients) - 1
while z > -1:
    if ingredients[z].lower() == "sugar" or ingredients[z].lower() == "white sugar" or ingredients[z].lower() == "refined sugar":
        sugar = True
        z = -1
    else:
        z = z - 1

z = len(ingredients) - 1
while z > -1:
    if ingredients[z].lower() == "chocolate chips" or ingredients[z].lower() == "mini chocolate chips":
        chocolate_chips = True
        z = -1
    else:
        z = z - 1    

if eggs == True and flour == True and butter == True and sugar == True and chocolate_chips == True:
    print()
    print()
    print("You are ready to make cookies!") 
    print()

else:
    if eggs == False:
        print()
        print("You are missing eggs!")
    if flour == False:
        print()
        print("You are missing flour")  
    if butter == False:
        print()
        print("You are missing butter!")
    if sugar == False:
        print()
        print("You are missing sugar!")
    if chocolate_chips == False:
        print()
        print("You are missing chocolate chips!") 
    print()
    print()
    print("Please find these ingredients and try again!")
    print()
    
     #  ingredients.append(0)
       
       
        


 


