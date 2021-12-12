#1
#print("net4u is the best place\n     ...in the world?")
#2
# from datetime import datetime
# print(datetime.now())
#3
# a=input("enter your name")
# print(a)
# print(' '.join(a[::-1]))
#4
# import pathlib
# print("File Extension: "+pathlib.Path(input("enter your file with extention")).suffix)
#5
# n=int(input("enter your number"))
# print(n+n*11+n*111)
#6
# num=int(input("enter your number"))
# if(num%2==0):
#     print("its an even number")
# else:
#     print("its not an even number")
####7
#print(input("your he"))
#8
#n=int(input("enter your number"))
#print(type(n)())
#9
# dict={"0":1,"2":3}
# print(dict)
# dict.update({"4":5})
# print(dict)
#10
# a=input("enter your word")
# dict={}
# for x in a:
#     dict[x]=dict.get(x,0)+1
# print(dict)
#11
# a=input("enter a word")
# b=input("enter a word")
# print(a,b)
# print(a.replace(a[0:2],b[0:2]),b.replace(b[0:2],a[0:2]))
#12
# import collections
# str1 = 'thequickbrownfoxjumpsoverthelazydog'
# d = collections.defaultdict(int)
# for c in str1:
#     d[c] += 1
#
# for c in sorted(d, key=d.get, reverse=True):
#   if d[c] > 1:
#       print('%s %d' % (c, d[c]))
#13
# from random import randint
# new_list=[]
# for x in range(int(input("enter a number"))):
#     new_list.append(randint(0,100))
# print("list= " + str(new_list))
# sum=0
# for x in new_list:
#     sum += x
# print("sum of list variables ", str(sum))
#14
# list=["red","green","white","black","pink","yellow"]
# print(list)
# list.remove(5)
# list.remove(4)
# list.remove(0)
# print(list)