import os
import serial
import time

os.chdir('c:/Users/sanme/Desktop/Jackal/Data')
freq = 1.05e5
samplingRate = 1 / freq

PORT = "COM8"
BAUD = 115200

if __name__ == "__main__":

    ser = serial.Serial(
        port=PORT,
        baudrate=BAUD,
        timeout=1
    )
    ser.flush()

    while True:
        if ser.in_waiting > 0:

            ser.write(b"Initiate\n")
            line = ser.readline().decode('utf-8').rstrip()

            if str(line) == "Attempting to connect":

                ser.write(b"Connection Successful!\n")

                line2 = ser.readline().decode('utf-8').rstrip()

                ser.write(b"startCode\n")

                if str(line2) == "Starting program in 2 seconds":

                    print("Enter number of runs")
                    n = int(input())

                    for i in range(0, n):

                        file = open("Data.txt", 'w')
                        time.sleep(2)

                        for j in range(0, 2*freq):
                            data = ser.readline().decode('utf-8').rstrip()

                            file.write(str(data) + '\n')
                            time.sleep(samplingRate)

                        file.close()
