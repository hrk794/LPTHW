# The total number of cars available is 100 and is assigned to variable named cars
cars = 100

# The space available in a single car is 4 and is assigned to the variable space_in_a_car
space_in_a_car = 4.0

# The total number of drivers available today is 30 and is assigned to the variable named drivers
drivers = 30

# The total number of passengers today is 90 and is assigned to the variable named passengers
passengers = 90

# The number of empty cars is equal to number of cars available - number of drivers available, and is assigned to variable cars_not_driven
cars_not_driven = cars - drivers

# The number of driven cars is equal to the number of drivers available today and is assigned to the variable cars_driven
cars_driven = drivers

# The car pool capacity is given by driven cars multiplied by the space available in a single car, assigned to the variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers pert car is given by total number of passengers divided by number of driven cars, assigned to the variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car,"in each car."

