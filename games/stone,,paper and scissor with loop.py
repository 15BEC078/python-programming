print("ready to play")
count1=0
count2=0
a=str(input('yes or no'))
if (a=='yes'):
  print ("continue")
else:
  print("exit")
  exit()
player1=str(input("enter your name:"))
player2=str(input("enter your name:"))
print("player1 name is:"+player1)
print("player2 name is:"+player2)
l=['stone','paper','scissor']
s=0 
while (s<3):
       s=s+1
       n=str(input("dear"+'_'+ player1+"please select stone,paper or scissor"))
       m=str(input("dear"+'_'+ player2+"please select stone,paper or scissor"))
       if(n==l[0]and m==l[0] or n==l[1] and m==l[1] or n==l[2] and m==l[2]):
          print("game draw")
          
       if(n==l[0] and m==l[2] or n==l[1]and m==l[0] or n==l[2] and m==l[1]):
          print(player1+'_' +"is winner")
          count1=count1+1
          
       else:
          print(player2+'_' +"is winner")
          count2=count2+1

if(count1>count2):
      print(" The overall winner is"+'_'+player1)
else:
      print(" The overall winner is"+'_'+player2)
