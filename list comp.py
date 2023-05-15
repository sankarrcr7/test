
# new_list = [expression for item in iterable if condition]

new_list = [item!=2 for item in range (1,11) if item %2==0]
print(new_list)

sec_list=[x for x in range (1,23) if x%2==0 ]
print(sec_list)
