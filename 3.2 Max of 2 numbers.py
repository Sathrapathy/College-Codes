num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
if num1 > num2:
    print(f'{num1} is greater than {num2}')
elif num1 == num2:
    print('Both numbers are equal')
else:
    print(f'{num2} is greater than {num1}')