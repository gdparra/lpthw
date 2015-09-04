#This is like your script with argv
def print_two(*args):
	arg1,arg2=args
	print "arg1: %r, arg2: %r" %(arg1,arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1,arg2)

#This one takes just one argument
def print_one(arg1):
	print "arg1: %r" %(arg1)

#This prints none
def print_none():
	print "I print nothing"

print_two("Gonzalo","Saly")
print_two_again("Gonzalo","Saly")
print_one("Saly")
print_none()
