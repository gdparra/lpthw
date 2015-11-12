class Parent(object):
   def implicit(self):
      print "Parent implicit()"

class Child(Parent):
   pass

dad=Prent()
son=Child()

dad.implicit()
son.implicit()
print "End"
