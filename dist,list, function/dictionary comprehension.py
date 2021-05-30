# square = {num:num**2 for num in range(1,11)}
# print(square)
# square = {f"Square of {num} is":num**2 for num in range(1,11)}
# for k,v in square.items():
#     print("{}:{}".format(k,v))

# s = "shuvo saha roy"
# letter_count = {char : s.count(char) for char in s}
# print(letter_count)

even_odd = {i: ('even'+ '\n' if i%2 == 0 else 'odd\n') for i in range(1,11)}
print(even_odd)