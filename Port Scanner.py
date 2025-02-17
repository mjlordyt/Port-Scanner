import socket
import threading

# Function to scan a single port
def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

# Function to scan multiple ports
def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target} from port {start_port} to {end_port}\n")
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    scan_type = input("Enter scan type (fast/full): ").lower()
    
    if scan_type == "fast":
        start_port, end_port = 1, 1024  # Common ports
    elif scan_type == "full":
        start_port, end_port = 1, 65535  # All ports
    else:
        print("Invalid scan type! Choose 'fast' or 'full'.")
        exit()
    
    scan_ports(target, start_port, end_port)
