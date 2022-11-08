n = int(input("enter number:"))
data = 0
while(n>0):
    dig = n%10
    data = data*10 + dig
    n = n//10
print(data)
