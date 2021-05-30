
f = lambda a: a*a
result = f(5)
print(result)

g = lambda a,b: a+b

sum = g(5,6)
print(sum)

is_even = lambda a: a%2==0
print(is_even(5))

last_char  = lambda s : s[-1]
print(last_char('shuvo'))

#lamda with if else

# fun = lambda n: True if n>5 else False
fun = lambda n: n>5
print(fun(8))