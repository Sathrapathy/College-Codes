a = int(input('Enter the coefficient of x^2 : '))
b = int(input('Enter the coefficient of x : '))
c = int(input('Enter the value of constant term : '))
x1 = (-b + (b**2 - (4*a*c))**(1/2)) / 2*a
x2 = (-b - (b**2 - (4*a*c))**(1/2)) / 2*a
print(f'The value of x are {x1}, {x2}')