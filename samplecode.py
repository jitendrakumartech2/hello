from netmiko import ConnectHandler

sw_11 = {
'device_type': 'avaya_vsp',
'ip': '1.2.3.4',
'username': 'uname',
'password': 'pass'
}

with open('config') as f:
lines = f.read().splitlines()
print lines

all_devices = [sw_11]

for devices in all_devices:
net_connect = ConnectHandler(**devices)
net_connect.enable()
output = net_connect.send_config_set(lines)
print output

config.close()
