print("Table Exception handling ")
x = input("Enter the value of x Table = ")
# print(x)
try:
    for i in range(1,11):
        print(f"{int(x)} X {i} = {int(x)*(i)}")
except Exception as e:
    print(e)

print("Some imp code")
print("End of the Programm.")
    