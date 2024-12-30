
# SET 1
# P1
c = float(input("Enter the value of celsius(c) = "))
f = 9/5*c+32
print("\nIn fahrenheit F = ",f)
x = float(input("\nEnter the value of fahrenheit(x) = "))
y = 5/9*(x-32)
print("\nIn calsius C = ",y)

# P2
l=float(input("\nenter a = "))
b=float(input("\nenter b = "))

a=l*b
print("\nArea of Rectangle = ",a)

P=2*(l*b)
print("\nParameter of rectangle = ",P)

# P3
p=str(input("\nEnter the password = "))
print("\nthe password length is ",len(p))

# P4
a = int(input("\nenter a = "))
b = int(input("\nenter b = "))
c = int(input("\nenter c = "))

avg = (a+b+c)/3
print("\nAverage = ",avg)

# P5
year = int(input("\nEnter any Year = "))
if(year%4 == 0 and year%100 != 0 or year%400 == 0):
  print("\nYear",year ,"is leap Year")
  
else:
  print("\nYear",year, "is not a leap year")
  
# P6
n = int(input("Enter n = "))
fact = 1
if(n<0):
  print("\nFactorial is not possible for negative number")
elif(n == 0):
  print("\nFactorial of 0 is 1")
else:  
  for i in range(1, n+1):
    fact = fact* i
  print("\nFactorial = ",fact)
  
# P7  
s = str(input("\nEnter String"))
if(s[::-1] == s):
  print("\nString is palindrome.")
else:
  print("\nStrint is not a palindrome.")
  
# using inbuild function  
st = str(input("\nEnter string"))
st = st.casefold()
rev = st[::-1]
if(st == rev):
  print("\nString is palindrome")

# stack  
list = [1,2,3,4,5]  
list.append(6) # push
print(list[0:4])
list.pop(4)
print(list)
  
# Creating a tuple with multiple elements
tuple1 = (1, 2, 3, 4)
tuple2 = 1, 2, 3, 4  # Without parentheses

# Creating a single-element tuple
single_element_tuple = (10,)  # Comma is important
# Accessing elements
print(tuple1[0])  # Output: 1
print(tuple1[-1])  # Output: 4  
  
