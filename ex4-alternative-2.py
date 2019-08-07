# set the variable car to integer 100
cars = 100
# set the variable space_in_a_car to float 4.0
space_in_a_car = 4.0
# set the variable drivers to integer 30
drivers = 30
# set the variable passengers to integer 90
passengers = 90
# set the variable cars_not_driven_ to cars - drivers (100 - 30)
cars_not_driven = cars - drivers
# set the variable cars_driven to equal drivers
cars_driven = drivers
# set the variable carpool_capacity to = cars_driven * space_in_a_car (30 * 4.0)
carpool_capacity = cars_driven * space_in_a_car
# set the variable average_passengers_per_car to = passengers / cars_driven (90/30)
average_passengers_per_car = passengers / cars_driven
# print There are 100 cars available.
print("There are {} cars available.".format(cars))
# print There are only 30 drivers available.
print("There are only {} drivers available.".format(drivers))
# print There will be 70 empty cars today.
print("There will be {} empty cars today.".format(cars_not_driven))
# print We can transport 120 people today.
print("We can transport {} today.".format(carpool_capacity))
# print We have 90 to carpool today.
print("We have {} to carpool today.".format(passengers))
# print We need to put about 3 in each car
print("We need to put about {} in each car.".format(average_passengers_per_car))