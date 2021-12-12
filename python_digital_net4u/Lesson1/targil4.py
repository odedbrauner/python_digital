'''a way to do a list
new_list=[]
another way
new_list2=list()
'''
my_list2=list("1234567")
my_string=''.join(my_list2)
print(my_string)
my_list=["hello",1,66.6,"oded"]
#prints the length of the list
print(len(my_list))
#append adds characters to the list
my_list.append("brauner")
print(my_list)
print(len(my_list))
#inserts a character in a specifc place
my_list.insert(3,2)
print(my_list)
#removing a character in a specified place
my_list.pop()
print(my_list)
