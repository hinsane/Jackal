# Import libraries
import os
import serial
import time
from datetime import datetime

# Change directory to storage location

# Sampling frequency and sampling rate
freq = int(1.05e5)
samplingRate = 1 / freq

# Serial port connection

PORT = "COM8"  # Enter custom port
BAUD = 115200  # Enter baud rate

ser = serial.Serial(
    port=PORT,
    baudrate=BAUD,
    timeout=1  # Change timeout if necessary
)
ser.flush()

# ------------------------------Main loop below---------------------------------------
if __name__ == '__main__':

    while True:
        # Begin connection attempt
        ser.write(b"Initiate\n")
        line = ser.readline().decode('utf-8').rstrip()

        while str(line) != "Attempting to connect":
            line = ser.readline().decode('utf-8').rstrip()

        ser.write(b"Connection Successful!\n")  # Achieved connection

        line2 = ser.readline().decode('utf-8').rstrip()

        ser.write(b"startCode\n")  # Data acquisition begins

        while str(line2) != "Starting program in 2 seconds":

            print("Enter number of runs: \n")  # Provide number of runs
            n = int(input())

            for i in range(0, n):
                timestamp = datetime.now().strftime('%Y%m%d')[:-3]  # Timestamp
                time.sleep(2)
                FileName = timestamp + ".txt"  # Create File

                with open(FileName, 'w') as file:

                    for j in range(0, 2 * freq):
                        data = ser.readline().decode('utf-8').rstrip()

                        file.write(str(data) + '\n')
                        time.sleep(samplingRate)
# ------------------------------Main loop above---------------------------------------
