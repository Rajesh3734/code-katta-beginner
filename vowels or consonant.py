a=input()
b=["a","e","i","o","u","A","E","I","O","U"]
if ((ord(a) in range(65,91))or(ord(a) in range(97,124))):
  if(a in b):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
  
