print("Are you ready to play?") 
a=str(input())
if(a=='yes'):
  print("continue")
else:
  exit()
s=0
print("Hi buddy, what is your name?")
myname=str(input())
print('hi'+ '_' +myname)
guessnumber=3
print("Take a guess and my number is between is 1 and 20") 
print(myname+'_'+"you have a three chances.ALL the best??")
while(s<3):
  s=s+1
  print("enter any number?")
  n=int(input())
  if(guessnumber<n):
    print("your guess is high")
  if(guessnumber>n):
    print("your guess is low ")
  if(guessnumber==n):
    break
    
if (guessnumber==n):
    s=str(s)
    print("welldone"+myname+"you guessed my number in"+s+"guesses")
if(guessnumber!=n):
    print("oops!Better luck next time")
