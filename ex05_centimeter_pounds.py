my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
#my_height_inches = 74 # inches
my_height_centimeters = 74  / 0.39370 # centimeters
#my_weight_lbs = 180 # lbs
my_weight_kilos = 180 / 2.2 # kilos
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
#print "He's %d inches tall." % my_height_inches
print "He's %d centimeters tall." % my_height_centimeters
#print "He's %d pounds heavy." % my_weight_lbs
print "He's %d kilos heavy." % my_weight_kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height_centimeters, my_weight_kilos, my_age + my_height_centimeters + my_weight_kilos)