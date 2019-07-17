(n,a,d)=map(int,input().split())
sum=0
for i in range(1,n+1):
  if (i==1):
    sum=a
  sum=sum+d
print(sum)

