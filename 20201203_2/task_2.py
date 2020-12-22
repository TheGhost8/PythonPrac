def check_annotations(self):
	for attr, recommended_type in self.__annotations__.items():
		#if hasattr(self, attr):
			#print(attr, type(getattr(self, attr)))
		if not hasattr(self, attr) or not ((type(getattr(self, attr)) == recommended_type) or issubclass(type(getattr(self, attr)), recommended_type)):
			return False
	return True

class check(type):
	def __init__(self, *args, **kwargs):
		self.check_annotations = check_annotations
		return super().__init__(self, args, kwargs)

import sys
exec(sys.stdin.read())