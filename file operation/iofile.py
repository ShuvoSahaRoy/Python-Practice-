f = open('file.txt')
# print(f'cursor position - {f.tell()}')
print(f.read())
print(f'cursor position - {f.tell()}')
f.seek(0)
print(f'cursor position - {f.tell()}')
# print(f.readline())

lines = f.readlines()
# print(lines)
print(len(lines))

#print(f.read())

print(f.name)
print(f.closed)

f.close()