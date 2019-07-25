a=int(input)
l=[int(x) for x input().split(" ",a-1)]
for i in range(0,len(l))
a=int(input())
l=[int(x) for x  in input().split(" ",a-1)]
min_value=0
for i in range(0,len(l)):
  min_value=i
  print(i)
  for j in range(1,len(l)):
    if(l[min_value]>l[j]):
      min_value=j
  (l[i],l[min_value])=(l[min_value],l[i])
    
print(l)

