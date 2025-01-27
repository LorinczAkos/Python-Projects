# Self evaluation Exercises - Basic concepts
# Exercise 1 - Variable with name and age
name = "Akos"
age = 29

# Exercise 2 - Simple Calculation

rate = 1.68
value = 274
payment = rate * value

# Exercise 3 - Advanced Calculation

rate = 1.68
value_day = 8
value_night = 4
payment = (rate*value_day)+((rate/2)*value_night)

# Exercise 4 - Use of comments in code

rate = 1.68
value_day = 358
value_night = 103
#Payment for electricity for the current month
payment = rate * value_day + rate / 2 * value_night

# Exercise 5 - Use of variables

first_name = "Ákos"
last_name = "Lőrincz"

# Exercise 6 - Uniting 2 variables

first_name = "Akos"
last_name = "Lorincz"
full_name = first_name+' '+last_name

# Exercise 7 - Use of F-string in order to add variables into a basic text

first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
message = f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"

# Exercise 8 - Boolean objects

is_active = True
is_delete = False

# Exercise 9 - Input use

name = str(input("Your name? "))
email = str(input("Your e-mail? "))
age = int(input("Your Age?"))
height = float(input("Your Height?"))
is_active = bool(input("Would you like to receive updates?"))

# Exercise 10 - Use of IF and ELSE conditional

is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else:
    is_next = False
print("Este candidatul invitat la urmatoarea interviu?",is_next)

# Exercise 11 - Advanced use IF conditional

work_experience = int(input("Enter your full work experience in years: "))

if work_experience >= 6:
    developer_type = "Senior"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Middle"
print("Developer seniority:",developer_type)