x= 10
if x>5:
    raise Exception(f"x should not exceed 5. The value of x was:{x}")

while True :
    print("Hello World") #SyntaxError: invalid syntax



def divide(x, y):
	try:
		result = x /y
		print("Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
divide(3, 0)




try:
	age = int(input("Enter your age: "))
	if age>=18:
		print("You are eligible to vote.")
	else:
		print("you are not eligible to vote.")
except Exception as e:
	print("ERROR!!!Please enter your age in neumeric character.", e)
print("Some important line of codes.")



IndexError and ValueError
def access_index_value(a):
      namelist = ["Rakesh", "Santosh","Hari", "Shyam", "Ramesh"]
      try:
        print(namelist[int(a)])
      except IndexError as ne:
        print("Error!!! Index is out of bond.",ne)
      except ValueError as e:
        print("Sorry!! you are suppose to enter index as integer value.", e)
a = input("Enter the index:")
access_index_value(a)

keyError
def my_dict(y):
   info = {
      "name":"Rakesh kumar",
      "mail":"rakesh@gmail",
      "number": 982834883
   }
   try:
      print(info[y])
   except KeyError:
      print("Error occured!! Key you want to access is unavailable")
y = input("Enter the value:")
my_dict(y)


# Try, except, else and finally
try :
    x1 = input("Enter the first number: ")
    y1 = input("Enter the second number: ")
    z = int(x1)/int(y1)
except ZeroDivisionError:
    print("Error!!Division by 0 is not accepted.")
except ValueError:
    print("Error!!Enter neumeric character.")
else:
    print("Division:",z)
finally:
    print("This is finally block")

# Raising an Exception

def value_range(a1):
    try:
        if a1>100:
            raise ValueError(a1)
    except ValueError:
        print(f"{a1} is out of allowed range.")
    else:
        print(f"{a1} is within the allowed range.")
a1 = int(input("Enter a number upto 100: "))
value_range(a1)


def person_(age):
    try:
        if int(age)<5:
            raise ValueError("Not allowed, Your age is less than 5")
        if int(age)>20:
            raise ValueError("Not allowed, your age is greater than 20")
    except ValueError as e:
        print("Value Error exception thrown", e)
age = input("Enter your age: ")
age(age)


