import serial
import time
import struct
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial('COM8', 115200, timeout=1)
file_name = time.strftime("%Y%m%d-%H%M%S") + ".txt"

data = np.empty((0, 105), dtype=np.int16)

with open(file_name, "w") as f:
    start_time = time.time()
    while time.time() - start_time < 5:
        samples = np.empty((0,), dtype=np.int16)
        for i in range(0, 210, 2):
            sample = struct.unpack('h', ser.read(2))[0]  # unpack 2 bytes as a signed integer
            samples = np.append(samples, sample)

        data = np.vstack((data, samples))
        np.savetxt(f, samples, fmt='%d')

        time.sleep(0.0000095238)  # delay to achieve 105 kHz sampling rate
f.close()
ser.close()

plt.specgram(data.flatten(), NFFT=256, Fs=105000, cmap=plt.cm.jet)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()
