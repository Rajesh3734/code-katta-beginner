(n,a,d)=map(int,input().split())
sum=0
l=[]
sumation_of_n=0
if((n>=1)and(d<=100000)):
    for i in range(1,n+1):
        if (i==1):
            sum=a
            l.append(sum)
        else:
            sum=sum+d
            l.append(sum)
print(l)
for j in l:
    sumation_of_n=sumation_of_n+j
print(sumation_of_n)

