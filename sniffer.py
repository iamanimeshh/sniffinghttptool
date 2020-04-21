import scapy.all as scapy
from scapy.layers import http
def sniffer(iface):
    scapy.sniff(iface= iface, store= False, prn= pf)

def pf(packets):
    if packets.haslayer(http.HTTPRequest):
      print(packets)

sniffer("eth0")
