from scapy.all import ICMP 
from scapy.all import IP
from scapy.all import sr1
from scapy.all import ls

if __name__ == "__main__":
    dest_ip = "www.google.com"

    ip_layer = IP(dst = dest_ip)
    print(ls(ip_layer))  # displaying complete layer info

    # accessing the fields
    print("Destination  = ", ip_layer.dst)

    print("Summary  = ",ip_layer.summary())