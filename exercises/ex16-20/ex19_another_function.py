def cars_and_bikes(saab, motorcycle):
    print "I have {:d} Saab.".format(saab)
    print "I have {:d} Motorcycle".format(motorcycle)

print "direct:"
cars_and_bikes(1, 1)

print "variables:"
number_saab = 1
number_moto = 1

cars_and_bikes(number_saab, number_moto)

print "combine variables and math: I wish I had this many"
cars_and_bikes(number_saab + 4, number_moto + 1)

print "math:"
cars_and_bikes(0 + 1, 1 + 0)
