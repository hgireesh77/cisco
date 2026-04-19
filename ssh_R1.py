from netmiko import ConnectHandler

router_details = {
    "ip":"192.168.29.94",
    "username":"admin1",
    "password":"cisco123",
    "device_type":"cisco_ios"
}
router_details["username"] = input("Enter username: ")
router_details["password"] = input("Enter password: ")

ch = ConnectHandler(**router_details)
print("Successfully created the SSH connection: ")
print(type(ch))

ip_address = input("Enter the IP Address")
subnet = input("Enter the Subnet")
interface = input("Enter the Interface")
description = input("Enter the Description")


#commands = ["no int loop 100","int loop 100", "ip add 10.10.10.1 255.255.255.0", "desc Created using Python Automation"]
commands = ["interface {}".format(interface), f"ip address {ip_address} {subnet}", "description " + description, "no shut"]
ospf_commands = ["router ospf 101", "network 0.0.0.0 0.0.0.0 area 0"]

int_configs = ch.send_config_set(commands)

print(int_configs)

int_details = ch.send_command("show ip int br")
print(int_details)

int_details = ch.send_command("show run int loop100")
print(int_details)

ospf_configs = ch.send_config_set(ospf_commands)
print(ospf_configs)

ospf_details = ch.send_command("show ip ospf int br")
print(ospf_details)

ch.save_config()
ch.disconnect()