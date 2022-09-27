print("Exercise 1")
print("Marissa S.")
print("8 Center St,Bristol,RI,02809")
print("401-410-7315")
print("Major: Computer Science!")
# Exercise 2
profit = 0.23
total_sales = float(input("Enter the total amount of sales."))
total_profit = total_sales * profit
print("Your total sales profit is: $", total_profit)
# Exercise 3
one_acre = 43560
square_feet = float(input('How many square feet in this land? '))
land = square_feet / one_acre
print('This is equal to', format(land, ',.14f'), 'acres')
# Exercise 4
sales_tax = 0.07
item1 = float(input('Price for Item 1: $'))
item2 = float(input('Price for Item 2: $'))
item3 = float(input('Price for Item 3: $'))
item4 = float(input('Price for Item 4: $'))
item5 = float(input('Price for Item 5: $'))
subtotal = float(item1 + item2 + item3 + item4 + item5)
total_tax = subtotal * sales_tax
total = subtotal + total_tax
print()
print('The subtotal is: $' + format(subtotal, ',.17f'))
print('The total tax is: $' + format(total_tax, ',.17f'))
print('The total amount due is: $' + format(total, ',.17f'))
# Exercise 5
speed = 70
print("The car is moving 70mph")
time = float(input('How many hours is the car traveling? '))
distance = speed * time
print('The distance covered is equal to', format(distance, ',.14f'), 'miles')
# Exercise 6
statetax = 0.05
countytax = 2.5
item = float(input('Price for purchase: $'))
statetaxtotal = item * statetax
countytaxtotal = item * countytax
saletaxtotal = statetaxtotal + countytaxtotal
completetotal = item + countytaxtotal + statetaxtotal
print()
print('The state tax total is: $' + format(statetaxtotal, ',.39f'))
print('The county tax total is: $' + format(countytaxtotal, ',.40f'))
print('The total sales tax is: $' + format(saletaxtotal, ',.41f'))
print('The total amount due is: $' + format(completetotal, ',.42f'))
# Exercise 7
gas = float(input("How many gallons of gas used?: "))
miles = float(input("How many miles traveled?: "))
mpg = miles / gas
print('Miles per gallon is : ' + format(mpg, '.52f'))
# Exercise 8
mealcost = float(input('How much is the meal?: $'))
mealtax = 0.07
tip = 0.18
mealtaxtotal = mealtax * mealcost
mealtiptotal = tip * mealcost
mealtotal = mealcost + mealtiptotal + mealtaxtotal
print("The meal total is: $" + format(mealtotal, '.61f'))
# Exercise 9
celsius = float(input('What is the temp in celsius? '))
farenheit = ((5/9) * celsius) + 32
print()
print("In farenheit that equals, " + format(farenheit, ".64f"))
# Exercise 10

