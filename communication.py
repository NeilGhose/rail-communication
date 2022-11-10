import serial
import time
import sys

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()
    f = open("file.txt", 'r')

    #a = f.read().encode('utf-8')
    a = f.read(1024).encode('utf-8')
    print("a encoded")

    while a:
        n = ser.write(a)
        a = f.read(1024).encode('utf-8')
        print("a written to",n," bytes")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
