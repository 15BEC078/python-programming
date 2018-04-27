a=str(input())
b=str(input())
l1=len(a)
l2=len(b)
if(l1==l2):
  for i in range (l1):
    if a[i]==b[i]:
       flag=1
    else:
       flag=0
  if (flag==1):
         print ("yes")
  else:
         print ("no")
else:
  print ("no")
