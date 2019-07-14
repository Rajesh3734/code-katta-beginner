n1=[]
sumation=0
(n,k)=map(int,input().split())
if((k<=n)and(k>=1)):
    for i in range(0,n):
        n1.append(i+1)       
for j in range(0,k):
    sumation=sumation+n1[j]
print(sumation)
