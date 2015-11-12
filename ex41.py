class Human():
   def __init__(self, name, gender):
      self.name=name
      self.gender=gender
   def speak_name(self):
      print "My name is %s" % self.name
      
will=Human("William", "Male")
print will.name
print will.gender
will.speak_name()   
   