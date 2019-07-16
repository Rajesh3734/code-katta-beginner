a=int(input())
num=a
rem=0
rev=0
if((a<=1000)and(a>=0)):
  while(num!=0):
    rem=num%10
    rev=rem+(rev*10)
    num=num//10
  if(rev==a):
    print("yes")
  else:
    print("no")
    
