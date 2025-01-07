# Ethan Lawrence
# Jan 7 2025
# Functions as batons

def welcome():
    return'Hello and welcome to my room area calcualtor script!'

def find_length():
    while True:
        length = input('Enter the length of the room: \n')
        if length.isdigit():
            break
    return int(length)

def find_width():
    while True:
        width = input('Enter the width of the room: \n')
        if width.isdigit():
            break
    return int(width)
def find_area(width, length):
    return width * length
def display_area(area):
    return f'The area of the room is {area} ft^2'
def end_script():
    return 'Thank you for using my script (:)'

welcome()
print(display_area(find_area(find_width(), find_length())))
end_script()