from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda n: n%2 == 0, nums))

doubles = list(map(lambda n: n*2,evens))

addsum = reduce(lambda n,m: n+m,doubles)

print(doubles)
print(evens)
print(addsum)