def No_Dup(listA):
    No_Duplicate = set(listA)
    print (No_Duplicate)

import random
number = random.randint(1,30)
elements = random.sample(range(1,number+1), number)
listA = [x for x in elements]
No_Dup(listA)
