def check_annotations(self):
	result = True
	for attr, recommended_type in self.__annotations__.items():
		#print(type(getattr(self, attr)), attr, recommended_type)
		if hasattr(self, attr):
			print(type(type(getattr(self, attr))))
		if not hasattr(self, attr) or not (type(getattr(self, attr)) == recommended_type):
			result = False
		#result = result and (type(attr) == recommended_type)# and hasattr(self, attr)
	return result

class check(type):
	def __init__(self, *args, **kwargs):
		self.check_annotations = check_annotations
		return super().__init__(self, args, kwargs)

class C(metaclass=check):
    A: int
    B: str = "QQ"

c = C()
print(c.check_annotations())
c.A = "ZZ"
print(c.check_annotations())
c.A = 100500
print(c.check_annotations())
c.B = type("Boo",(str,),{})(42)
print(c.check_annotations())