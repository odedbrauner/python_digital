from random import randint
a=int(input("enter your money"))
b=3*a
if (a%3!=0):
    print("you can have "+str(a%3) + " dollars back")
    a=a-(a%3)
prize=0
for x in range(a//3):
    print("round number "+str((x+1))+"\n----------------")
    cube1 = randint(1,6)
    cube2 = randint(1,6)
    print("cube1="+str(cube1)+"\ncube2="+str(cube2)+"\n----------------")
    if (cube1==cube2 and cube2==6):
        prize=prize+1000
    elif(cube1==cube2 and cube1!=6):
        prize+=100
    elif(cube1==1 and cube2!=cube1):
        prize+=20
    elif (cube2 == 2 and cube2 != cube1):
        prize += 40
print("your prize is "+str(prize)+"$")




