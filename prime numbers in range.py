(a,b)=map(int,input().split())
l=[]
for i in range(a+1,b):
  for j in range(2,b//2):
    if((i%j==0)):
      break
  else:
      l.append(i)
for k in l:
  print(k,end=" ")
  
