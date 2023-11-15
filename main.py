import socket
import threading
import argparse
import time

# Def all avilable ports
ALL_PORTS = [1, 65536]

def scan_port(ip, port):
    """
    Scan a specific port on the target IP address.

    Args:
        ip (str): Target IP address.
        port (int): Port to scan.

    Returns:
        None
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"Port {port} is open")
    except (socket.timeout, socket.error):
        # print("Timeout.")
        # Port is either timeout or close 
        pass
    except KeyboardInterrupt:
        print("Scan interrupted.")
    except socket.gaierror:
        print("Host couldn't be resolved.")
    except socket.error:
        print("Couldn't connect.")
    finally:
        sock.close()

def scan_range(ip, start_port, end_port):
    """
    Scan a range of ports on the target IP address.

    Args:
        ip (str): Target IP address.
        start_port (int): Starting port of the range.
        end_port (int): Ending port of the range.

    Returns:
        None
    """
    # Check the validity of the range
    if start_port >= ALL_PORTS[0] and start_port <= ALL_PORTS[1] and start_port < end_port and end_port <= ALL_PORTS[1]:
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(ip, port))
            thread.start()
    else:
        print("Invalid port range.")
        print(start_port, end_port)

def scan_all_ports(ip):
    """
    Scan all ports (1-65535) on the target IP address.

    Args:
        ip (str): Target IP address.

    Returns:
        None
    """     
    for port in range(ALL_PORTS[0], ALL_PORTS[1]):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

def main():
    """
    Main function to parse command line arguments and initiate port scanning.

    Returns:
        None
    """
    
    # Priniting banner
    parser = argparse.ArgumentParser(description="Port Ripper - Lightweight fast port scanner.")
    parser.add_argument("target", help="Target IP address or host name")
    parser.add_argument("-p", "--port", type=int, default=0, help="Scan a specific port")
    parser.add_argument("-r", "--range", nargs=2, type=int, metavar=("start", "end"),
                        default=[1, 1024], help="Scan a range of ports (default: 0-1024)")
    parser.add_argument("-a", "--all", action="store_true", help="Scan all ports (1-65535)")

    args = parser.parse_args()

    target = args.target
    ip = socket.gethostbyname(target) if not target == "localhost" else "127.0.0.1"

    start_time = time.time()

    # Banner
    print("=" * 80)
    print(f"Scanning {target} ({ip}) - Start Time: {time.ctime(start_time)}")
    print("=" * 80)

    if args.port:
        scan_port(ip, args.port)
    elif args.range:
        start_port, end_port = args.range
        scan_range(ip, start_port, end_port)
    elif args.all:
        scan_all_ports(ip)
    else:
        print("Please specify a port, a range of ports, or use the --all flag to scan all ports.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Scan finished - Elapsed Time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
