# def my_function(fname,mname, lname):
#     print(f"His name is {fname} {mname} {lname}.")

# my_function("Santosh", "Kumar", "Chapagain")


#default argument
# def student(name,age,grade="Ten"):
#     print(f"student details: {name},{age},{grade}")
# student("Santosh", 20)

# def student1(name,age,grade="Ten"):
#     print(f"student details: {name},{age},{grade}")
# student("Santosh",35,"Bachelors")

#keyword argument
# def student2(name,age,grade):
#     print(f"student details: {name},{age},{grade}")
# student2("Santosh",50,grade="Masters")

#positiona Argument
# def add(x,y,z):
#     return x+y+z
# print(add(10,20,5))



# def student3(name,address,college,grades):
#     print("Student details:", name,address,college,grades)
# student3(grades="Masters", address="Kathmandu",college="ABC",name="Santosh")


#arbitrary arguments, *args
# def my_function1(*person):
#     print(f"The coolest person is {person[2]}")
# my_function1("Vinicius","Rodrygo","Neymar")

#Arbitrary KeyWord Arguments, **Kwargs

# def my_function2(**person):
#     print("His last first name is", person["fname"])
# my_function2(lname= "Messi", fname="Lionel")



# def adder(*num):
#     sum2= 0
#     for n in num:
#         sum2 = sum2+n
#     print("sum:",sum2)
# adder(10,2,3,4)
# adder(11,22,33,44,55)
# adder(11,22,33)


# def add_num(num1,num2):
#     sum1 = num1+num2
#     return sum1
# result = add_num(10,20)
# print("sum:",result)

# def get_square(num):
#     return num*num
# for i in range(1,10):
#     result = get_square(i)
#     print("square of",i,"=",result)


# def details(roll):
#     a = [22,23,44,55,66]
#     if roll in a:
#         print(f"Roll number {roll} is present.")
#     else:
#         print(f"Roll number {roll} is absent.")
# roll = int(input("Enter the roll number."))
# details(roll)

# def max1(x,y,z):
#     if x>y and x>z:
#         return x
#     elif y>x and y>z:
#         return y
#     else:
#         return z
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))
# print("The maximum value is",max1(x,y,z))


# def count(val):
#     vov = 0
#     con = 0
#     for i in range(len(val)):
#         if val[i] in ["a","e","i","o","u"]:
#             vov+=1
#         else:
#             con+=1
#     print("Count of vowel is: ", vov)
#     print("Count of consonant is: ",con)
# x = input("Enter value: ")
# count(x)

# def myfunction(num):
#     rev = 0
#     while(num>0):
#         digit= num%10
#         rev =(rev*10)+digit
#         num= num//10
#     return rev
# print(myfunction(4567))

def outer_fun():
    x=777
    def inner_fun():
        global y
        y= 100
        x=700
        print("inside inner function:",x,y)
    inner_fun()
    def myfun():
        print("**************",y)
    myfun()
    print("inside outer function",x)
outer_fun()
