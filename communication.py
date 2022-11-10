import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()
    f = open("file.txt", 'r')

    #a = f.read().encode('utf-8')
    a = f.read(1024).encode('utf-8')
    print("a encoded")
    x = ""
    start = time.time()

    while a:
        n = ser.write(a)
        a = f.read(1024).encode('utf-8')
        print("a written to",n," bytes")
        x += ser.read(2048).decode('utf-8').rstrip()

    print(x)
    print("Time: ", time.time() - start, "seconds")
