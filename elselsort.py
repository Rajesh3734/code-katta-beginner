n=int(input())
l=[int(input().split(" ",n-1))]
def sort(l,min_num,max_num):
  for i in range(0,len(l)):
    if(l[i]==min_num):
      continue
    elif(l[i]<min_num):
      (l[i],min_num)=(min_num,l[i])
    elif()
