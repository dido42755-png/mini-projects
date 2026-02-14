

import pprint


principle = 0
rate = 0
time = 0
while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle must be greater than zero. Please try again.")
while rate <= 0:
    rate = float(input("Enter the interest rate (as a percentage): "))
    if rate <= 0:
        print("Interest rate must be greater than zero. Please try again.")
while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero. Please try again.")
rate = rate / 100
amount = principle * (1 + rate) ** time
print(f"The amount after {time} years is: {amount:.2f}")

total = principle * pow((1 + rate), time)
print(f"The total amount after {time} years is: {total:.2f}")