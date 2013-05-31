from sys import argv

script, filename = argv

print "Let's read file {0!r}.".format(filename)

target = open(filename)

print "Below is the contents of {}.\n".format(filename)

print target.read()

print "And finally, we close it."
target.close()
