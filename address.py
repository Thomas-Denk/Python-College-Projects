first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
street_address = input("What is your street address? ")
city = input("What is your city? ")
state = input("What is your state? ")
zip_code = input("What is your zipcode? ")

print("Your mailing address should be structured as:")

print(f"{first_name.title()} {last_name.title()}")
print(f"{street_address.title()}")
print(f"{city.title()}, {state.upper()} {zip_code}")

