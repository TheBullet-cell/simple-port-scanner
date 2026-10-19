import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

target = input("Enter target IP (e.g, 127.0.0.1): ")
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]

print(f"\nScanning {target}...\n")

for port in ports:
    if scan_port(target, port):
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
