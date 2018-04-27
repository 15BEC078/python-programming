a=[]
N=int(input('enter the number of numbers in an array:'))
k=int(input())
for i in range(N):
  n=int(input('enter the number:'))
  a.append(n)
b=sorted(a)
print (b)
print (b[k-1])
