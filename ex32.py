the_count=[1,2,3,4,5]
fruits=['aples','oranges','pears','apricots']
change=[1,'penies',2,'dimes',3,'quarters']

#This firt kind of for loop goes through a list
for number in the_count:
	print "This is count %d" %number

#same as above
for fruit in fruits:
	print "A fruit of type %s" %fruit

for i in change:
	print "I got %r" %i

#we can also build lists, first start with an empty one 
elements=[]

#then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list" %i
	elements.append(i)

for i in elements:
	print "Element was %d" %i
