def person(name, **data):

    print(name)
    #print(data)

    for i,j in data.items():
        print(i,j)

person("shuvo", age=25, city ='Mumbai', mob = 1963102700)