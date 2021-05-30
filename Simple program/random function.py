import random
m=0
number = random.randint(1,5)

#for i in range(20):
i=0
while i==0:
    m+=1
    k = int(input("Guess a number"))
    if k== number:
        print("you win and u guess this number in {} times".format(m))
        print("Want to play again?\nFor yes press 0\nFor no press 1")
        i=int(input())
        if i == 0:
            m=0
            continue
        else:
            break
 #       break
    else:
        print("wrong")

