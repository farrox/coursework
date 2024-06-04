import serial
import time
import threading

class ArduinoResetController:
    def __init__(self, port, baud_rate=9600, reset_interval=60):
        self.port = port
        self.baud_rate = baud_rate
        self.reset_interval = reset_interval
        self.serial_connection = serial.Serial(port, baud_rate)
        time.sleep(2)  # Wait for the serial connection to initialize
        self.running = False

    def reset_power(self):
        self.serial_connection.write(b'R')  # Send the reset command to Arduino
        print("Power reset initiated")

    def close(self):
        self.serial_connection.close()

    def auto_reset(self):
        self.running = True
        while self.running:
            self.reset_power()
            time.sleep(self.reset_interval)
            
    def start_auto_reset(self):
        self.thread = threading.Thread(target=self.auto_reset)
        self.thread.start()
        
    def stop_auto_reset(self):
        self.running = False
        self.thread.join()

# Save this class in a file, e.g., arduino_reset.py
