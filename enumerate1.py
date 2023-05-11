# mobiles = ["samsung","oppo","vivo","redmi"]
# newlist = []
# for index, mobile in enumerate(mobiles):
#     newlist.append(f"{mobile},({index}) ")
# print(newlist)

# colors = ["red","green", "blue","yellow"]
# newdict = {}
# for i, color in enumerate(colors):
#     newdict[color] =i
# print(newdict)

# brands = ["samsung","oppo","vivo","redmi"]
# newlist1= []
# for x, brand in enumerate(brands):
#     newlist1.append(f"{brand}:{x}")
# newtuple = tuple(newlist1)
# print(newtuple)

#Remove duplicates item and print their index

brands1 = ["samsung","oppo","samsung","vivo","oppo","redmi"]
# for i in range(len(brands1)):
#     if i==3:
#         brands1.remove("samsung")
#     elif i==5:
#         brands1.remove("oppo")
# print(brands1)

# newset = set(brands1)
# print(newset)

# newbrands = []
# for index,values in enumerate(brands1):
#     if values not in newbrands:
#         newbrands.append(values)
#         print(index,values)



# dict_1 = {"a":10, "b":20, "c":30, "d":40, "e":50}
# dict_2 = {"a":1, "d":4}
# dict3= {**dict_1,**dict_2}
# print(dict3)

# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# newdict = {}
# for i in (dict1,dict2,dict3):
#     newdict.update(i)
# print(newdict)

# mydict = {
#     "a":20,
#     "b":30,
#     "c":10,
#     "d":40
# }
# sum_count=0
# for i in mydict.values():
#     sum_count=sum_count+i
# print(sum_count)


# mydict2 = {
#     "a":20,
#     "b":30.45,
#     "c":"cat",
#     "d":40
# }
# sum_count2 = 0
# for x in mydict2.values():
#  if x != "cat":
#     sum_count2 = sum_count2+x
# print(sum_count2)

# sum_count2 = 0
# for x in mydict2.values():
#     if type(x)!=str:
#         sum_count2 = sum_count2+x
# print(int(sum_count2))

# # mylist = [2,3,4,5,2,3,4]
# # newlist = []
# # for i in mylist:
# #     if i not in newlist:
# #         newlist.append(i)
# # print(newlist)
# # print(set(mylist))

# x="i dont love football"
# y="i love football have"
# x1=x.split()
# y1=y.split()
# commonlist = []
# uniquelist = []
# for letter in x1:
#     if letter in y1:
#         commonlist.append(letter)
#     else:
#         uniquelist.append(letter)
# for letter1 in y1:
#     if letter1 in x1:
#         commonlist.append(letter1)
#     else
#         uniquelist.append(letter1)
# print(commonlist)
# print(uniquelist)


# size = 10
# mylist = []
# for i in range(size):
#     mylist.append(int(input("Enter the Elements:")))
#     if 10<=mylist[i]<=12:
#         mylist[i]=10
#     else:
#         mylist[i]

# print(mylist)
# 

# x="i dont love football"
# y="i love football have"
# x1 = x.split()
# y1 = y.split()
# common = set(x1).intersection(set(y1))
# print(common)
# unique = set(x1).symmetric_difference(set(y1))
# print(unique)

# mydict = {
#     "k1":"v1",
#     "k2":"v2",
#     "k3":"v3"
# }
# newdict = {}
# newdict1= {}
# newdict1["values"]= "hello"
# for keys,values in mydict.items():
    # dict1 = {values:keys}
    # newdict.update(dict1)
    # newdict1[values]=keys

# newdict2 = {v:k for k,v in mydict.items()}
# mydict["k4"]= "v5"
# print(mydict)

# a ={
#     "a":20,
#     "b":30,
#     "c":40
# }
# b = {
#     "a":1,
#     "d":50
# }
# a["a"] = 50
# for i,v in b.items():
#     print(i)
#     a[i] = v
# print(a)


# keys = ["a", "b","c","d"]
# values = [20,30,40,50]
# mydict = {}
# for i in keys:
#     for j in values:
#         mydict.update({i:j})
# print(mydict)

# size = int(input("Enter the size:"))
# a= []
# for x in range(size):
#     elements = input("enter the elements: ")
#     a.append(elements)
# for i in range(size):
#     for j in range(0,size-i-1):
#         if a[j]> a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1]= temp
# print(a)


#Second highest value

# mylist = [11,2,5,6,7,9,8,9,10,12,18]
# mylist.sort()
# print(mylist[-2:-1])
# if mylist[0]>mylist[1]:
#     print(mylist[1])
# elif mylist[1]>mylist[2]:
#     print(mylist[2])
# else:
#     print(mylist[3])


# txt= "my name is don"
# txt2=txt.replace(" ", "")
# value_count = {}
# for i in txt2:
#     value_count[i] = value_count.get(i,0)+1
    # if i not in value_count:
    #     value_count[i]=1
    # else:
    #     value_count[i]+=1

# print(value_count)
        

# Palindrome number-1

# user_input =input("Enter the number:")
# a = int(user_input[-1::-1])
# if str(a==user_input):
#     print(f"Given number {user_input} is palindrome.")
# else:
#     print(f"Given number {user_input} is not palindrome.")

# my_dict = {
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40,
#     "e":60
# }
# max_value = my_dict["d"]
# for value in my_dict:
#     if max_value>my_dict[value]:
#         max_value = my_dict[value]
# print(max_value)


#max value
# my_dict = {
#     "a":10,
#     "b":"banana",
#     "c":30,
#     "d":40
# }
# max_value = 0
# for value in my_dict.values():
#     if type(value)!= str and max_value<value:
#         max_value = value
# print(max_value)

#min value

my_dict = {
    "a":10,
    "b":"banana",
    "c":30,
    "d":40
}
min_value = my_dict["d"]
for value in my_dict.values():
    if type(value)!= str and min_value>value:
        min_value = value
print(min_value)



time = int(input("Enter the time in seconds: "))
mins=time//60
print("***********",mins)
sec=time%60
print("!!!!!!!!!!!",sec)
print(f"{mins} minute,{sec}Seconds")


my_list = [{"a":10, "b":20},{"c":40, "d":50}]
