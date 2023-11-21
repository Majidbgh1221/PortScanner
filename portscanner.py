import socket
from termcolor import colored

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print(colored(f'[+] Port {port} opened on {ip}', 'green'))
    except socket.error:
        pass
    finally:
        sock.close()

def scan(targets, ports):
    print(colored(f'Scanning for {targets}', 'red'))
    for port in range(1, ports + 1):  
        scan_port(targets, port)

if __name__ == "__main__":
    targets = input('[*] Enter Targets to Scan (seperate them with ,):\n ')
    ports = int(input('[*] Enter How Many Ports You Want To Scan:\n '))

    if ',' in targets:
        print(colored('[*] Scanning multiple targets', 'green'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(), ports)
    else:
        scan(targets, ports)
