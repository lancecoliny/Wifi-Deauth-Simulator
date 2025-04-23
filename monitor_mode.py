import os

def enable_monitor(interface):
    os.system(f"sudo ip link set {interface} down")
    os.system(f"sudo iwconfig {interface} mode monitor")
    os.system(f"sudo ip link set {interface} up")

def disable_monitor(interface):
    os.system(f"sudo ip link set {interface} down")
    os.system(f"sudo iwconfig {interface} mode managed")
    os.system(f"sudo ip link set {interface} up")
