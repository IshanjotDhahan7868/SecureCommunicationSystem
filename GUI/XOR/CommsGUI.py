import serial
import tkinter as tk
from tkinter import scrolledtext

# ==== Serial Config ====
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600
KEY = 'k'

# ==== XOR Encrypt Function ====
def xor_encrypt(input_text, key):
    return ''.join([chr(ord(char) ^ ord(key)) for char in input_text])

# ==== GUI Functions ====
def send_message():
    user_input = input_field.get()
    if not user_input.strip():
        return

    encrypted = xor_encrypt(user_input, KEY)

    try:
        ser.write((encrypted + '\n').encode())
    except:
        output_box.insert(tk.END, "⚠️ Failed to send to Arduino\n")
        return

    # 🔧 FIXED MISSING PARENTHESIS
    output_box.insert(tk.END, f"You: {user_input}\n")
    output_box.insert(tk.END, f"Encrypted: {repr(encrypted)}\n")

    # Read Arduino reply
    try:
        reply = ser.readline().decode(errors='ignore').strip()
        output_box.insert(tk.END, f"Decrypted (Arduino): {reply}\n\n")
    except:
        output_box.insert(tk.END, "No response from Arduino\n")

    input_field.delete(0, tk.END)

# ==== Setup Serial Port ====
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
except:
    print("⚠️ Couldn't connect to Arduino. Check /dev/ttyACM0.")
    exit()

# ==== Build GUI ====
root = tk.Tk()  # 🔧 FIXED: was "tk.TK()"
root.title("Secure Communication Terminal")  # 🔧 FIXED: was "roo.title"

input_label = tk.Label(root, text="Type your message:")  # 🔧 FIXED: was "LAbel"
input_label.pack()

input_field = tk.Entry(root, width=50)
input_field.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)  # 🔧 FIXED: was "send_btton"
send_button.pack(pady=5)

output_box = scrolledtext.ScrolledText(root, width=60, height=15)
output_box.pack(padx=10, pady=10)
output_box.insert(tk.END, "✅ Connected to Arduino on /dev/ttyACM0\n\n")

root.mainloop()

