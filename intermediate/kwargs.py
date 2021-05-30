

def fun(**kwargs):
    #print(kwargs)  #kwargs return type is dictionary
    for k,v in kwargs.items():
        print("{} : {}".format(k,v))
#dictionary unpacking
d = dict(f_name = 'shuvo', l_name = 'saha')
fun(**d)
