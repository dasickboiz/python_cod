# range(start, stop, step)

a = range(1, 10, 3)
for i in a:
    print(i, end = " ")
print("\n")

# duyet cac so tu 1 den 100
sum = 0;
for i in range(1, 51):
    print(i, end = " ")
    sum += i
print("\n")
print("Sum = ", sum)

for i in range(1, 21):
    if(i % 7 == 0):
        break
    else:
        print(i, end = " ")
print("\n")

for i in range(1, 21):
    if(i == 19):
        continue
    print(i, end = " ")

print("\n")

for i in range(3):
    for j in range(4):
        print(i,j)

print("\n")
n = 10
i = 1
while i < n:
    print("i = " , i)
    i += 1

print("\n")
n = 1000000
dem = 0
while n != 0:
    dem += 1
    n = n // 10
print("n = ", dem)

m = 98765
tong = 0
while n != 0:
    m = n % 10
    tong += m
    m //= 10
print("tong = ", tong) 

a = 12345
rev = 0
while a != 0:
    temp = a % 10
    rev = rev * 10 + temp
    a //= 10
print("Rev = ", rev)