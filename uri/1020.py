days = int(input())

y=int(days/365)
y1 = days%365
m =int(y1/30)
m1 = y1%30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(y,m,m1))