
new_list = [expression for item in iterable if condition]

new_list = [item!=2 for item in range (1,11) if item %2==0]
print(new_list)

sec_list=[x for x in range (1,23) if x%2==0 ]
print(sec_list)


words = ["apple","orange","cherry","banana"]
w=[word.upper()for word in words]
r=[word.lower()for word in words]
print(w)
print(r)

# nested_list

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newlist=[item for i in nested for item in i]
print(newlist)

# Creating a list of tuples from two separate lists:

names = ["sankar", "ashik", "sathish"]
age= [23,34,44]
ziip= [(names,age)for names, age in zip(names,age)]
print(ziip)


words = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
long_words = [word for word in words if len(word) >=6]
print(long_words)
