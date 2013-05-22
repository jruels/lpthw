name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about {name}.".format("name")
print "He's {height} inches tall.".format("height")
print "He's {weight} pounds heavy.".format("weight")
print "Actually that's not too heavy."
print "He's got {eyes} eyes and {hair} hair.".format(eyes,hair)
print "His teeth are usually {teeth} depending on the coffee.".format(teeth)

# this line is tricky, try to get it exactly right.
print "If I add {0}, {1}, and {2} I get {3}.".format(
age, height, weight, age + height + weight)