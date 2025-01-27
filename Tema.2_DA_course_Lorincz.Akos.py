# Self evaluation Exercises - Working with data in Python
# Exercise 1 - Character repetition

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for char in message:
    if char == search:
        result += 1

print("Number of occurrences of 'r':", result)

# Exercise 2 - Use of loops

sum = 0

while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        sum += i

print("Summa totala este:", sum)

# Exercise 3 - Use of Definitions

def greeting():
    print('Hello world!')

greeting()

# Exercise 4 - Use of a template for an invitation list

username = str(input("Your Name: "))
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"
print (invite_to_event(username))

# Exercise 5 - Taxi service cost calculator

base_rate = 40
price_per_km = 10
total_trip = 0

def calculate_trip_price(distance_km):
    global total_trip
    total_trip += 1
    return base_rate + (price_per_km * distance_km)

# Example usage:
distance_km = 15
trip_cost = calculate_trip_price(distance_km)
print(f"Total trip cost: {trip_cost} USD")
print(f"Total trips made: {total_trip}")

# Exercise 6 - Variable to return full names

def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

print(get_fullname("Akos", "Lorincz"))
print(get_fullname("Peter", "Szakacs", "Andras"))

# Exercise 7 - Calculation of total debt ignoring advanced payments

def amount_payment(payments):
    total_debt = 0
    for payment in payments:
        if payment > 0:
            total_debt += payment
    return total_debt

payments = [100, -50, 200, -10, 300]
print(amount_payment(payments))

# Exercise 8 - Removing extremes from sample

def prepare_data(data):
    data.remove(min(data))
    data.remove(max(data))
    return sorted(data)

data = [0, 45, 78, 98, 243]
print(prepare_data(data))

# Exercise 9 - Creation of keys in case same value repeats

def lookup_key(data, value):
    keys_with_value = [key for key, val in data.items() if val == value]
    return keys_with_value

data = {
    "key1": 100,
    "key2": 200,
    "key3": 100,
    "key4": 300
}
value = 100
print(lookup_key(data, value))

# Exercise 10 - Split list returning scores above and below average based on sample

def split_list(grades):
    if not grades:
        return ([], [])
    average = sum(grades)/ len(grades)
    below_avg = [grade for grade in grades if grade <= average ]
    above_avg = [grade for grade in grades if grade > average]

    return (below_avg, above_avg)
    
grades = [78, 56, 44, 89, 99]
below_avg, above_avg = split_list(grades)