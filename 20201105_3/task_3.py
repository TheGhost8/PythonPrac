from re import sub

print(sub(r"(0[1-9]{2,4}(?=0))", r"", input()))