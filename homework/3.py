
server_ip = ("192", "168", "1", "10")  
allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed_ips(new_ip):
    if new_ip not in allowed_ips:
        allowed_ips.append(new_ip)
        print(f"Added {new_ip} to allowed IPs.")
    else:
        print(f"{new_ip} is already in allowed IPs.")

def display_config():
    print("\n--- Web Server Configuration ---")
    print("Server IP (unchangeable):", ".".join(server_ip))
    print("Allowed IPs:", allowed_ips)

while True:
    print("\n1. Add Allowed IP")
    print("2. Display Configuration")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == '1':
        ip = input("Enter new allowed IP: ")
        update_allowed_ips(ip)
    elif choice == '2':
        display_config()
    elif choice == '3':
        print("Exiting configuration system...")
        break
    else:
        print("Invalid choice! Please try again.")
