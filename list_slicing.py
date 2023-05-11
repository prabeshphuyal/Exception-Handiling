# user_input= int(input("Enter value."))
# if user_input==50:
#     print("100")
# elif user_input==100:
#     print("50")

mylist = [4,3,8,5,10,7]
# even_list = []
# odd_list = []
# for x in mylist:
#     if x%2==0:
#         even_list.append(x)
#     else:
#         odd_list.append(x)
# print(even_list)
# print(odd_list)
mylist1= [i for i in mylist if i%2==0 ]
print(mylist1)