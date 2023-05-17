# while loop:


count=0
while count < 5:
    print(count)
    count +=1


count=0

while count <10:
    count+=1
    if count %2==0:
        continue
    elif count==9:
        break
    print(count)
    
a=1

while a<=5:
   a+=1
   print(a)
   a+=1

count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("Loop ended.")


a=1
b=5
while True:
   while b>0:
       print("*"*a)
       a+=1
       b-=1

#user validation with number or string

while True:
    user_input = input("Enter an integer or string: ")

    # Check if the input is an integer
    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            break  # Valid integer input, exit the loop
        else:
            print("Invalid input. Please enter a positive integer.")
    elif isinstance(user_input, str):
        break  # Valid string input, exit the loop
    else:
        print("Invalid input. Please enter a valid integer or string.")

# Process the valid input
if isinstance(user_input, int):
    print("You entered an integer:", user_input)
else:
    print("You entered a string:", user_input)

# login validation:

register_user= {'user1':'password1','user2':'password2','user3':'password2','user4':'password4'}

while True:
    username=input('Enter the name:')
    userpassword=input('Enter the password:')
    
    if username in register_user and password ==register_user [username]:
        print('login successfully!')
        break
    else:
        print("invaild information! please check password or username and try again")
        
print("welcome,",username)
    