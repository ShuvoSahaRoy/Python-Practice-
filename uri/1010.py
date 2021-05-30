a,b,c = input().split()
x,y,z = input().split()
a,b,c = [int(a) , int(b), float(c)]
x,y,z = [int(x), int(y), float(z)]
print("VALOR A PAGAR: R$ {:.2f}".format(b*c + y*z))