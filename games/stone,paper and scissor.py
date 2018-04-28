print("ready to play")
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
list=['stone','paper','scissor']
n=str(input("dear player1,please select stone,paper or scissor"))
m=str(input("dear player2,please select stone,paper or scissor"))
if(n==list[0]and m==list[0] or n==list[1] and m==list[1] or n==list[2] and m==list[2]):
  print("game draw")
elif((n==list[0] and m==list[2]) or (n==list[1]and m==list[0]) or (n==list[2] and m==list[1]) ):
  print("bhavadharini is winner")
else:
  print("harini is winner")
