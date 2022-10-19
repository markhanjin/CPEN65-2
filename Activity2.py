#Creat a python program that use array
#Insert each character of your full name and displays each character of your full name in reverse order.
name = str(input("Enter your full name: "))
print(name)
reversedname = reversed(name)
print(''.join(reversedname))