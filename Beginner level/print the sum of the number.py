N=int(raw_input())
s=0
while N>0:
    rem=N%10
    s=s+rem
    N=N/10
print s
