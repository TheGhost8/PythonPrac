from re import match

nums = input().replace(" ", "").split(sep=',')
for i in nums:
	print((match(r"^([-+]?)(\d+)(\.(\d)*)?((e|E)([+-]?)(\d)+)?$", str(i)) is not None) or 
		  	 	(match(r"^([-+]?)(\d*)(\.(\d)+)?((e|E)([+-]?)(\d)+)?$", str(i)) is not None) and (match(r"^$", str(i)) is None))