# a = [1,2,3,4]
# b = 'sample string'

# print(str(a))
# print(repr(a))

# print(str(b))
# print(repr(b))

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print(f"{str(a)}")
print(f"{str(b)}")

print(f"{repr(a)}")
print(f"{repr(b)}")