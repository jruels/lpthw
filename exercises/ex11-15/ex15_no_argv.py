print "Type the filename again:"
file_again = raw_input("> ")
# assign txt_again to open the file that was provided in last step
txt_again = open(file_again)
# print out the file that was provided.
print txt_again.read()