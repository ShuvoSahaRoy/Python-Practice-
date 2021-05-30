a,b,c = input().split()
a,b,c = [int(a),int(b),int(c)]
d=(a+b+abs(a-b))/2
e=(d+c+abs(d-c))/2
print("{} eh o maior".format(int(e)))