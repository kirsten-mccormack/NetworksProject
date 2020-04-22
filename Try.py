filePath = "testFile1.txt"
file = open(filePath,'w')
upload = file.write('PLEASE FREAKING WORK')
print(upload)



# GetAddrPort = "198 23,34,54,44,67\r\n"

# IndexFound = -1

# IndexFound = GetAddrPort.find("\r\n")
# Hello = GetAddrPort[0:IndexFound]
# print(Hello)
# for x in range(4):
#     IndexFound = GetAddrPort.find(",",IndexFound+1)

# Client_DataAddr = GetAddrPort[0:IndexFound].replace(",",".")
# print(Client_DataAddr)
# GetAddrPort = GetAddrPort[IndexFound+1:]
# Ports = GetAddrPort.split(",")

# P1 = int(Ports[0])
# P2 = int(Ports[1])
# Client_DataPort = P1*256+P2

# print(Client_DataPort)