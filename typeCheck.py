
def TypeCheck(n):
    if isinstance(n,list):
        print(f"{n} is a list.")
    elif isinstance(n,dict):
        print(f"{n} is a dictionary.")
    elif isinstance(n,tuple):
        print(f"{n} is a tuple.")
    elif isinstance(n,str):
        try:
            str1 = eval(n)
            TypeCheck(str1)
        except (NameError,SyntaxError):
            print(f"{n} is a string.")
        
    elif isinstance(n,set):
        print(f"{n} is a set.")
    elif  isinstance(n,int):
        print(f"{n} is a integer.")
    elif isinstance(n,float):
        print(f"{n} is a float.")
n= "1,2,3"

TypeCheck(n)

def pos_num(a):
    if a<0:
        return -a
    else:
        return a

a=-500
print(pos_num(a))




# a1= "[1,2,3,4,5]"
# print(type(a1.splitlines()))
# print(type(a1.strip("][").split(',')))
# print(type(eval(a1)))
# a2 = "(1,2,3,4,5)"
# print(type(eval(a2)))
# a3 = "{
# }"
# a2 = list(a1)
# print(type(a2))

# c = "{1,2,3,4,5}"
# d = set(c)
