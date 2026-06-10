from netmiko import ConnectHandler
from getpass import getpass

routers = open(r"C:\Users\Administrator\Documents\Git\Python\cisco\routers.txt", 'r')

static_routes = ['ip route 10.10.10.0 255.255.255.0 192.168.29.1', 'ip route 10.10.20.0 255.255.255.0 192.168.29.1', 'ip route 10.10.30.0 255.255.255.0 192.168.29.1']

for router in routers:
    print(f"\n------Credentials for {router.strip()}------")
    router_details = {
        "ip":router,
        "username":input("Enter the username: "),
        "password":getpass("Enter the password: "),
        "device_type":"cisco_ios"
    }

    print(f"\n------Initiating connection to {router.strip()}\n")
    ssh_conn = ConnectHandler(**router_details)
    print(f"------Connected to {router.strip()}\n")

    for static_route in static_routes:
        ssh_conn.send_config_set(static_route)
    
    print(ssh_conn.send_command("sh ip route"))

    ssh_conn.save_config()
    ssh_conn.disconnect()

routers.close()