# Ethan Lawrence
# Jan 8 2025
# build and display

def get_city():
    return input('Please enter the name of the city you live in:    ')
def get_age():
    return input('Please enter your age:    ')
def build_output(city, age):
    return f'You live in {city} and you are {age} years old.'

user_city = get_city()
user_age = get_age()
print(build_output(user_city, user_age))