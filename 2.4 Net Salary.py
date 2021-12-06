basic_pay = int(input('Enter the basic pay amount : '))
dearness_allowance = basic_pay * 0.05
house_rent_allowance = basic_pay * 0.1
allowance = dearness_allowance + house_rent_allowance
tax = basic_pay * 0.2
net_salary = basic_pay + allowance - tax
print(f'Net salary is {net_salary}')