#user input for the size of the shape
shape = input("Enter the shape: ")
shape = str(shape)

length = input("Enter the length: ")
length = float(length)

width = input("enter the width: ")
width = float(width)

if shape == 'rectangle':
    print(f"The area of the rectangle is {length*width}")
elif shape == 'square':
    print(f"The area of the square is {length**2}")