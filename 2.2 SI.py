principle = int(input('Enter the principle amount : '))
time_period = int(input('Enter the time period : '))
rate = int(input('Enter the rate of interest : '))
def SI(principle, time_period, rate):
    return (principle * time_period * rate) / 100
print(f'Simple interest is {SI(principle, time_period, rate)}')