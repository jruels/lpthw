cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#print the number of cars (100)
print "There are", cars, "cars available."

#print number of drivers (30)
print "There are only", drivers, "drivers available."

#print number of cars_not_driven = cars - drivers = 100-30=70
print "There will be", cars_not_driven, "empty cars today."

#print carpool_capacity, which equals cars_driven(30), * space_in_a_car(4.0)
print "We can transport", carpool_capacity, "people today."

#print passengers(90)
print "We have", passengers, "to carpool today."

#print average_passengers_per_car(90) / cars_driven(drivers(30))
print "We need to put about", average_passengers_per_car, "in each car."