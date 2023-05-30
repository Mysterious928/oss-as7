DESCRIPTION

This Python script offers a basic penetration testing tool. It can scan specific ports on a target IP address, enumerate services on open ports using nmap, and perform directory brute-forcing using gobuster.

REQUIREMENTS

To successfully run the script, ensure that you have Python 3 installed, along with the following dependencies:

- nmap: This tool is necessary for enumerating services on open ports.
- gobuster: This tool is required for directory brute forcing.

Before executing the script, verify that these dependencies are installed and accessible from your system's PATH.

USAGE

In order to utilize the script, you must supply a target IP address, specify a list of ports for scanning, and provide a wordlist file to be used by gobuster.

The available command-line arguments are as follows:
●	-t, --target: Target IP address. (required)
●	-p, --ports: Ports to scan. Default are ports 22, 80, and 443. (optional)
●	-a, --all-ports: Scan all ports. (optional)
●	-w, --wordlist-file: File path to the wordlist for gobuster. (required)
Here is an example of how to run the script:
	python gbscan.py -t <target_IP> -p <ports> -w <path_to_wordlist>
