from scapy.all import ICMP 
from scapy.all import IP
from scapy.all import sr1

if __name__ == "__main__":
    src_ip = "192.168.74.128"
    dest_ip = "www.google.com"

    ip_layer = IP(src = src_ip, dst = dest_ip)
    icmp_req = ICMP(id=100)

    packet = ip_layer / icmp_req

    response = sr1(packet, iface="eth0")
    if response:
        print(response.show())