#implicit Type Casting.
integer_number = "10"
intnumber = 10
print(integer_number+intnumber)
float_number = 20.20
new_number = integer_number+float_number
print(new_number)
print(type(new_number))

#Explicit Type Casting
num_string = "12"
num_integer = 20
print(type(num_string))
num_string = int(num_string)#explicit type conversion
print(type(num_string))
num_sum = num_string+ num_integer
print(num_sum)
print(type(num_sum))


user_input = input("Enter numbers: ")
print(type(user_input), user_input) #String
user_input = int(user_input) #Type conversion
print(type(user_input), user_input) #Integer


#Type Casting
#converting string into tuple
strType = "Hello World!!"
TupleType =  tuple(strType)
print(type(TupleType),TupleType)


#Converting string into set
setType = set(strType)
print(type(setType), setType)

#converting string into list
listType = list(strType)
print(type(listType), listType)

# print(0/0)