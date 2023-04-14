import os
import serial
import time

os.chdir('c:/Users/sanme/Desktop/Jackal/Data')
freq = 1.05e5
samplingRate = 1/freq

print("Enter number of runs")
n = int(input())

PORT = "COM8"
BAUD = 115200

if __name__=="__main__":

    ser = serial.Serial(
    port=PORT,
    baudrate=BAUD,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            signal_1 = "Initiate"
            signal_1 = signal_1.encode('utf-8')

            ser.write(signal_1)
            line = ser.readline().decode().rstrip()

            if str(line)=="Attempting to connect":

                signal_2 = "Connection Successful!"
                signal_2 = signal_1.encode('utf-8')
                ser.write(signal_2)
                
                line2 = ser.readline().decode('utf-8').rstrip()

                signal_3 = "startCode"
                signal_3 = signal_1.encode('utf-8')
                ser.write(signal_3)
                
                if str(line2)=="Starting program in 2 seconds":
                    
                    for i in range (0, n):

                      file = open("Data%d.txt",i, 'w')
                      time.sleep(2)

                      for j in range(0, freq):
                          
                            data = ser.readline().decode('utf-8').rstrip()
                    
                            file.write(str(data)+'\n')
                            time.sleep(samplingRate)
                     
                    
                      file.close()









                