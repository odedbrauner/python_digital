from time import sleep
##for loops
# list_oded=["banana","apple","mango"]
# for x in range(len(list_oded)):
#     print(list_oded[x])
print("Now we will get all the details about your class: \n")
for i in range(4):
    name=input("enter a name: ")
    age=int(input("enter an age:"))
    phone=input("enter a phone")
    print("printing student number "+ str(i)+" detailes...")
    sleep(3)
    print("full name "+ name+ "\nage: "+str(age)+"\nphone: "+ phone)

