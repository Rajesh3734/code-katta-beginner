import random
a=int(input())
#l=list(map(int,(input().split())))
#print(l)
#x = [int(x), input("Enter multiple value: ").split()for x in range(a)] 
l=[input().split()[:random.randint(0,10)] for x in range(a)]
#lowerlist = ['abcdefghijklmnopqrstuvwxyz'[:random.randint(0,25)] for x in range(1000)]
#upperlist = [str.upper(x) for x in lowerlist]
print(l)
