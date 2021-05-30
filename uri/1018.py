x=int(input())
print(x)

print("{} nota(s) de R$ 100,00".format(int(x/100)))
y = x%100
print("{} nota(s) de R$ 50,00".format(int(y/50)))
y = y%50
print("{} nota(s) de R$ 20,00".format(int(y/20)))
y = y%20
print("{} nota(s) de R$ 10,00".format(int(y/10)))
y = y%10
print("{} nota(s) de R$ 5,00".format(int(y/5)))
y = y%5
print("{} nota(s) de R$ 2,00".format(int(y/2)))
y= y%2
print("{} nota(s) de R$ 1,00".format(int(y/1)))