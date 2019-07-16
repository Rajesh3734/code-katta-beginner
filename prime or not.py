a=int(input())

if((a<=10000)and(a>1)):
  for i in range(2,(a//2)+1):
    if((a%i==0)):
      print("no")
      break
      
  else:
    print("yes")
  
