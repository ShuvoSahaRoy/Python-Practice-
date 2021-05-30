import math

a,b = input().split()
c,d = input().split()
a,b,c,d = [float(a),float(b),float(c),float(d)]
e=(((c-a)*(c-a))+((d-b)*(d-b)))
print("{:.4f}".format(math.sqrt(e)))