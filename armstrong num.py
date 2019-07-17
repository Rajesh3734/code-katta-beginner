a=int(input())
num=a
rem=0
arm=0
if((a<=10000)and(a>=0)):
  while(num!=0):
    rem=num%10
    arm=(rem*rem*rem)+arm
    num=num//10
  if(arm==a):
    print("yes")
  else:
    print("no")
   
