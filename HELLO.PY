#user input for the size of the shape
shape = input("Enter the shape: ")
shape = str(shape)

#user input for the length
length = input("Enter the length: ")
length = float(length)

#user input for the width
width = input("enter the width: ")
width = float(width)

#conditional statement for the code to show different result according to the users input
if shape == 'rectangle':
    print(f"The area of the rectangle is {length*width}")
elif shape == 'square':
    print(f"The area of the square is {length**2}")
