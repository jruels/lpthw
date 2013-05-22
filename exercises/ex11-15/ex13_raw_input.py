from sys import argv

script, first, second, third = argv

print "the script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

splash = raw_input("What does Rylinn do in the bath? ")

print "Rylinn likes to {} in the bathtub".format(splash)
