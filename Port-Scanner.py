import socket

import re

#Recognises IPv4 addresses and extracts them
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

#Recognises Port numbers and extracts them
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

#Some Variables ot use later
port_min = 0
port_max = 65535
print("\n***************************************************************")
print(r"""
  _____           _      _____ 
 |  __ \         | |    / ____|                                
 | |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __ 
 |  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |   
 |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|   
""")
print("\n***************************************************************")
print("This Script is VERY BASIC.")
print("It does not differentiate between Filtered or closed ports")
print("***************************************************************")

#An empty list we will use to store the open ports later on
open_ports = []

#Asks the user for an IPv4 adress
while True:
    ip_add_entered = input("\nPlease enter the IP address you want to scan:")
    #Runs the IP from the user through the experssion checker using re that was decalred on line 6
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} IS a valid IPv4 address")
        break


while True:
    print("Enter the range of ports you want to scan in the format int-int e.g 1-80")
    port_range = input("Enter Port Range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ", " "))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break



#Actual Port Scanning starts here!

for port in range(port_min, port_max + 1):

    try:
        #Creates a socket object
        #socket.AF_INET is used to determine ipv4 addresses are being used
        #socket.SOCK_Stream determines that it is a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            #Sets a time-out time of 0.5 seconds. This means that the script will wait 0.5 seconds for a connection
            #extending this time will heel more accurate results
            s.settimeout(0.5)

            #We use the socket object we created called 's' to connect to the IP and Port Range the user inputs
            s.connect((ip_add_entered, port))

            #appends to the empty list 'open_ports' we made earlier
            open_ports.append(port)

    except:

        pass


#loop through the list printing all the items (ports in this case) that were open when the original for loop was ran
for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")


