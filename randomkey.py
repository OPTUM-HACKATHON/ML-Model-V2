## A basic Program to Generate Random Key
## for API 

import random 
import string 

all_strings = string.ascii_lowercase + string.digits
key = random.sample(all_strings,20)
print("".join(key))