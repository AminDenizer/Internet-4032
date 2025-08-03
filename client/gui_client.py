import tkinter as tk
from tkinter import ttk, messagebox
import socket
import asyncio
import threading
from .quic_base_client import send_quic_message

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Protocol Tester")
        self.geometry("500x400")

        self.protocol = tk.StringVar(value="TCP")
        self.server_address = tk.StringVar(value="localhost")
        self.message = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Protocol selection
        protocol_frame = ttk.LabelFrame(self, text="Protocol")
        protocol_frame.pack(padx=10, pady=10, fill="x")
        ttk.Radiobutton(protocol_frame, text="TCP", variable=self.protocol, value="TCP").pack(side="left", padx=5)
        ttk.Radiobutton(protocol_frame, text="UDP", variable=self.protocol, value="UDP").pack(side="left", padx=5)
        ttk.Radiobutton(protocol_frame, text="QUIC", variable=self.protocol, value="QUIC").pack(side="left", padx=5)

        # Server address
        address_frame = ttk.LabelFrame(self, text="Server Address")
        address_frame.pack(padx=10, pady=10, fill="x")
        ttk.Entry(address_frame, textvariable=self.server_address).pack(fill="x", expand=True)

        # Message
        message_frame = ttk.LabelFrame(self, text="Message")
        message_frame.pack(padx=10, pady=10, fill="x")
        ttk.Entry(message_frame, textvariable=self.message).pack(fill="x", expand=True)

        # Send button
        send_button = ttk.Button(self, text="Send", command=self.send_message)
        send_button.pack(padx=10, pady=10)

        # Response
        response_frame = ttk.LabelFrame(self, text="Response")
        response_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.response_text = tk.Text(response_frame, height=10, width=50)
        self.response_text.pack(fill="both", expand=True)

    def send_message(self):
        protocol = self.protocol.get()
        address = self.server_address.get()
        message = self.message.get()

        if not message:
            messagebox.showerror("Error", "Message cannot be empty")
            return

        self.response_text.delete(1.0, tk.END)

        if protocol == "TCP":
            self.send_tcp(address, message)
        elif protocol == "UDP":
            self.send_udp(address, message)
        elif protocol == "QUIC":
            self.send_quic(address, message)

    def send_tcp(self, address, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((address, 23456))
                s.sendall(message.encode())
                data = s.recv(1024)
                self.response_text.insert(tk.END, data.decode())
        except Exception as e:
            self.response_text.insert(tk.END, f"Error: {e}")

    def send_udp(self, address, message):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.sendto(message.encode(), (address, 12345))
                data, _ = s.recvfrom(1024)
                self.response_text.insert(tk.END, data.decode())
        except Exception as e:
            self.response_text.insert(tk.END, f"Error: {e}")

    def send_quic(self, address, message):
        # QUIC requires asyncio, so we run it in a separate thread
        threading.Thread(target=self._run_quic_client, args=(address, message)).start()

    def _run_quic_client(self, address, message):
        try:
            response = asyncio.run(send_quic_message(address, 4433, message))
            self.response_text.insert(tk.END, response)
        except Exception as e:
            self.response_text.insert(tk.END, f"Error: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
