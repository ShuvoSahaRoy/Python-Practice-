def check(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


li = [1,1,2,3,1]
li2 = [1,1,2,4,1]
li3 = [1,1,2,1,2,3]

print(check(li))
print(check(li2))
print(check(li3))

# for i,j in enumerate(range(10)):
#     print("value of i = {}\tvalue of j = {} ".format(i,j))