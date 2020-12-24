from re import sub, search

print(sub(r"(?<=0)([1-9]{2,4})(?=0)([0-9]*?)(?<=0)([1-9]{2,4})(?=0)", r"\3\2\1",input()))