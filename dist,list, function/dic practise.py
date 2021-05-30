# Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
# credits = sum(val for val in Junior.values())
#
# str1 = "peter piper picked a peck of pickled peppers"
# freq = {}
# for char in str1:
#     if char not in freq:
#         freq[char] = 0
#     freq[char] += 1
# print(freq)
#
# s1 = "hello"
#
# counts = {}
# for char in s1:
#     if char not in counts:
#         counts[char] = 0
#     counts[char] += 1
# print(counts)
#
# str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
#
# freq_words = {}
# for word in str1.split():
#     if word not in freq_words:
#         freq_words[word] = 0
#     freq_words[word] +=1
# print(freq_words)
#
# sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
#
# wrd_d = {}
# for word in sent.split():
#     if word not in wrd_d:
#         wrd_d[word] = 0
#     wrd_d[word] +=1
# print(wrd_d)
#
# sally = "sally sells sea shells by the sea shore"
#
# characters = {}
# for char in sally:
#     if char not in characters:
#         characters[char] = 0
#     characters[char] += 1
#
# for k,v in characters .items():
#     if v == max(characters .values()):
#         best_char = k
# print(best_char)

# sally = "sally sells sea shells by the sea shore and by the road"
# 
# characters = {}
# for i in sally:
#     characters[i] = characters.get(i, 0) + 1
# 
# print(sorted(characters.items(), key=lambda x: x[1]))
# worst_char = sorted(characters.items(), key=lambda x: x[1])[-13][0]
# print(worst_char)

# string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
# letter_counts={}
# for i in string1.lower():
#     if i not in letter_counts:
#         letter_counts[i]=0
#     letter_counts[i]=letter_counts[i]+1
#
#
# p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
# low_d={}
# for i in p.lower():
#     if i not in low_d:
#         low_d[i]=0
#     low_d[i]=low_d[i]+1

# tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
# country = list()
# for c in tuples_lst:
#     country.append(c[1])
# print(country)


# gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
#
# num_medals = [values for values in gold.values()]
# print(num_medals)

# def check_nums(l):
#     ll = []
#     i = 0
#
#     while len(l) > i:
#         if l[i] == 7:
#             break
#         else:
#             ll.append(l[i])
#             i += 1
#     return ll
# print(check_nums([0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]))

# def sublist(list):
#     i = 0
#     sub = []
#     while i < len(list):
#
#         if (sub[i] == 'STOP'):
#             break
#         sub = list
#         i+=1
#     return sub
# print(sublist(['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']))


# def beginning(inputstr):
#     d = 0
#     x=[]
#     str1 = list(inputstr)
#     while d<len(inputstr) :
#         if str1[d] == 'bye' :
#             break
#         else:
#             x.append(str1[d])
#             d+=1
#     if len(x)<10:
#             return x[:len(x)]
#     return x[:10]
#
#
# print(beginning(['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']))
#
# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))
# print(f(4, ["Hello"]))
# print(f(5, ["Hello"]))
#
# def test(a, b = True, dict1 = {2:3,4:5,6:8} ):
#     if a in dict1.keys() and b == True:
#         return dict1[a]
#     else:
#         b= False
#         return b
#
# print(test(2))

# L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
#
# key = lambda k: k[x]
# print(key(L))

# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
# top_three = sorted(medals.values(), key = lambda x: medals[x], reverse=True)


# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
# top_three = sorted(medals.keys(),key=lambda x : medals[x],reverse = True)[:3]
# print(top_three)

# groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
# most_needed = sorted(groceries.keys(), key=lambda x: groceries[x], reverse = True)


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
def last_four(x):
    return (str(x)[-4:])

last_four(ids)
sorted_ids = sorted(ids, key=last_four)
print(sorted_ids)

# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
#
# sorted_id = sorted(ids, key=lambda x: str(x)[-4:])