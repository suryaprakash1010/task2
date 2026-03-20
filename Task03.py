# loop basics 
#task (1-10)
# print numbers from 1 to 50
for i in range(1,51):
    print(i)

# even numbers from 1 to 100
for i in range(2,101,2):
    print(i)

# odd numbers from 1 to 100
for i in range(1,101, 2):
    print(i)

# multiplication table of 7
for i in range(1,11):
    print( f"7 * {i} = {7*i}")

# sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
    print("sum:", total)

# numbers from 50 to 1 (reverse)
for i  in range(50, 0, -1):
    print(i)

#numbres divisible by 3(1-100)
count = 0 
for i in range (1,101):
    if i % 3 == 0:
        count += 1
        print("count:", count)

#square num from 1-10
for i in range(1,11):
    print(i**2)

# cube of (1-10)
for i in range(1,11):
    print(i**3)

# i\p n and print 1 to n
n = int(input ("enter a number:"))
for i in range(1, n+1):
    print(i)

#(11-15)
    num = 1
    while num<21:
        print(num)
        num+=1

#Find factorial of a number using while
num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact = fact * i
    i += 1

print("Factorial =", fact)

#Reverse a number using while

num = int(input("Enter a number: "))

rev = 0

while num > 0:
    digit = num % 10        
    rev = rev * 10 + digit 
    num = num // 10        

print("Reversed number =", rev)

#Count digits in a number

num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits =", count)

while True:
    user_input = input("Enter something (type 'stop' to exit): ")
    
    if user_input.lower() == "stop":
        break
    
    print("You entered:", user_input)

#(16-20)

# nested loop
for i in range(1,5):
    for j in range(i):
        print("*", end="")
    print()

1
12
123
1234
for i in range(1,5):
    for j in range(1, i + 1):
        print(j, end="")
print()

# multiplication table 1 to 5
for i in range(1,6):
    for j in range(1,6):
        print(i, "x", j, "=", i*j)
        print()

for i in range(3):
    for j in range(3):
        print(chr(65+j), end=" ")
        print()

for i in range(1, 10):
    for j in range(1):
        print( i, end=" ")
        print()

#(21-25)
# string basics

text = "welcome python"
res = len(text)
print(res)

text = input("hello world")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count +=1
        print("number of vowels:", count)

s= "enter a string:"
count = 0
for ch in s:
    if ch.lower() in "aeiou":
        count += 1
        print("number of vowels:", count)

# reverse a String 

s=input("enter a string:")
reverse ="" 
for char in s:
    reverse = char + reverse
    print("reversed sstring:",reverse)

#(26-30)
# string slices
string="london university"
print(string[ :5])

print(string[-3])

print(string[:: -1])

print(string[:: 2])

print(string[1:-1])

#(31-35)
# List Basics
nums =[10,20,30,40,50]
print("sum =", sum(nums))

print("maximum=", max(nums))

print("minimum=",min(nums))

print("total elements=",len(nums))

x = int[60]
if x in nums:
    print("element exists")
else:
    print("element not found" )

#(36-40)
# List Operations

#append()
nums.append[70]
print(nums)

# Insert element at specific index
nums.insert[3,35]
print(nums)

# Remove element using remove()
nums.remove[50]
print(nums)

# Reverse list without using .reverse()
nums_reversed =nums[::-1]
print(nums_reversed)

#
num=[60,10,50,80,20]
for i in range(len(num)):
    for j in range(0, len(num)-i-1):
        if num[j]> nums[j+1]:
            num[j], num[j+1]=num[j+1], num[j]
            print(num)            