a=[]
N=int(input())
k=int(input())
for i in range (N):
  n=int(input())
  b=a.append(n)
for i in range(N):
  if(a[i]==k):
    print ("yes")
    break
  else:
    print ("no")
    break
