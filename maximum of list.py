N=int(input())
if((N>1)and(N<=10000)):
  l=[int(x)for x in input().split(" ",N-1)]
print(min(l))
