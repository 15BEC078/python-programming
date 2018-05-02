N=int(input())
sum=0
while(N!=0):
  rem=N%10
  if(rem%2!=0):
    sum=sum+rem
  N=N/10
if(sum%2==0):
  print("E")
else:
  print("O")
  
