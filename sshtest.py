from netmiko import ConnectHandler                                                                                                         

arista1 = { 'device_type': 'arista_eos', 
			'host': '10.10.10.2',
			'username': 'admin',
			'password': 'python'
			}
			
arista2 = { 'device_type': 'arista_eos', 
			'host': '10.10.10.2',
			'username': 'admin',
			'password': 'python'
			}
			
device-list = [arista1,	arista2]

for switch in device-list:
	net_connect = ConnectHandler(**switch)
	for n in range(2,10):
		print("creating vlan_"+ str(n))
		config_commands("vlan "+ str(n), "name python_vlan_" + str(n))
		output = net_connect.send_config_set(config_commands)
		print(output)
