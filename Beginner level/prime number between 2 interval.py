N=int(raw_input())
M=int(raw_input())
for j in range (N,M+1):
    if j>1:
     for i in range (2,j):
        if (j%i==0):
            break
        else:
           print j
           break
