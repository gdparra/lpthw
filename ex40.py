class className: 
	def createName(self, name):
		self.name=name
	def displayName(self):
		return self.name
	def saying(self):
		print "hello %s" % self.name

first=className()
second=className()
first.createName("bucky")
second.createName("tony")
first.displayName()
first.saying()