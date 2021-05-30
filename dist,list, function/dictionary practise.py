#cube finder
# def cube_finder(n):
#     cube = {}
#     for i in range(1,n+1):
#         cube[i] = i**3
#     return cube
#
# print(cube_finder(10))

#word counter
def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count

#name = ['shuvo', 'saha', 'roy','shuvo']
#print(word_counter(name))

print(word_counter('shuvo saha roy'))