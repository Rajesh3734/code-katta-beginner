(a,b)=map(int,input().split())
l=[]
rem=0
arm=0
if((b<=10000)and(a>=0)):
  for i in range(a+1,b):
    num=i
    while(num!=0):
      rem=num%10
      arm=(rem*rem*rem)+arm
      num=num//10
    if(arm==i):
      l.append(arm)
  for j in range(0,len(l)):
    print(l[j],end=" ")
   
