from itertools import *
print(*iter(sorted([str().join(i) for i in product('TOR', repeat=(int)(input())) if (str().join(i)).count('TOR') == 2])))