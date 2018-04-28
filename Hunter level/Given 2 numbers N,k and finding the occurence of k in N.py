N=int(input())
k=int(input())
count=0
while(N!=0):
  rem=N%10
  if (rem==k):
     count=count+1 
  N=N%10
print(count)
