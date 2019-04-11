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
for router in all_devices:
	net_connect = ConnectHandler(**router)
	net_connect.enable()
	output = net_connect.send_command('show ip int brief')
	print(output)
	
	config_commands = ['int loop3', 'ip add 3.3.3.3 255.255.255.255', 'shutdown']
	output = net_connect.send_config_set(config_commands)
	print(output)
	
	for n in range (100,110):
		print('creating vlan '+ str(n))
		config_commands = ['vlan '+ str(n), 'name python_vlan_' + str(n)]
		output = net_connect.send_config_set(config_commands)
		print (output)
		
	output = net_connect.send_command('show vlan')
	print(output)
	
	for n in range (100,110):
		print('deleting vlans ' + str(n))
		config_commands = ['no vlan '+str(n)]
		output = net_connect.send_config_set(config_commands)
		print(output)
	
	output = net_connect.send_command('show vlan')
	print(output)
	
	


# that need to be added , ref taken from here https://github.com/ktbyers/netmiko/issues/797
