a=str(input("enter the string:"))
b=str(input("enter k:"))
c=len(a)
count=0
for i in range(c):
  if(a[i]==b):
    count=count+1
print (count)
