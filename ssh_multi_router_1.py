from netmiko import ConnectHandler
from getpass import getpass

R1 = "192.168.29.111"
R2 = "192.168.29.112"
R3 = "192.168.29.113"

routers = [R1, R2, R3]

for router in routers:
    router_details = {
        "ip": router,
        "username": input("Enter the username: "),
        "password": getpass("Enter the password"),
        "device_type": "cisco_ios"
    }

    ssh_con = ConnectHandler(**router_details)
    print("Connection created successfully")

    interfaces = int(input("Enter the number of interfaces to be configured: "))

    for i in range(interfaces):
        int_name = input("Enter the interface name: ")
        ip_addr = input("Enter the IP Address: ")
        subnet_mask =  input("Enter the subnet mask: ")
        desc = input("Enter the Description: ")

        ssh_con.send_config_set([f"int {int_name}", f"ip add {ip_addr} {subnet_mask}", f"no shut", f"desc {desc}"])

    int_config = ssh_con.send_command("sh ip int br")
    print(int_config)

    ssh_con.save_config()
    ssh_con.disconnect()
