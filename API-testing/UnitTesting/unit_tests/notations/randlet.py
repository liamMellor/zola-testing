import random
import string

def getCode(length = 10, char = string.ascii_uppercase + string.digits + string.ascii_lowercase ):
    return ''.join(random.choice( char) for x in range(length))

print getCode(20, "mychars")

