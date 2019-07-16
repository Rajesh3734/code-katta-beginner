(basea,p)=map(int,input().split())
output=1
#output=pow(basea,p)
if(p==0):
  output=1
else:
  for i in range(p):
    output=output*basea

print(output)
