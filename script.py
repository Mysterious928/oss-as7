import argparse
import concurrent.futures
import socket
import subprocess

def port_scan(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((target,port))
        if result == 0:
            print("Port {} is open.".format(port))
            return port


def service_enum(target, port):
    try:
        print("Enumerating port {}:".format(port))

        result = subprocess.check_output(['nmap', '-sV', '-p', str(port), target])
        print(result.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred during service enumeration: {e}")


parser = argparse.ArgumentParser(description="A simple pentest script.")
parser.add_argument("-t", "--target", required=True, help="Target IP address.")
parser.add_argument("-p", "--ports", nargs="+", default=[22, 80, 443], type=int, help="Ports to scan.")

args = parser.parse_args()

open_ports = []
try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(port_scan, args.target, port) for port in args.ports}
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port is not None:
                open_ports.append(port)

    for port in open_ports:
        service_enum(args.target, port)

except KeyboardInterrupt:
    print("\nExiting...")
    try:
        for future in futures:
            future.cancel()
    except:
        pass
