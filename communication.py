import serial
import time
import sys

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    f = open("file.txt", 'r')
    a = ""
    for x in f:
        a += x
    print("a built")
    a = a.encode('utf-8')
    print("a encoded")
    while True:
        ser.write(a)
        print("a written")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
