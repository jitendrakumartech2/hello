# for multiple devices
# one thing is missing here while connecting to routers, that programme should tell us about which host is tying to login ,asking for password, 
from netmiko import ConnectHandler
from getpass import getpass
password = getpass()
                                                                     
arista1 = {
	'device_type': 'arista_eos', 
	'host': '10.10.10.1', 
	'username': 'admin', 
	'password': password
}

cisco1 = {
	'device_type': 'cisco_ios',
	'host': '10.10.10.2',
	'username': 'admin',
	'password': password
}
		
all_devices = [arista1, cisco1]

with open('D:\pycharm\showconf.txt') as f:
	lines = f.read().splitlines()
print(lines)

for router in all_devices:
	net_connect = ConnectHandler(**router)
	net_connect.enable()
	output = net_connect.send_config_set(lines)
	print(output)
