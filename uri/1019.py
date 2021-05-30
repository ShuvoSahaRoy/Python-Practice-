t = int(input())
h = int(t / 3600)
t = t - (h * 3600)
m = int(t / 60)
t = t - (m * 60)
print("{}:{}:{}".format(h,m,t))

