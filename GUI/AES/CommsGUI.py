import serial
import tkinter as tk
from tkinter import scrolledtext
from cryptography.fernet import Fernet

# ==== CONFIGURATION ====
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

# Replace this with your generated key!
FERNET_KEY = b'XjJGMojT5GSl2MI6YB3SKoWiDmY3PLAatviEmeXX2p8='
cipher = Fernet(FERNET_KEY)

# ==== GUI Functions ====
def send_message():
    user_input = input_field.get()
    if not user_input.strip():
        return

    encrypted = cipher.encrypt(user_input.encode()).decode()  # encrypted -> string
    try:
        ser.write((encrypted + '\n').encode())
    except:
        output_box.insert(tk.END, "⚠️ Failed to send to Arduino\n")
        return

    output_box.insert(tk.END, f"You: {user_input}\n")
    output_box.insert(tk.END, f"Encrypted (Base64): {encrypted}\n\n")
    input_field.delete(0, tk.END)

# ==== Serial Setup ====
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
except:
    print("⚠️ Couldn't connect to Arduino on /dev/ttyACM0.")
    exit()

# ==== GUI Layout ====
root = tk.Tk()
root.title("AES Secure Comms Terminal")

input_label = tk.Label(root, text="Type your message:")
input_label.pack()

input_field = tk.Entry(root, width=50)
input_field.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

output_box = scrolledtext.ScrolledText(root, width=60, height=15)
output_box.pack(padx=10, pady=10)
output_box.insert(tk.END, "🔒 AES GUI started. Connected to Arduino.\n\n")

root.mainloop()

