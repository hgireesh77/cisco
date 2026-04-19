from netmiko import ConnectHandler
from getpass import getpass

routers = open(r"C:\Users\Administrator\Documents\Git\Python\cisco\routers.txt", 'r')

for router in routers:
    print(f"\n\n\nCredentials for {router}\n")
    router_details = {
        "ip":router,
        "username":input(f"Enter the username: "),
        "password":getpass(f"Enter the password: "),
        "device_type":"cisco_ios"
    }

    print(f"Initiating connection to the device: {router}")
    ssh_conn = ConnectHandler(**router_details)
    print(f"Connected to the device {router}")

    commands = open(r"C:\Users\Administrator\Documents\Git\Python\cisco\commands.txt", 'r')
    output = open(r"C:\Users\Administrator\Documents\Git\Python\cisco\output.txt", "a")

    for command in commands:
        print(f"Executing the command: {command.strip()}")
        c_write = ssh_conn.send_command(command)
        output.write(f"----------------{router.strip()}----------------\n")
        output.write(f"Command: {command.strip()} \n")
        output.write(f"{c_write} \n")

    output.write(f"***********************************************************************************************************\n\n")

    commands.close()
    output.close()
    ssh_conn.disconnect()

routers.close()


