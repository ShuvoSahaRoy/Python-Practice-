
l = [1,2,3,4,5,6,7]
lenth = len(l)
for i in range(lenth):
    for j in range(i+1, lenth):
        print(l[i],l[j])