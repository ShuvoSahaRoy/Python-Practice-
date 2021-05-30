# fruits = ['grapes' , 'mango' , 'apple']
# # fruits.sort()
# # print(fruits)
#
# fruits2 = ('grapes' , 'mango' , 'apple')  #this is a touple
# print(sorted(fruits2))   #touple is immutable. so we can't change it

fruits3 = ['grapes', 'mango', 'apple']

guitars = [
    {'model': 'yamaha f310', 'price': 8400},
    {'model': 'signature', 'price': 5400},
    {'model': 'yamaha', 'price': 7400},
    {'model': 'Gibson', 'price': 6400}
]

# print(sorted(guitars, key=lambda d:d['price']))
print(sorted(guitars, key=lambda d: d['price'], reverse=True))
