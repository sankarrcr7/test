# using pass statement :

#function
def my_function():
    pass
my_function()  # nothing happend to prevent syntax error

# class
class my_class():
    pass

myobject=my_class()

#for loop

for i in range(10):
    if i!=2:
        print("nothing")
    elif i==2:
        print("happend")
    else:
        print(i)
        
#while loop

i=0
while i<10:
    if i!=2:
        print("nothing")
    elif i==2:
        print("happend")
    else:
        print(i)
    i+=1 
      
# Error handling:
try:
    x = int("abc")
except ValueError:
    pass 