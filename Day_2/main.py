print(1+2)
print(1-2)
print(1*2)
print(1**2)
print(1/2)
print(1%2)
print(1//2)
print("------------------------------------------------------")
print(5 > 3)
print("------------------------------------------------------")

print(True and True)
print(True or False)
print(not True)
print(2 and 3)
print(2 or 1)
print("------------------------------------------------------")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

print("{0} + {1} = {2}".format(a, b, a+b))
print("{0} - {1} = {2}".format(a, b, a-b))
print("{0} * {1} = {2}".format(a, b, a*b))
print("{0} ** {1} = {2}".format(a, b, a**b))
print("{0} / {1} = {2}".format(a, b, a/b))
print("{0} // {1} = {2}".format(a, b, a//b))
print("{0} % {1} = {2}".format(a, b, a%b))

print("------------------------------------------------------")

age = 40
print(f"I am {age}")
print("I am {}".format(age))

print("------------------------------------------------------")

s = "hello world"

s = s.upper()
print(s)
s = s.capitalize()
print(s)
s = s.title()
print(s)

new_string = s.split()
print(new_string)

a, b = map(str, new_string)
print("a = {0}, b = {1}".format(a, b))