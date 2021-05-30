# def count_letters(word_list):
#     letter_count={}
#     for word in word_list:
#         for char in word:
#             if char in letter_count:
#                 letter_count[char] += 1
#             else:
#                 letter_count[char] = 1
#     return letter_count
#
# monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
#
# monty_words = monty_quote.split(" ")
# m = count_letters(monty_words)
# for key in sorted(m.keys(), key= lambda x: m[x] ):
#     print("{} {}".format(key, m[key]))
#
#
instructor_ratings = {"Joe" : "awesome", "Scott" : "hmmm..."}
print(instructor_ratings['jo'])