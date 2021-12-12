my_dict={"oded":3000,"oz":4000,"yonatan":3500,"avi":2000,"adi":1000000}
print(my_dict)
print("the sum of the first and last names money is "+str(my_dict["adi"]+my_dict["oded"]))
my_dict.update({"dumbass":str(my_dict["adi"]+my_dict["oded"])})
print(my_dict)
#or you can do this instead of the 2 last rows
'''my_dict["dumbass"]=str(my_dict["adi"]+my_dict["oded"])
print(my_dict)'''
print("num of entries= "+str(len(my_dict)))
print("idan" in my_dict)