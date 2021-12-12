from time import sleep
print("menu: \n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 entries to DNS_Dictionary and print it\n4.Check if a string is polindrom")
num=int(input("choose one of the above 1-4"))
if(num==1):
    print("Insert Number and ** it by 3")
    print((int(input("enter a number of choice"))**3))
elif(num==2):
    print("Insert 4 IPs to a list and print it")
    print(input("insert 4 IPs"))
elif(num==3):
    print("Insert 4 entries to DNS_Dictionary and print it")
    DNS_dict={input("enter a dns key"):input("enter a dns variable"),input("enter a dns key"):input("enter a dns variable"),input("enter a dns key"):input("enter a dns variable"),input("enter a dns key"):input("enter a dns variable")}
    print("the dns dictionary is= "+DNS_dict)
elif(num==4):
    print("Check if a string is polindrom")
    a=input("enter a word")
    if(a==a[::-1]):
        print("is polindrom")
    else:
        print("its not a polindrom")
else:
    print("you need to insert a number between 1-4")

