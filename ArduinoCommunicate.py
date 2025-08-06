import serial

# Connect to Arduino port
SERIAL_PORT = '/dev/ttyACM0'  
BAUD_RATE = 9600
KEY = 'k'

def xor_encrypt(message, key):
    encrypted = ''.join([chr(ord(char) ^ ord(key)) for char in message])
    return encrypted

def main():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
    print("Type a message to encrypt and send to Arduino (CTRL-C to quit)\n")

    try:
        while True:
            user_input = input("You: ")
            encrypted = xor_encrypt(user_input, KEY) 
            ser.write((encrypted + '\n').encode())   
    except KeyboardInterrupt:
        print("\nNow Exiting...")
    finally:
        ser.close()

if __name__ == "__main__":
    main()

