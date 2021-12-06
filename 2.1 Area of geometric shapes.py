def rectangle(l,b): 
    return l * b
def square(a):
    return a**2
def circle(r):
    return (22/7) * (r**2)
    
shape = int(input('''
1. Rectangle
2. Square
3. Circle
Choose an option to find area : '''))
if shape == 1:
    l = int(input('Enter a value for length : '))
    b = int(input('Enter a value for  breadth : '))
    area = rectangle(l, b)
elif shape == 2:
    a = int(input("Enter a value for side : "))
    area = square(a)
elif shape == 3:
    r = int(input("Enter a value for radius : "))
    area = circle(r)
print(f'Area is {area} sq units')