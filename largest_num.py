
num = [5,1,3,13,6,7,10,8,9,12]
mylist = 0
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] > num[j] :
            num[j], num[i] = num[i], num[j]

print(num)


# print(mylist)

# num.sort()
# num1 = []
# for x in num[-1::-1]:
#     num1.append(x)
# print(num1[0])

