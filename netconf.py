from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString

device = {
    'host': '192.168.29.95',
    'port': '830',
    'username': 'admin',
    'password': 'cisco',
    'hostkey_verify': False
}

netconf = manager.connect(**device)

print("NETCONF Connection established with the device successfully")
netconf_filter = ''
c=netconf.get_config(source='running')
output = open(r"C:\Users\Administrator\Documents\Git\Python\cisco\netconf_output.xml", "a")
print(c.data_xml)
output.write(c.data_xml)
output.close()