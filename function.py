# print("this is programming")
# # print("its is getting deeper")
# # print("python is the easiest")
# def exco():
#     print("this is programming")
#     print("its is getting deeper")
#     print("python is the easiest")
# def addScore(value, name):
#     result = value + 30
#     print(f"{name} scores {str(result)}")

# "New class begins with function"

def myStudents(*students):
    
    print(f"second name is {students[1]}")
    print(f"third name is {students[2]}")
    print(f'first name is {students[-1]}')

myStudents('mary', 'john', 'peace', 'whyte', 'joy', 'lucy')




def addition(num1=10 , num2= 20):
    result= num1 + num2
    print(result)


addition(20, 46)

def multiply(num1, num2):
    print(num1* num2)
    return num1 * num2

final = multiply(num1 = 20, num2 =46)*5
print(final)

divider = lambda a, b : a/b

result = divider(100 , 50) + 3

print(int(result))

def added(a):
    return lambda b : a+b
    
finalresult = added(5)
print(finalresult(10))



