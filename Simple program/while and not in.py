name = input()
i=0
temp = ""
while i<len(name):
    if name[i] not in temp:
        temp += name[i]
        print("# {} : {}".format(name[i], name.count(name[i])))
    i+=1