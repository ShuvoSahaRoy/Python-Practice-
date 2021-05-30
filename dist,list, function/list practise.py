list1 = [1,2,4,5,6,7,9]

list2 = ["amar","tumar","tar","shimul","shuvo","saha"]

list3 = ["eta","mixed",5,6,3,6,'c']

print(len(list2))

print(list1[1])
print(list2[3])
print(list3[-1])

list3[6] = 66   #we can change index value
print(list3)

list3[1:] = ['new','item']  #we can change list
print(list3)

number = [1,2,3,4,5,1]
print(number.count(1))
number.append(5)
print(number)

number.insert(1,110) # for insertion in particular index
print(number)

print(list3+number) # we can add lists
# extand method
list1.extend(number)
print(list1)

num = list(range(1,11))
print(num)
