from netmiko import ConnectHandler
from getpass import getpass

router_details = {
    "ip":"192.168.29.115",
    "username":"",
    "password":"",
    "device_type":"cisco_ios"
}

router_details["username"] = input("Enter username: ")
router_details["password"] = getpass("Enter password: ")

ch = None

ch = ConnectHandler(**router_details)

if ch:
    print("Connection successful...!")

no_of_ints = int(input("Enter the number of interfaces to be configured: "))

for i in range(0,no_of_ints):
    int_name = input("Enter the Interface name: ")
    int_ip_add = input("Enter the IP Address: ")
    int_mask = input("Enter the Subnet mask: ")
    int_desc = input("Enter the Description: ")

    commands = [f"interface {int_name}", f"ip add {int_ip_add} {int_mask}", f"desc {int_desc}", "no shut"]

    int_config = ch.send_config_set(commands)
    print(int_config)

    int_details = ch.send_command("sh ip int br")
    print(int_details)

ch.save_config()
ch.disconnect()