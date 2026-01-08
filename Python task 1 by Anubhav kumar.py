#Python task 1 by Anubhav kumar
#task 1 - Perform Basic Mathematical Operations

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

print("addition : " , n1+n2)
print("subtraction : " , n1-n2)
print("multiplication : " , n1*n2)

if n2 == 0:
    print("Not defined")
else:
    print("division : " , n1/n2)