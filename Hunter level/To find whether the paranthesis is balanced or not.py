s=str(input())
count1=0
count2=0
l=len(s)
for i in range(l):
  if(s[i]=='('):
    count1=count1+1
  elif(s[i]==')'):
    count2=count2+1 
if(count1==count2): 
  print("yes")
else:
  print("no")
