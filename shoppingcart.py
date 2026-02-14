foods =[]
prices = []
total = 0
while True:
    food = input('enter the food you want to order:')
    price = float(input('enter the price of the food:'))
    foods.append(food)
    prices.append(price)
    total += price
    more = input('do you want to order more? (yes/no):')
    if more.lower() != 'yes':
        break
print('--- YOUR CART ---')
for i in range(len(foods)):
    print(f'{foods[i]} - ${prices[i]}')
print(f'total: ${total}')