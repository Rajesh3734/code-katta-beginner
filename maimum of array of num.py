import random
a=int(input())
#l=list(map(int,(input().split())))
#print(l)
#x = [int(x), input("Enter multiple value: ").split()for x in range(a)] 
l=[input().split()[:random.randint(0,10)] for x in range(a)]
#lowerlist = ['abcdefghijklmnopqrstuvwxyz'[:random.randint(0,25)] for x in range(1000)]
#upperlist = [str.upper(x) for x in lowerlist]
print(l)
a=int(input())
l=[input().split()for i in range(a)]
print(l)
print(max(l))
int(input())
l=list(map(int,(input().split( )for i in range(a))))

print(max(l))

# Python program showing how to 
# multiple input using split 
  
# taking two inputs at a time 
x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print() 
  
# taking three inputs at a time 
x, y, z = input("Enter a three value: ").split() 
print("Total number of students: ", x) 
print("Number of boys is : ", y) 
print("Number of girls is : ", z) 
print() 
  
# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 
  
# taking multiple inputs at a time  
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split())) 

# Python program showing 
# how to take multiple input 
# using List comprehension 
  
# taking two input at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print() 
  
# taking three input at a time 
x, y, z = [int(x) for x in input("Enter three value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print("Third Number is: ", z) 
print() 
  
# taking two inputs at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First number is {} and second number is {}".format(x, y)) 
print() 
  
# taking multiple inputs at a time  
x = [int(x) for x in input("Enter multiple value: ").split()] 
print("Number of list is: ", x)  

https://www.datacamp.com/community/tutorials/python-list-comprehension
  https://www.google.com/search?rlz=1C1GCEU_enIN858IN858&ei=1HYwXfS7HcqCvQT70JmYCA&q=how+to+get+multiple+inputs+of+integer+type+to+a+list+in+a+same+line+using+list+comphrenhension+and+with+a+specific+range&oq=how+to+get+multiple+inputs+of+integer+type+to+a+list+in+a+same+line+using+list+comphrenhension+and+with+a+specific+range&gs_l=psy-ab.3..0i71l8.4770.8351..11583...0.0..0.0.0.......3....1..gws-wiz.R0mOJEif8P4&ved=0ahUKEwj09c6JzL7jAhVKQY8KHXtoBoMQ4dUDCAo&uact=5
    https://www.google.com/search?rlz=1C1GCEU_enIN858IN858&ei=ynYwXY7qFIiBvQT8laOgBw&q=how+to+getmultiple+inputs+of+integer+type+to+a+list+in+a+same+line+using+list+comphrenhension+and+with+a+specific+range&oq=how+to+getmultiple+inputs+of+integer+type+to+a+list+in+a+same+line+using+list+comphrenhension+and+with+a+specific+range&gs_l=psy-ab.3..0i71l8.5672.8435..8921...0.0..0.0.0.......5....1..gws-wiz.5GxGq-CS5xY&ved=0ahUKEwiO9-OEzL7jAhWIQI8KHfzKCHQQ4dUDCAo&uact=5
      https://www.google.com/search?rlz=1C1GCEU_enIN858IN858&ei=T3QwXa3SKMuA9QOOsoqYCA&q=how+to+feet+multiple+inputs+of+integer+type+to+a+list+in+a+same+line+using+list+comphrenhension+and+with+a+specific+range&oq=how+to+feet+multiple+inputs+of+integer+type+to+a+list+in+a+same+line+using+list+comphrenhension+and+with+a+specific+range&gs_l=psy-ab.3..0i71l8.16020.31133..41425...0.0..0.0.0.......25....1..gws-wiz.9SF2hFl7gfg&ved=0ahUKEwjttZLWyb7jAhVLQH0KHQ6ZAoMQ4dUDCAo&uact=5
        https://www.google.com/search?q=how+to+feet+multiple+inputs+to+a+list+in+a+same+line+using+list+comphrenhension+and+with+a+specific+range&rlz=1C1GCEU_enIN858IN858&oq=how+to+feet+multiple+inputs+to+a+list+in+a+same+line+using+list+comphrenhension+and+with+a+specific+range&aqs=chrome..69i57.83209j0j8&sourceid=chrome&ie=UTF-8
N=int(input('How many cases will you calculate?\n'))
print('Input parameters separated by spaces:')
entr = [list(int(x) for x in input().split(" ",N)) for i in range(N)]
print(entr)
