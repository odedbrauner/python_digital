my_credentials=["odedbrauner",16,"oded@gmail.com","0549222555"]
print("name={}\nage={}\nmail={}\nphone={}".format(my_credentials[0],str(my_credentials[1]),my_credentials[2],my_credentials[3]))
IPs=["192.25.46.1","172.16.16.1"]
print(IPs)
IPs.append("192.2.2.1")
IPs.append("172.16.3.1")
IPs.append("182.2.3.1")
print(IPs)
IPs.pop(3)
print(IPs)
print("the ips list length is"+str(len(IPs)))