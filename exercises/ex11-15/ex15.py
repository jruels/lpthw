# import argv module
from sys import argv
# assign script, and filename to CLI arguments
script, filename = argv
# assign 'txt' variable to open a file passed on command-line
txt = open(filename)
# print the output of the file.
print "Here's your file {0!r}: ".format(filename)
print txt.read()

# prompt for filename on command-line
print "Type the filename again:"
file_again = raw_input("> ")
# assign txt_again to open the file that was provided in last step
txt_again = open(file_again)
# print out the file that was provided.
print txt_again.read()
