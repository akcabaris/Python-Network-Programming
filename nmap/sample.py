import nmap

scanner = nmap.PortScanner()

ip = "10.10.10.21"
scanner.scan(ip,'0-100','-sV')
#print(scanner.scaninfo())
#print(scanner[ip])

#up or down
print(ip +":",scanner[ip].state())
#print(scanner[ip].state())

#type of scan (like tcp, udp)
print(scanner[ip].all_protocols())

# which ports are open?
#print("Open Ports :",scanner[ip]['tcp'].keys())

#print(scanner[ip]['tcp'][21])

#for port in scanner[ip]['tcp'].keys():
	#print(port)
	#print(scanner[ip]['tcp'][port])
	#print("_________________________________")


for port in scanner[ip]['tcp'].keys():
	name = scanner[ip]['tcp'][port]['name']
	state =scanner[ip]['tcp'][port]['state']
	product = scanner[ip]['tcp'][port]['product']
	version = scanner[ip]['tcp'][port]['version']
	print(port, name, state, product, version)
